# anomaly_detection.py

import pandas as pd
import numpy as np
import logging
from typing import Tuple
from .data_preparation import DataPreparation
from .feature_engineering import FeatureEngineering
from django.apps import apps

logger = logging.getLogger(__name__)

class AnomalyDetector:
    def __init__(self, metric_id, prepared_data=None, dynamic_params=None, engineered_features=None):
        self.metric_id = metric_id
        if prepared_data is not None:
            self.df, self.metadata = prepared_data
        else:
            Metric = apps.get_model('metrics', 'Metric')
            self.metric = Metric.objects.get(id=self.metric_id)
            data_prep = DataPreparation(metric_id, self.metric.tenant)
            self.df, self.metadata = data_prep.prepare_data()
        
        self.fe = FeatureEngineering(self.metric_id)
        self.features = engineered_features if engineered_features is not None else self.fe.engineer_features()
        self.dynamic_params = dynamic_params if dynamic_params is not None else self.fe.compute_dynamic_parameters()
        self.metric = self.get_metric()
        self.tenant = self.metric.tenant
        
        required_params = ['seasonality_period', 'window_size', 'base_threshold', 'context_window', 'global_threshold']
        
        missing_params = [param for param in required_params if param not in self.dynamic_params]
        if missing_params:
            raise ValueError(f"Missing required dynamic parameters: {', '.join(missing_params)}")

        # Initialize dynamic parameters
        self.seasonality_period = self.dynamic_params['seasonality_period']
        self.window_size = self.dynamic_params['window_size']
        self.base_threshold = self.dynamic_params['base_threshold']
        self.context_window = self.dynamic_params['context_window']
        self.global_threshold = self.dynamic_params['global_threshold']

        logger.info(f"Initialized AnomalyDetector for metric {self.metric_id}")
        logger.info(f"Seasonality period: {self.seasonality_period}")
        logger.info(f"Window size: {self.window_size}")
        logger.info(f"Base threshold: {self.base_threshold}")
        logger.info(f"Context window: {self.context_window}")
        logger.info(f"Global threshold: {self.global_threshold}")

    def get_metric(self):
        Metric = apps.get_model('metrics', 'Metric')
        return Metric.objects.get(id=self.metric_id)

    def detect_anomalies(self) -> pd.DataFrame:
        try:
            if self.df is None or len(self.df) < self.window_size:
                logger.warning(f"Not enough data for anomaly detection for metric {self.metric_id}")
                return pd.DataFrame(columns=['date', 'value', 'anomaly_score', 'type'])

            logger.info(f"Starting anomaly detection for metric {self.metric_id}")
            self._log_data_summary()

            self._ensure_datetime_index()
            deseasonalized = self._deseasonalize_data()
            modified_z_scores = self._calculate_modified_z_scores(deseasonalized)
            adaptive_threshold = self._calculate_adaptive_threshold(deseasonalized)
            context_z_scores = self._calculate_contextual_z_scores(modified_z_scores)
            global_mean, global_std = self._calculate_global_statistics(deseasonalized)

            anomaly_mask = self._create_anomaly_mask(modified_z_scores, context_z_scores, deseasonalized, adaptive_threshold, global_mean, global_std)
            anomalies = self._create_anomalies_dataframe(anomaly_mask, modified_z_scores, context_z_scores, deseasonalized, global_mean, global_std)

            logger.info(f"Detected {len(anomalies)} anomalies for metric {self.metric_id}")
            return anomalies

        except Exception as e:
            logger.error(f"Error in anomaly detection for metric {self.metric_id}: {str(e)}")
            return pd.DataFrame(columns=['date', 'value', 'anomaly_score', 'type'])

    def _log_data_summary(self) -> None:
        logger.info(f"Data shape: {self.df.shape}")
        logger.info(f"Data summary: {self.df['value'].describe()}")

    def _ensure_datetime_index(self) -> None:
        if not isinstance(self.df.index, pd.DatetimeIndex):
            if 'date' in self.df.columns:
                self.df = self.df.set_index('date')
            else:
                raise ValueError("DataFrame does not have a 'date' column to set as index")
        self.df.index = pd.to_datetime(self.df.index)

    def _deseasonalize_data(self) -> pd.Series:
        if self.seasonality_period:
            seasonal = self.df['value'].diff(self.seasonality_period).fillna(0)
            deseasonalized = self.df['value'] - seasonal
        else:
            deseasonalized = self.df['value']
        logger.info(f"Deseasonalized data summary: {deseasonalized.describe()}")
        return deseasonalized

    def _calculate_modified_z_scores(self, deseasonalized: pd.Series) -> pd.Series:
        rolling_median = deseasonalized.rolling(window=self.window_size, center=True).median()
        rolling_mad = deseasonalized.rolling(window=self.window_size, center=True).apply(lambda x: np.median(np.abs(x - np.median(x))))
        modified_z_scores = 0.6745 * (deseasonalized - rolling_median) / rolling_mad
        logger.info(f"Modified z-scores range: {modified_z_scores.min()} to {modified_z_scores.max()}")
        logger.info(f"Modified z-scores summary: {modified_z_scores.describe()}")
        return modified_z_scores

    def _calculate_adaptive_threshold(self, deseasonalized: pd.Series) -> pd.Series:
        rolling_mad = deseasonalized.rolling(window=self.window_size, center=True).apply(lambda x: np.median(np.abs(x - np.median(x))))
        adaptive_threshold = self.base_threshold * (1 + 0.1 * np.log1p(rolling_mad))
        logger.info(f"Adaptive threshold range: {adaptive_threshold.min()} to {adaptive_threshold.max()}")
        logger.info(f"Adaptive threshold summary: {adaptive_threshold.describe()}")
        return adaptive_threshold

    def _calculate_contextual_z_scores(self, modified_z_scores: pd.Series) -> pd.Series:
        context_z_scores = modified_z_scores.rolling(window=self.context_window, center=True).apply(lambda x: (x[self.context_window//2] - x.mean()) / x.std())
        logger.info(f"Contextual z-scores range: {context_z_scores.min()} to {context_z_scores.max()}")
        logger.info(f"Contextual z-scores summary: {context_z_scores.describe()}")
        return context_z_scores

    def _calculate_global_statistics(self, deseasonalized: pd.Series) -> Tuple[float, float]:
        global_mean = deseasonalized.mean()
        global_std = deseasonalized.std()
        logger.info(f"Global mean: {global_mean}, Global std: {global_std}")
        return global_mean, global_std

    def _create_anomaly_mask(self, modified_z_scores: pd.Series, context_z_scores: pd.Series, 
                             deseasonalized: pd.Series, adaptive_threshold: pd.Series, 
                             global_mean: float, global_std: float) -> pd.Series:
        anomaly_mask = (
            (abs(modified_z_scores) > adaptive_threshold) |
            (abs(context_z_scores) > self.base_threshold) |
            (abs(deseasonalized - global_mean) > self.global_threshold * global_std)
        )
        logger.info(f"Number of anomalies detected: {anomaly_mask.sum()}")
        return anomaly_mask

    def _create_anomalies_dataframe(self, anomaly_mask: pd.Series, modified_z_scores: pd.Series, 
                                    context_z_scores: pd.Series, deseasonalized: pd.Series, 
                                    global_mean: float, global_std: float) -> pd.DataFrame:
        anomalies = self.df[anomaly_mask].copy()
        anomalies['anomaly_score'] = np.maximum(
            abs(modified_z_scores[anomaly_mask]),
            abs(context_z_scores[anomaly_mask]),
            abs(deseasonalized[anomaly_mask] - global_mean) / global_std
        )
        anomalies['type'] = 'point'  # You can add more sophisticated type detection if needed
        anomalies = anomalies.reset_index()
        anomalies = anomalies[['date', 'value', 'anomaly_score', 'type']]
        return anomalies