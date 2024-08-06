import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.seasonal import seasonal_decompose
from scipy.signal import find_peaks
from typing import Dict, List, Tuple, Optional
from ..models import Metric, SeasonalityResult, TrendChangePoint
from django.db import transaction
import logging
from .data_preparation import DataPreparation
from .config import Config

logger = logging.getLogger(__name__)

class FeatureEngineering:
    def __init__(self, metric_id: int):
        self.metric_id = metric_id
        self.metric = Metric.objects.get(id=metric_id)
        self.tenant = self.metric.tenant
        data_prep = DataPreparation(metric_id)
        try:
            self.df, self.metadata = data_prep.prepare_data()
        except ValueError as e:
            logger.warning(f"No data available for metric {metric_id}: {str(e)}")
            self.df = pd.DataFrame(columns=['date', 'value'])
            self.metadata = {}
        self._dynamic_parameters: Optional[Dict] = None
        self._engineered_features: Optional[Dict] = None
        self._parameter_type: str = "unknown"

    def get_data(self) -> Tuple[pd.DataFrame, Dict]:
        return self.df, self.metadata

    def compute_dynamic_parameters(self) -> Dict:
        if self._dynamic_parameters is None:
            try:
                data_length = len(self.df)
                if data_length == 0:
                    raise ValueError("No data available for computing dynamic parameters")
                
                data_quality_score = self.metadata.get('data_quality_score', 0)
                
                if data_length < 10 or data_quality_score < Config.MIN_DATA_QUALITY_SCORE:
                    self._dynamic_parameters = self._compute_simple_parameters(data_length, data_quality_score)
                    self._parameter_type = "simple"
                    logger.info(f"Using simple parameters for metric {self.metric_id} due to insufficient data or low quality score")
                else:
                    seasonality_period = self._compute_seasonality_period()
                    forecast_horizon = self._compute_forecast_horizon(data_length, seasonality_period)
                    
                    self._dynamic_parameters = {
                        'seasonality_period': seasonality_period,
                        'forecast_horizon': forecast_horizon,
                        'correlation_window': self._compute_correlation_window(data_length, seasonality_period),
                        'trend_window': self._compute_trend_window(data_length),
                        'anomaly_detection_window': self._compute_anomaly_detection_window(data_length, seasonality_period),
                        'base_threshold': self._compute_base_threshold(),
                        'window_size': self._get_window_size(data_length),
                        'context_window': self._get_context_window(data_length),
                        'global_threshold': Config.GLOBAL_THRESHOLD,
                        'imputation_method': self.metadata.get('imputation_method', 'mean')
                    }
                    self._parameter_type = "dynamic"
                    logger.info(f"Using dynamic parameters for metric {self.metric_id}")
                    
                # Ensure consistency in seasonality period only for larger datasets
                if self._dynamic_parameters['seasonality_period'] is not None and data_length >= 30:
                    max_period = min(365, data_length // 2)
                    self._dynamic_parameters['seasonality_period'] = min(self._dynamic_parameters['seasonality_period'], max_period)
            
            except Exception as e:
                logger.error(f"Error in compute_dynamic_parameters: {str(e)}")
                self._dynamic_parameters = self._compute_simple_parameters(0, 0)
                self._parameter_type = "simple (fallback)"
                logger.warning(f"Falling back to simple parameters for metric {self.metric_id} due to error")
        
        logger.info(f"Parameters for metric {self.metric_id}: {self._parameter_type}")
        logger.debug(f"Parameter values for metric {self.metric_id}: {self._dynamic_parameters}")
        return self._dynamic_parameters

    def _compute_simple_parameters(self, data_length: int) -> Dict:
        return {
            'seasonality_period': None,
            'forecast_horizon': min(data_length // 4, 30),
            'correlation_window': min(data_length, 30),
            'trend_window': min(data_length, 30),
            'anomaly_detection_window': min(data_length // 4, 30),
            'base_threshold': 3.0,
            'window_size': self._get_window_size(data_length),
            'context_window': min(5, max(3, data_length // 73)),
            'global_threshold': Config.GLOBAL_THRESHOLD,
            'imputation_method': 'mean'
        }

    def _compute_seasonality_period(self) -> Optional[int]:
        logger.debug(f"Starting _compute_seasonality_period for metric {self.metric_id}")
        try:
            seasonality_result = self.detect_seasonality()
            return seasonality_result['period']
        except Exception as e:
            logger.error(f"Error in _compute_seasonality_period: {str(e)}")
            return None

    def _compute_forecast_horizon(self, data_length: int, seasonality_period: Optional[int]) -> int:
        try:
            if seasonality_period:
                forecast_horizon = min(seasonality_period, 30)
            else:
                forecast_horizon = min(data_length // 10, 30)
            return max(1, min(int(forecast_horizon), 30))
        except Exception as e:
            logger.error(f"Error in _compute_forecast_horizon: {str(e)}")
            return 7  # Default value

    def _compute_correlation_window(self, data_length: int, seasonality_period: Optional[int]) -> int:
        try:
            if seasonality_period:
                correlation_window = min(2 * seasonality_period, data_length // 2)
            else:
                correlation_window = min(90, data_length // 2)
            return max(7, min(correlation_window, 90))
        except Exception as e:
            logger.error(f"Error in _compute_correlation_window: {str(e)}")
            return 30  # Default value

    def _compute_trend_window(self, data_length: int) -> int:
        try:
            if data_length >= 1000:
                trend_window = max(90, data_length // 10)
            elif data_length >= 500:
                trend_window = max(60, data_length // 10)
            else:
                trend_window = max(30, data_length // 10)
            
            return min(trend_window, data_length // 2)
        except Exception as e:
            logger.error(f"Error in _compute_trend_window: {str(e)}")
            return 30  # Default value

    def _compute_anomaly_detection_window(self, data_length: int, seasonality_period: Optional[int]) -> int:
        try:
            if seasonality_period:
                anomaly_window = min(seasonality_period, 30)
            else:
                anomaly_window = min(data_length // 4, 30)
            return max(7, min(anomaly_window, 30))
        except Exception as e:
            logger.error(f"Error in _compute_anomaly_detection_window: {str(e)}")
            return 14  # Default value

    def _compute_base_threshold(self) -> float:
        try:
            std_dev = self.df['value'].std()
            mean_value = self.df['value'].mean()
            data_quality_score = self.metadata.get('data_quality_score', 0)
            
            if std_dev == 0:  # Constant value dataset
                return 0  # Set to 0 for constant datasets
            
            # Consider seasonality amplitude
            seasonality = self.detect_seasonality()
            seasonality_amplitude = seasonality.get('amplitude', 0) if seasonality else 0
            volatility = self.compute_volatility()
            
            # Use the coefficient of variation as the volatility measure
            volatility_measure = volatility.get('coefficient_of_variation', 0)
            
            base_threshold = max(10, min(seasonality_amplitude + volatility_measure * 100, 20))
            
            # Adjust based on data quality score
            if data_quality_score < 50:
                base_threshold *= 1.2  # Increase threshold for lower quality data
            
            return min(base_threshold, 5.0)  # Cap at 5.0 to avoid extreme values
        except Exception as e:
            logger.error(f"Error in _compute_base_threshold: {str(e)}")
            return 3.0  # Default value
    
    def _create_empty_profile(self) -> Dict:
        return {
            'count': 0,
            'mean': np.nan,
            'median': np.nan,
            'std': np.nan,
            'min': np.nan,
            'max': np.nan,
            'range': np.nan,
            'skewness': np.nan,
            'kurtosis': np.nan,
            'variance': np.nan,
            'coefficient_of_variation': np.nan,
            'percentiles': {
                '1%': np.nan, '5%': np.nan, '25%': np.nan,
                '75%': np.nan, '95%': np.nan, '99%': np.nan
            },
            'missing_values': 0,
            'missing_percentage': 0,
            'unique_values': 0,
            'time_range': {'start': None, 'end': None, 'duration_days': 0},
            'frequency': None,
            'trend': None,
            'stationarity': None,
            'outliers': {'count': 0, 'percentage': 0}
        }
    
    def profile_data(self) -> Dict:
        try:
            if len(self.df) < 2:
                logger.warning("Not enough data points to create a profile")
                return self._create_empty_profile()

            values = self.df['value'].dropna()
            dates = self.df['date'].dropna()

            profile = {
                'count': len(values),
                'mean': values.mean(),
                'median': values.median(),
                'std': values.std(),
                'min': values.min(),
                'max': values.max(),
                'range': values.max() - values.min(),
                'skewness': stats.skew(values),
                'kurtosis': stats.kurtosis(values),
                'variance': values.var(),
                'coefficient_of_variation': values.std() / values.mean() if values.mean() != 0 else np.nan,
                'percentiles': {
                    '1%': np.percentile(values, 1),
                    '5%': np.percentile(values, 5),
                    '25%': np.percentile(values, 25),
                    '75%': np.percentile(values, 75),
                    '95%': np.percentile(values, 95),
                    '99%': np.percentile(values, 99)
                },
                'missing_values': values.isnull().sum(),
                'missing_percentage': (values.isnull().sum() / len(values)) * 100,
                'unique_values': values.nunique(),
                'time_range': {
                    'start': dates.min().isoformat(),
                    'end': dates.max().isoformat(),
                    'duration_days': (dates.max() - dates.min()).days
                },
                'frequency': self._infer_frequency(dates),
                'trend': self._detect_trend(values),
                'stationarity': self._check_stationarity(values),
                'outliers': self._detect_outliers(values)
            }

            return profile

        except Exception as e:
            logger.error(f"Error in profile_data: {str(e)}")
            return self._create_empty_profile()
    
    def _infer_frequency(self, dates: pd.Series) -> str:
        try:
            return pd.infer_freq(dates) or 'Unknown'
        except Exception:
            return 'Unknown'

    def _detect_trend(self, values: pd.Series) -> str:
        try:
            slope, _, _, _, _ = stats.linregress(range(len(values)), values)
            if slope > 0:
                return 'Increasing'
            elif slope < 0:
                return 'Decreasing'
            else:
                return 'No trend'
        except Exception:
            return 'Unknown'

    def _check_stationarity(self, values: pd.Series) -> str:
        try:
            result = stats.adfuller(values)
            return 'Stationary' if result[1] < 0.05 else 'Non-stationary'
        except Exception:
            return 'Unknown'

    def _detect_outliers(self, values: pd.Series) -> Dict:
        try:
            q1 = values.quantile(0.25)
            q3 = values.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - (1.5 * iqr)
            upper_bound = q3 + (1.5 * iqr)
            outliers = values[(values < lower_bound) | (values > upper_bound)]
            return {
                'count': len(outliers),
                'percentage': (len(outliers) / len(values)) * 100
            }
        except Exception:
            return {'count': 0, 'percentage': 0}

    def detect_seasonality(self) -> Dict:
        try:
            if len(self.df) < 2:
                logger.warning("Not enough data points to detect seasonality")
                return {'period': None, 'type': None, 'strength': 0, 'amplitude': 0, 'component': None}

            values = self.df['value'].dropna()

            # FFT analysis
            fft_result = np.abs(np.fft.fft(values))
            frequencies = np.fft.fftfreq(len(values))
            positive_freq_idx = np.where(frequencies > 0)[0]
            main_freq_idx = np.argmax(fft_result[positive_freq_idx])
            fft_period = int(1 / frequencies[positive_freq_idx[main_freq_idx]])

            # ACF analysis (from _compute_seasonality_period)
            acf_result = acf(values, nlags=len(values) // 2)
            peaks, _ = find_peaks(acf_result)
            if len(peaks) == 0:
                logger.info("No clear seasonality detected using ACF")
                return {'period': None, 'type': None, 'strength': 0, 'amplitude': 0, 'component': None}

            acf_period = peaks[0]

            # Use the smaller of the two periods, but ensure it's at least 2
            seasonality_period = max(2, min(fft_period, acf_period))
            
            # Determine seasonality type
            seasonality_type, adjusted_period = self._classify_seasonality_type(seasonality_period)

            try:
                # Seasonal decomposition
                result = seasonal_decompose(values, model='additive', period=adjusted_period)
                seasonal = result.seasonal
                residual = result.resid

                strength = 1 - np.var(residual) / np.var(seasonal + residual)
                amplitude = np.max(seasonal) - np.min(seasonal)

                with transaction.atomic():
                    seasonality_result, created = SeasonalityResult.objects.update_or_create(
                        metric=self.metric,
                        seasonality_type=seasonality_type,
                        defaults={
                            'period': adjusted_period,
                            'strength': strength
                        }
                    )

                logger.info(f"Seasonality detected: type={seasonality_type}, period={adjusted_period}, strength={strength:.2f}")
                return {
                    'period': seasonality_result.period,
                    'type': seasonality_result.seasonality_type,
                    'strength': seasonality_result.strength,
                    'amplitude': amplitude,
                    'component': seasonal.tolist()
                }
            except ValueError as ve:
                logger.error(f"Error in seasonal decomposition: {str(ve)}")
                return {'period': None, 'type': None, 'strength': 0, 'amplitude': 0, 'component': None}
        except Exception as e:
            logger.error(f"Error in detect_seasonality: {str(e)}")
            return {'period': None, 'type': None, 'strength': 0, 'amplitude': 0, 'component': None}

    def _classify_seasonality_type(self, period: int) -> Tuple[str, int]:
        """
        Classify the seasonality type based on the detected period.
        Returns a tuple of (seasonality_type, adjusted_period).
        """
        if period <= 1:
            return 'none', period
        elif 2 <= period <= 3:
            return 'daily', period
        elif 4 <= period <= 8:
            return 'weekly', 7
        elif 25 <= period <= 35:
            return 'monthly', 30
        elif 350 <= period <= 380:
            return 'yearly', 365
        else:
            return 'custom', period
    
    def engineer_features(self) -> Dict:
        if self._engineered_features is None:
            try:
                if len(self.df) == 0:
                    raise ValueError("No data available for feature engineering")

                # Get dynamic parameters
                dynamic_params = self._dynamic_parameters()

                features = {
                    'profile': self.profile_data(),
                    'seasonality': self.detect_seasonality(),
                    'trend_changes': self.detect_trend_changes(),
                    'volatility': self.compute_volatility(),
                    'outlier_method': self._get_outlier_method(),
                    'forecasting_model': self._get_forecasting_model(),
                    'max_lag': self._get_max_lag(),
                    'window_size': dynamic_params['window_size'],
                    'context_window': dynamic_params['context_window'],
                    'correlation_type': self._get_correlation_type(),
                    'seasonality_period': dynamic_params['seasonality_period'],
                    'forecast_horizon': dynamic_params['forecast_horizon'],
                    'correlation_window': dynamic_params['correlation_window'],
                    'trend_window': dynamic_params['trend_window'],
                    'anomaly_detection_window': dynamic_params['anomaly_detection_window'],
                    'base_threshold': dynamic_params['base_threshold'],
                    'global_threshold': dynamic_params['global_threshold'],
                    'imputation_method': dynamic_params['imputation_method']
                }

                # Add lagged features
                for lag in range(1, min(features['max_lag'] + 1, len(self.df))):
                    self.df[f'lag_{lag}'] = self.df['value'].shift(lag)

                # Add rolling statistics
                window_size = features['window_size']
                self.df['rolling_mean'] = self.df['value'].rolling(window=window_size).mean()
                self.df['rolling_std'] = self.df['value'].rolling(window=window_size).std()

                # Add time-based features
                self.df['day_of_week'] = self.df.index.dayofweek
                self.df['month'] = self.df.index.month
                self.df['is_weekend'] = self.df.index.dayofweek.isin([5, 6]).astype(int)

                self._engineered_features = features

            except Exception as e:
                logger.error(f"Error in engineer_features: {str(e)}")
                self._engineered_features = {}

        return self._engineered_features

    def compute_trend(self) -> Dict:
        try:
            if len(self.df) < 2:
                return {'slope': 0, 'intercept': 0, 'strength': 0}

            x = np.arange(len(self.df)).reshape(-1, 1)
            y = self.df['value'].values
            slope, intercept, r_value, _, _ = stats.linregress(x.flatten(), y)
            trend_strength = r_value ** 2
            return {
                'slope': slope,
                'intercept': intercept,
                'strength': trend_strength
            }
        except Exception as e:
            logger.error(f"Error in compute_trend: {str(e)}")
            return {'slope': 0, 'intercept': 0, 'strength': 0}

    def compute_volatility(self) -> Dict:
        try:
            if len(self.df) < 2:
                return {'std_dev': 0, 'coefficient_of_variation': 0, 'average_true_range': 0}

            # Calculate percentage changes
            pct_changes = self.df['value'].pct_change().dropna()
            
            # Calculate standard deviation of percentage changes
            std_dev = pct_changes.std()
            
            # Calculate coefficient of variation
            cv = self.df['value'].std() / self.df['value'].mean() if self.df['value'].mean() != 0 else 0

            # Calculate average true range (ATR)
            high = self.df['value'].rolling(window=2).max()
            low = self.df['value'].rolling(window=2).min()
            close = self.df['value']
            tr = pd.concat([high - low, abs(high - close.shift()), abs(low - close.shift())], axis=1).max(axis=1)
            atr = tr.rolling(window=14).mean().iloc[-1]

            return {
                'std_dev': std_dev,
                'coefficient_of_variation': cv,
                'average_true_range': atr
            }
        except Exception as e:
            logger.error(f"Error in compute_volatility: {str(e)}")
            return {'std_dev': 0, 'coefficient_of_variation': 0, 'average_true_range': 0}

    def detect_trend_changes(self) -> Dict:
        try:
            if len(self.df) < 30:
                return {'is_stationary': True, 'num_change_points': 0, 'change_points': []}

            trend_window = self.compute_dynamic_parameters()['trend_window']
            rolling_mean = self.df['value'].rolling(window=trend_window).mean()
            trend_changes = (rolling_mean.diff() > 0) != (rolling_mean.diff().shift(1) > 0)
            
            significant_changes = self.df[trend_changes].index

            with transaction.atomic():
                TrendChangePoint.objects.filter(metric=self.metric).delete()
                for change_point in significant_changes:
                    TrendChangePoint.objects.create(
                        metric=self.metric,
                        date=change_point,
                        direction='upward' if rolling_mean.loc[change_point] > rolling_mean.shift(1).loc[change_point] else 'downward',
                        significance=None  # Calculate significance if possible, or set to None
                    )

            # Ensure is_stationary is a boolean
            is_stationary = bool(self.metadata.get('is_stationary', False))

            return {'is_stationary': is_stationary, 'num_change_points': len(significant_changes), 'change_points': significant_changes.tolist()}
        except Exception as e:
            logger.error(f"Error in detect_trend_changes: {str(e)}")
            return {'is_stationary': True, 'num_change_points': 0, 'change_points': []}

    def _get_outlier_method(self, features):
        try:
            if features['profile']['skewness'] < 1 and features['profile']['kurtosis'] < 3:
                return {'method': 'iqr', 'threshold': 1.5}
            else:
                return {'method': 'zscore', 'threshold': 3}
        except Exception as e:
            logger.error(f"Error in _get_outlier_method: {str(e)}")
            return {'method': 'zscore', 'threshold': 3}

    def _get_forecasting_model(self):
        try:
            features = self.engineer_features()
            if features.get('seasonality_strength', 0) > 0.6:
                return 'sarima'
            elif features.get('trend_changes', {}).get('is_stationary', False):
                return 'arima'
            else:
                return 'prophet'
        except Exception as e:
            logger.error(f"Error in _get_forecasting_model: {str(e)}")
            return 'prophet'  # Default to prophet in case of error

    def _get_max_lag(self):
        try:
            features = self.engineer_features()
            if features.get('seasonality_period', None):
                return min(features['seasonality_period'] * 2, len(self.df) // 10)
            else:
                return min(30, len(self.df) // 10)
        except Exception as e:
            logger.error(f"Error in _get_max_lag: {str(e)}")
            return 30  # Default value

    # Getting window size clusters, related with seasonality period below.
    def _get_window_size(self, data_length: int) -> int:
        try:
            # Use a separate method to get seasonality period to avoid circular dependency
            seasonality_period = self._get_seasonality_period()
            suggested_window = max(7, min(90, data_length // 10))
            if seasonality_period:
                suggested_window = max(suggested_window, seasonality_period)
            return suggested_window
        except Exception as e:
            logger.error(f"Error in _get_window_size: {str(e)}")
            return min(30, max(7, data_length // 12))
    
    def _get_seasonality_period(self) -> Optional[int]:
        try:
            # Implement a simplified version of seasonality detection here
            # This should not depend on engineer_features or compute_dynamic_parameters
            # For example:
            from statsmodels.tsa.seasonal import seasonal_decompose
            result = seasonal_decompose(self.df['value'], model='additive', period=1)
            seasonality = result.seasonal
            if seasonality is not None and len(seasonality) > 0:
                return len(seasonality)
            return None
        except Exception as e:
            logger.error(f"Error in _get_seasonality_period: {str(e)}")
            return None

    def _get_context_window(self, data_length: int) -> int:
        try:
            window_size = self._get_window_size(data_length)
            return max(3, min(15, window_size // 5))
        except Exception as e:
            logger.error(f"Error in _get_context_window: {str(e)}")
            return 5  # Default value

    def _get_correlation_type(self):
        try:
            _, p_value = stats.normaltest(self.df['value'])
            return 'pearson' if p_value > 0.05 else 'spearman'
        except Exception as e:
            logger.error(f"Error in _get_correlation_type: {str(e)}")
            return 'pearson'  # Default value

def get_dynamic_parameters(metric_id: int, required_params: Optional[List[str]] = None) -> Dict:
    fe = FeatureEngineering(metric_id)
    params = fe.compute_dynamic_parameters()
    logger.info(f"Retrieved {fe._parameter_type} parameters for metric {metric_id}")
    if required_params is None:
        return params
    else:
        return {param: params[param] for param in required_params if param in params}

def get_engineered_features(metric_id: int) -> Dict:
    fe = FeatureEngineering(metric_id)
    return fe.engineer_features()

"""
FeatureEngineering class for extracting and creating features from prepared metric data.

This class handles the creation of additional features and data transformations, including:
- Detecting and extracting seasonality
- Creating lagged features
- Calculating rolling statistics
- Performing time-based feature extraction

Data Flow:
1. Load prepared data from DataPreparation
2. Compute seasonality
3. Create lagged features
4. Calculate rolling statistics
5. Extract time-based features
6. Profile the engineered data

Output Format:
A pandas DataFrame containing the original data along with engineered features.

Output Example:
pd.DataFrame({
    'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'value': [100.0, 101.5, 99.8],
    'lag_1': [NaN, 100.0, 101.5],
    'rolling_mean_7': [NaN, NaN, 100.43],
    'is_weekend': [0, 1, 0],
    'month': [1, 1, 1],
    'day_of_week': [2, 3, 4]
})
"""
