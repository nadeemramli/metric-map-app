import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, acf
from scipy.signal import find_peaks
from ..models import Metric, SeasonalityResult, TrendChangePoint
from django.db import transaction
import logging
from .data_preparation import get_prepared_data

logger = logging.getLogger(__name__)

class FeatureEngineering:
    def __init__(self, metric_id: int):
        self.metric_id = metric_id
        self.metric = Metric.objects.get(id=metric_id)
        data_prep = DataPreparation(metric_id)
        self.df, self.metadata = data_prep.prepare_data()
        self.features = None

    def profile_data(self):
        profile = {
            'length': len(self.df),
            'mean': self.df['value'].mean(),
            'median': self.df['value'].median(),
            'std': self.df['value'].std(),
            'min': self.df['value'].min(),
            'max': self.df['value'].max(),
            'skewness': self.df['value'].skew(),
            'kurtosis': self.df['value'].kurtosis(),
            'q1': self.df['value'].quantile(0.25),
            'q3': self.df['value'].quantile(0.75),
            'iqr': self.df['value'].quantile(0.75) - self.df['value'].quantile(0.25),
            'missing_percentage': (self.df['value'].isnull().sum() / len(self.df)) * 100,
            'autocorrelation': self.df['value'].autocorr(),
            'is_stationary': self.metadata['is_stationary']
        }
        return profile

    def detect_seasonality(self):
        if len(self.df) < 2:
            return None

        result = seasonal_decompose(self.df['value'], model='additive', extrapolate_trend='freq')
        seasonality_strength = 1 - np.var(result.resid) / np.var(result.seasonal + result.resid)
        
        # Determine the seasonality type
        freq = pd.infer_freq(self.df.index)
        if freq in ['D', 'B']:
            seasonality_type = 'daily'
        elif freq in ['W', 'W-MON']:
            seasonality_type = 'weekly'
        elif freq in ['M', 'MS']:
            seasonality_type = 'monthly'
        else:
            seasonality_type = 'unknown'

        seasonality_result, _ = SeasonalityResult.objects.update_or_create(
            metric=self.metric,
            defaults={
                'seasonality_type': seasonality_type,
                'strength': seasonality_strength,
                'period': len(result.seasonal) if result.seasonal is not None else 0
            }
        )
        return seasonality_result

    def detect_trend_changes(self):
        result = adfuller(self.df['value'])
        is_stationary = result[1] <= 0.05  # p-value threshold

        # Simple trend change detection
        rolling_mean = self.df['value'].rolling(window=30).mean()
        trend_changes = (rolling_mean.diff() > 0) != (rolling_mean.diff().shift(1) > 0)
        
        significant_changes = self.df[trend_changes].index

        with transaction.atomic():
            TrendChangePoint.objects.filter(metric=self.metric).delete()
            for change_point in significant_changes:
                TrendChangePoint.objects.create(
                    metric=self.metric,
                    date=change_point,
                    change_type='upward' if rolling_mean.loc[change_point] > rolling_mean.shift(1).loc[change_point] else 'downward',
                    significance=abs(rolling_mean.diff().loc[change_point])
                )

        return {'is_stationary': is_stationary, 'num_change_points': len(significant_changes)}

    def engineer_features(self):
        if self.features is None:
            self.features = {
                'profile': self.profile_data(),
                'seasonality': self.detect_seasonality(),
                'trend_changes': self.detect_trend_changes()
            }
        return self.features

    def compute_dynamic_parameters(self, required_params=None):
        features = self.engineer_features()
        params = {}

        param_functions = {
            'imputation_method': self._get_imputation_method,
            'outlier_method': self._get_outlier_method,
            'forecasting_model': self._get_forecasting_model,
            'max_lag': self._get_max_lag,
            'window_size': self._get_window_size,
            'base_threshold': self._get_base_threshold,
            'context_window': self._get_context_window,
            'correlation_type': self._get_correlation_type,
            'seasonality_period': self._get_seasonality_period,
        }

        if required_params is None:
            required_params = param_functions.keys()

        for param in required_params:
            if param in param_functions:
                params[param] = param_functions[param](features)

        return params

    def _get_imputation_method(self, features):
        if features['profile']['missing_percentage'] < 5:
            return 'mean'
        elif features['profile']['missing_percentage'] < 15:
            return 'interpolate'
        else:
            return 'knn'

    def _get_outlier_method(self, features):
        if features['profile']['skewness'] < 1 and features['profile']['kurtosis'] < 3:
            return {'method': 'iqr', 'threshold': 1.5}
        else:
            return {'method': 'zscore', 'threshold': 3}

    def _get_forecasting_model(self, features):
        if features['seasonality'] and features['seasonality'].strength > 0.6:
            return 'sarima'
        elif features['trend_changes']['is_stationary']:
            return 'arima'
        else:
            return 'prophet'

    def _get_max_lag(self, features):
        if features['seasonality']:
            return min(features['seasonality'].period * 2, features['profile']['length'] // 10)
        else:
            return min(30, features['profile']['length'] // 10)

    def _get_window_size(self, features):
        suggested_window = max(7, min(90, features['profile']['length'] // 10))
        if features['seasonality']:
            suggested_window = max(suggested_window, features['seasonality'].period)
        return suggested_window

    def _get_base_threshold(self, features):
        q1 = np.percentile(self.df['value'], 25)
        q3 = np.percentile(self.df['value'], 75)
        iqr = q3 - q1
        return max(2.0, min(4.0, 1.5 * iqr))

    def _get_context_window(self, features):
        window_size = self._get_window_size(features)
        return max(3, min(15, window_size // 5))

    def _get_correlation_type(self, features):
        _, p_value = stats.normaltest(self.df['value'])
        return 'pearson' if p_value > 0.05 else 'spearman'

    def _get_seasonality_period(self, features):
        if features['seasonality']:
            return features['seasonality'].period
        else:
            autocorr = acf(self.df['value'], nlags=len(self.df) // 2)
            peaks, _ = find_peaks(autocorr, height=0.1, distance=1)
            if len(peaks) > 1:
                return int(np.diff(peaks).mean())
        return None

def get_dynamic_parameters(metric_id: int, required_params=None):
    fe = FeatureEngineering(metric_id)
    return fe.compute_dynamic_parameters(required_params)

def get_data_profile(metric_id: int):
    fe = FeatureEngineering(metric_id)
    return fe.profile_data()