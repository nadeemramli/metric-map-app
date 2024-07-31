# anomaly_detection.py

import pandas as pd
import numpy as np
import logging
from .data_preparation import get_prepared_data
from .feature_engineering import FeatureEngineering

logger = logging.getLogger(__name__)

class AnomalyDetector:
    def __init__(self, metric_id: int):
        self.metric_id = metric_id
        self.df, self.metadata = get_prepared_data(metric_id)
        self.fe = FeatureEngineering(metric_id)
        self.features = self.fe.engineer_features()
        self.dynamic_params = self.fe.compute_dynamic_parameters()

    def detect_anomalies(self) -> pd.DataFrame:
        try:
            if len(self.df) < 14:
                logger.warning("Not enough data for anomaly detection")
                return pd.DataFrame()

            self.seasonality_period = self.dynamic_params.get('seasonality_period')
            self.window_size = self.dynamic_params.get('window_size')
            self.base_threshold = self.dynamic_params.get('base_threshold')
            self.context_window = self.dynamic_params.get('context_window')

            logger.info(f"Detected seasonality period: {self.seasonality_period}")
            logger.info(f"Determined window size: {self.window_size}")
            logger.info(f"Determined base threshold: {self.base_threshold}")
            logger.info(f"Determined context window: {self.context_window}")

            """
            Detect anomalies in the metric data.

            Args:
                window (int): Rolling window size for anomaly detection.
                base_threshold (float): Base threshold for z-score to consider a point anomalous.
                seasonality_period (Optional[int]): Period of seasonality in the data. If None, it will be automatically detected.
                context_window (int): Window size for contextual anomaly detection.
            """

            logger.info(f"Starting anomaly detection for metric {self.metric.id}")
            logger.info(f"Data shape: {self.df.shape}")
            logger.info(f"Data summary: {self.df['value'].describe()}")
            
            # Automatically detect seasonality if not provided
            if seasonality_period is None:
                seasonality_period = self._detect_seasonality_period()
                logger.info(f"Automatically detected seasonality period: {seasonality_period}")

            # Calculate seasonal component
            seasonal = self.df['value'].diff(seasonality_period).fillna(0)
            
            # Remove seasonality from the data
            deseasonalized = self.df['value'] - seasonal
            
            logger.info(f"Deseasonalized data summary: {deseasonalized.describe()}")
            
            # Calculate rolling median and MAD
            rolling_median = deseasonalized.rolling(window=window, center=True).median()
            rolling_mad = deseasonalized.rolling(window=window, center=True).apply(lambda x: np.median(np.abs(x - np.median(x))))

            # Calculate modified z-scores
            modified_z_scores = 0.6745 * (deseasonalized - rolling_median) / rolling_mad
            
            logger.info(f"Modified z-scores summary: {modified_z_scores.describe()}")

            # Calculate adaptive threshold
            adaptive_threshold = base_threshold * (1 + 0.1 * np.log1p(rolling_mad))
            
            logger.info(f"Adaptive threshold summary: {adaptive_threshold.describe()}")
            
            # Calculate contextual z-scores
            context_z_scores =  modified_z_scores.rolling(window=context_window, center=True).apply(lambda x: (x[context_window//2] - x.mean()) / x.std())

            logger.info(f"Contextual z-scores summary: {context_z_scores.describe()}")
            
            # Global outlier detection
            global_mean = deseasonalized.mean()
            global_std = deseasonalized.std()
            global_threshold = 5  # Detect values more than 5 standard deviations from the mean

            # Combine global and local anomaly detection
            anomaly_mask = (
                (abs(modified_z_scores) > adaptive_threshold) |
                (abs(context_z_scores) > base_threshold) |
                (abs(deseasonalized - global_mean) > global_threshold * global_std)
            )
            
            logger.info(f"Number of anomalies detected: {anomaly_mask.sum()}")

            # Get anomalies using the mask
            anomalies = self.df[anomaly_mask].copy()
            anomalies['anomaly_score'] = np.maximum(
                abs(modified_z_scores[anomaly_mask]),
                abs(context_z_scores[anomaly_mask]),
                abs(deseasonalized[anomaly_mask] - global_mean) / global_std
            )

            logger.info(f"Anomalies detected:\n{anomalies}")

            
            logger.info(f"Detected and saved {len(anomalies)} anomalies for metric {self.metric.id}")

            return anomalies

        except Exception as e:
            logger.error(f"Error in anomaly detection for metric {self.metric_id}: {str(e)}")
            return pd.DataFrame()