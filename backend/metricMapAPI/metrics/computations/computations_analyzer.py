# analyze.py

from typing import Dict, List, Tuple, Any

import logging
import numpy as np
import pandas as pd
from scipy.stats import kendalltau
from sklearn.linear_model import LinearRegression
from .data_preparation import get_prepared_data
from .feature_engineering import FeatureEngineering
from django.apps import apps

logger = logging.getLogger(__name__)

class Analyzer:
    def __init__(self, metric_id: int, prepared_data=None, dynamic_params=None, engineered_features=None):
        self.metric_id = metric_id
        if prepared_data is not None:
            self.df, self.metadata = prepared_data, {}
        else:
            self.df, self.metadata = self.get_prepared_data()
        
        self.fe = FeatureEngineering(metric_id)
        self.features = engineered_features if engineered_features is not None else self.fe.engineer_features()
        self.dynamic_params = dynamic_params if dynamic_params is not None else self.fe.compute_dynamic_parameters()
        self.metric = self.get_metric()
        self.client = self.metric.client

    def get_metric(self):
        Metric = apps.get_model('metrics', 'Metric')
        return Metric.objects.get(id=self.metric_id)

    def get_prepared_data(self):
        DataPreparation = apps.get_model('metrics', 'DataPreparation')
        return DataPreparation(metric_id=self.metric_id, client=self.client).get_prepared_data()

    def analyze(self):
        trend_analysis = self.analyze_trend()
        technical_indicators = self.calculate_technical_indicators()
        seasonality = self.detect_seasonality()
        trend_changes = self.detect_trend_changes()
        return {
            'trend': trend_analysis,
            'technical_indicators': technical_indicators,
            'seasonality': seasonality,
            'trend_changes': trend_changes
        }

    def calculate_moving_averages(self) -> Dict[str, Dict[str, float]]:
        try:
            windows = self.dynamic_params.get('ma_windows', [7, 14, 30, 90])
            moving_averages = {}

            for window in windows:
                sma = self.df['value'].rolling(window=window).mean().iloc[-1]
                ema = self.df['value'].ewm(span=window, adjust=False).mean().iloc[-1]
                
                # Calculate WMA
                weights = np.arange(1, window + 1)
                wma = self.df['value'].rolling(window=window).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True).iloc[-1]

                moving_averages[f'{window}_day'] = {
                    'SMA': sma,
                    'EMA': ema,
                    'WMA': wma
                }

            logger.info(f"Calculated moving averages for metric {self.metric_id}")
            return moving_averages
        except Exception as e:
            logger.error(f"Error calculating moving averages for metric {self.metric_id}: {str(e)}")
            raise

    def calculate_technical_indicators(self) -> Dict[str, float]:
        try:
            window = self.dynamic_params.get('window_size', 14)
            # Stochastic Oscillator
            low_min = self.df['value'].rolling(window=window).min()
            high_max = self.df['value'].rolling(window=window).max()
            k = 100 * (self.df['value'] - low_min) / (high_max - low_min)
            d = k.rolling(window=3).mean()
            
            # RSI
            delta = self.df['value'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            
            latest_date = self.df.index[-1]
            indicators = {
                'date': latest_date,
                'stochastic_k': k.iloc[-1],
                'stochastic_d': d.iloc[-1],
                'rsi': rsi.iloc[-1],
                'percent_change': self.df['value'].pct_change(periods=window).iloc[-1] * 100,
            }
            
            # Add moving averages
            moving_averages = self.calculate_moving_averages()
            for window, ma_values in moving_averages.items():
                indicators.update({f'{window}_{ma_type}': value for ma_type, value in ma_values.items()})
            
            logger.info(f"Calculated technical indicators for metric {self.metric_id}")
            return indicators
        except Exception as e:
            logger.error(f"Error calculating technical indicators for metric {self.metric_id}: {str(e)}")
            raise

    def analyze_trend(self) -> Dict[str, Any]:
        try:
            if len(self.df) < 2:
                logger.warning(f"Not enough data for trend analysis for metric {self.metric_id}")
                return {}

            ts = self.df['value']
            
            window_size = self.dynamic_params.get('trend_window_size', 14)
            trend_threshold = self.dynamic_params.get('trend_threshold', 0.05)

            # Validate input data
            if not isinstance(ts, pd.Series) or ts.empty:
                logger.error(f"Invalid input data for trend analysis for metric {self.metric_id}")
                return {}

            # Calculate rolling mean
            rolling_mean = ts.rolling(window=window_size).mean()

            # Perform Mann-Kendall test
            tau, p_value = kendalltau(ts.index, ts.values)

            # Fit linear regression
            X = np.arange(len(ts)).reshape(-1, 1)
            y = ts.values.reshape(-1, 1)
            reg = LinearRegression().fit(X, y)
            slope = reg.coef_[0][0]
            r_squared = reg.score(X, y)

            # Determine trend type
            if p_value <= trend_threshold:
                trend_type = 'Upward' if tau > 0 else 'Downward'
            else:
                trend_type = 'No significant trend'

            trend_results = {
                'trend_type': trend_type,
                'start_date': self.df.index[0],
                'end_date': self.df.index[-1],
                'trend_value': ts.iloc[-1],
                'slope': slope,
                'notes': f'Mann-Kendall p-value: {p_value}, tau: {tau}, R-squared: {r_squared}'
            }

            logger.info(f"Analyzed trend for metric {self.metric_id}")
            return trend_results

        except Exception as e:
            logger.error(f"Error analyzing trend for metric {self.metric_id}: {str(e)}")
            return {}

    def detect_trend_changes(self) -> List[Dict[str, Any]]:
        try:
            def pettitt_test(x: np.ndarray) -> Tuple[int, float]:
                n = len(x)
                k = range(n)
                t = [np.sum(np.sign(x[i] - x[j]) for j in range(i)) for i in k]
                k_max = max(abs(i) for i in t)
                change_point = t.index(k_max) if k_max in t else t.index(-k_max)
                p_value = 2 * np.exp(-6 * k_max**2 / (n**3 + n**2))
                return change_point, p_value

            change_point, p_value = pettitt_test(self.df['value'].values)
            change_date = self.df.index[change_point]
            change_type = 'upward' if self.df['value'].iloc[change_point] < self.df['value'].iloc[change_point+1] else 'downward'
            
            trend_change = {
                'date': change_date,
                'change_type': change_type,
                'significance': 1 - p_value
            }
            
            logger.info(f"Detected trend change point for metric {self.metric_id}")
            return [trend_change]
        except Exception as e:
            logger.error(f"Error detecting trend changes for metric {self.metric_id}: {str(e)}")
            raise

    def detect_seasonality(self) -> Dict[str, Any]:
        try:
            FeatureEngineering = apps.get_model('metrics', 'FeatureEngineering')
            seasonality_result = FeatureEngineering(metric_id=self.metric_id).detect_seasonality()
            if seasonality_result is None:
                return {}
            
            return {
                'seasonality_strength': seasonality_result.strength,
                'period': seasonality_result.period,
                'seasonality_type': seasonality_result.seasonality_type
            }
        except Exception as e:
            logger.error(f"Error detecting seasonality for metric {self.metric_id}: {str(e)}")
            return {}

    def calculate_percent_change(self, old_value: float, new_value: float) -> float:
        if old_value == 0:
            return 0
        return ((new_value - old_value) / old_value) * 100