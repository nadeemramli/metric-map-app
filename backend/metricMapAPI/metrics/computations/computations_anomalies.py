# anomaly_detection.py

import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import acf
from scipy.signal import find_peaks
import logging

logger = logging.getLogger(__name__)

class SeasonalityDetector:
    @staticmethod
    def detect_seasonality_period(data: pd.Series) -> int:
        try:
            autocorr = acf(data, nlags=len(data) // 2)
            peaks, _ = find_peaks(autocorr, height=0.1, distance=1)
            if len(peaks) > 1:
                peak_diffs = np.diff(peaks)
                seasonality = np.bincount(peak_diffs).argmax()
                if 2 <= seasonality <= 365:
                    return int(seasonality)
            return None
        except Exception as e:
            logger.warning(f"Error in detecting seasonality: {str(e)}. Defaulting to None.")
            return None
 
class ParameterDeterminer:
    @staticmethod
    def determine_window_size(data: pd.Series, seasonality_period: int = None) -> int:
        try:
            suggested_window = max(7, min(90, len(data) // 10))
            if seasonality_period:
                suggested_window = max(suggested_window, seasonality_period)
            return suggested_window
        except Exception as e:
            logger.warning(f"Error in determining window size: {str(e)}. Defaulting to 30.")
            return 30

    @staticmethod
    def determine_base_threshold(data: pd.Series) -> float:
        try:
            q1 = data.quantile(0.25)
            q3 = data.quantile(0.75)
            iqr = q3 - q1
            suggested_threshold = max(2.0, min(4.0, 1.5 * iqr))
            return suggested_threshold
        except Exception as e:
            logger.warning(f"Error in determining base threshold: {str(e)}. Defaulting to 2.5.")
            return 2.5

    @staticmethod
    def determine_context_window(window_size: int) -> int:
        try:
            suggested_context_window = max(3, min(15, window_size // 5))
            return suggested_context_window
        except Exception as e:
            logger.warning(f"Error in determining context window: {str(e)}. Defaulting to 5.")
            return 5

class AnomalyDetector:
    def __init__(self, df: pd.DataFrame, metadata: dict):
        self.df = df
        self.seasonality_period = None
        self.window_size = None
        self.base_threshold = None
        self.context_window = None
        self.metadata = metadata


    def detect_anomalies(self) -> pd.DataFrame:
        try:
            if len(self.df) < 14:
                logger.warning("Not enough data for anomaly detection")
                return pd.DataFrame()

            self.seasonality_period = SeasonalityDetector.detect_seasonality_period(self.df['value'])
            self.window_size = ParameterDeterminer.determine_window_size(self.df['value'], self.seasonality_period)
            self.base_threshold = ParameterDeterminer.determine_base_threshold(self.df['value'])
            self.context_window = ParameterDeterminer.determine_context_window(self.window_size)

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

        except Exception as e:
            logger.error(f"Error detecting anomalies for metric {self.metric.id}: {str(e)}")
            raise
            return anomalies

        except Exception as e:
            logger.error(f"Error in anomaly detection: {str(e)}")
            return pd.DataFrame()