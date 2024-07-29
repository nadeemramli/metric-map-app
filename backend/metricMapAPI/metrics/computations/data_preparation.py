"""Module for performing permanent computations on metrics data."""

from typing import Dict, Tuple, Any
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.tsa.seasonal import seasonal_decompose, STL
from sklearn.impute import SimpleImputer
from django.core.exceptions import ObjectDoesNotExist
from utils import log_exceptions, validate_metadata, safe_divide
from config import config
from ..models import ( Metric, DataQualityScore, HistoricalData )
from django.db import transaction
import logging
from statsmodels.tsa.stattools import adfuller

logger = logging.getLogger(__name__)

class DataPreparation:
    def __init__(self, metric_id: int):
        """Initialize the PermanentComputations object.

        Args:
            metric_id (int): The ID of the metric to perform computations on.
        """
        self.metric_id = metric_id
        self.metric = None
        self.tenant = None
        self.project = None
        self._load_metric()  # This will set self.metric, self.tenant, and self.project
        self.raw_df = self._load_historical_data()
        self.df = None
        self.params = self._compute_parameters()
        self.data_quality_score = None
        self.outliers = None

    @log_exceptions
    def _load_metric(self) -> None:
        try:
            self.metric = Metric.objects.select_related('tenant', 'project').get(id=self.metric_id)
            self.tenant = self.metric.tenant
            self.project = self.metric.project
            logger.info(f"Loaded metric {self.metric_id} for tenant {self.tenant.id} and project {self.project.id}")
        except ObjectDoesNotExist:
            logger.error(f"Metric with id {self.metric_id} does not exist")
            raise ValueError(f"Invalid metric_id: {self.metric_id}")

    def _validate_data(self) -> None:
        if not isinstance(self.raw_df.index, pd.DatetimeIndex):
            raise ValueError("DataFrame index must be a DatetimeIndex")
        if 'value' not in self.raw_df.columns:
            raise ValueError("DataFrame must have a 'value' column")
    
    @log_exceptions
    def _load_historical_data(self):
        try:
            historical_data = HistoricalData.objects.filter(
                metric=self.metric,
                tenant=self.tenant,
                metric__project=self.project
            ).values('date', 'value')
            df = pd.DataFrame(historical_data)
            if df.empty:
                logger.warning(f"No historical data found for metric {self.metric_id}")
                return pd.DataFrame()
            df['date'] = pd.to_datetime(df['date'])
            df.set_index('date', inplace=True)
            df.sort_index(inplace=True)
            return df
        except ObjectDoesNotExist:
            logger.error(f"Metric with id {self.metric_id} does not exist")
            raise ValueError(f"Invalid metric_id: {self.metric_id}")
        except Exception as e:
            logger.error(f"Error loading historical data for metric {self.metric_id}: {str(e)}")
            return pd.DataFrame()
    
    def _compute_parameters(self) -> Dict[str, Any]:
        return {
            'imputation_method': 'mean' if self.raw_df['value'].isnull().sum() / len(self.raw_df) < 0.1 else 'interpolate',
            'outlier_method': 'iqr' if self.raw_df['value'].skew() < 1 else 'zscore',
            'outlier_threshold': 1.5 if self.raw_df['value'].kurtosis() < 3 else 3
        }
    
    @log_exceptions
    def prepare_data(self) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Prepare data for computations."""
        if self.raw_df.empty:
            logger.error(f"No data available for metric {self.metric_id}")
            raise ValueError("No historical data available for this metric")
        
        self.handle_missing_values()
        self.handle_outliers()
        self.calculate_data_quality_score()
        
        metadata = {
            'metric_id': self.metric_id,
            'tenant_id': self.metric.tenant.id,
            'project_id': self.metric.project.id,
            'metric_name': self.metric.name,
            'data_quality_score': self.data_quality_score.overall_score if self.data_quality_score else None
        }
        
        if not validate_metadata(metadata, ['metric_id', 'tenant_id', 'project_id', 'metric_name']):
            logger.warning(f"Incomplete metadata for metric {self.metric_id}")
        
        return self.df, metadata

    def check_missing_values(self) -> None:
        missing_values = self.raw_df['value'].isnull().sum()
        if missing_values > 0:
            logger.warning(f"Found {missing_values} missing values in the data")

    @log_exceptions
    def handle_missing_values(self) -> None:
        if self.params['imputation_method'] == 'mean':
            imputer = SimpleImputer(strategy='mean')
            imputed_values = imputer.fit_transform(self.raw_df)
            self.df = pd.DataFrame(imputed_values, columns=self.raw_df.columns, index=self.raw_df.index)
        else:
            self.df = self.raw_df.interpolate()
        
        # Update the database with imputed values
        self._update_database_with_imputed_values()
        
        logger.info(f"Handled missing values for metric {self.metric_id}")
    
    @log_exceptions
    def _update_database_with_imputed_values(self) -> None:
        try:
            with transaction.atomic():
                for index, row in self.df.iterrows():
                    HistoricalData.objects.update_or_create(
                        metric=self.metric,
                        tenant=self.tenant,
                        date=index.date(),
                        defaults={'value': row['value']}
                    )
            logger.info(f"Updated database with imputed values for metric {self.metric_id}")
        except Exception as e:
            logger.error(f"Failed to update database with imputed values for metric {self.metric_id}: {str(e)}")
            raise
    
    def handle_outliers(self) -> None:
        """Detect outliers in the data.

        Args:
            method (str): Method to use for outlier detection. Either 'iqr' or 'zscore'.

        Returns:
            pd.DataFrame: DataFrame containing outliers.
        """
        try:
            if self.params['outlier_method'] == 'iqr':
                q1 = self.raw_df['value'].quantile(0.25)
                q3 = self.raw_df['value'].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - self.params['outlier_threshold'] * iqr
                upper_bound = q3 + self.params['outlier_threshold'] * iqr
                self.df = self.df[(self.df['value'] >= lower_bound) & (self.df['value'] <= upper_bound)]
            elif self.params['outlier_method'] == 'zscore':
                z_scores = np.abs((self.df['value'] - self.df['value'].mean()) / self.df['value'].std())
                self.df = self.df[z_scores < self.params['outlier_threshold']]
            else:
                raise ValueError("Method must be either 'iqr' or 'zscore'")
            
            logger.info(f"Detected {len(self.df)} outliers for metric {self.metric_id}")
            return self.df
        except Exception as e:
            logger.error(f"Error detecting outliers for metric {self.metric_id}: {str(e)}")
            raise

    def calculate_data_quality_score(self) -> None:
        try:
            completeness = 1 - (self.raw_df['value'].isnull().sum() / len(self.raw_df))
            accuracy = 1 - (len(self.df) / len(self.raw_df))
            consistency = self._calculate_consistency_score()
            timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.df.index.max()).days))
            
            overall_score = np.mean([completeness, accuracy, consistency, timeliness])
            
            self.data_quality_score, _ = DataQualityScore.objects.update_or_create(
                metric=self.metric,
                tenant=self.metric.tenant,
                project=self.metric.project,
                defaults={
                    'data_entry': f"Metric_{self.metric_id}",
                    'completeness_score': completeness,
                    'accuracy_score': accuracy,
                    'consistency_score': consistency,
                    'timeliness_score': timeliness,
                    'overall_score': overall_score
                }
            )
            logger.info(f"Calculated data quality score for metric {self.metric_id}")
        except Exception as e:
            logger.error(f"Error calculating data quality score for metric {self.metric_id}: {str(e)}")
            raise
    
    def _calculate_consistency_score(self) -> float:
        trend_consistency = self._calculate_trend_consistency()
        volatility_score = self._calculate_volatility_score()
        seasonality_consistency = self._calculate_seasonality_consistency()
        
        # Combine the scores, giving more weight to trend consistency and volatility
        consistency_score = (0.4 * trend_consistency + 
                             0.4 * volatility_score + 
                             0.2 * seasonality_consistency)
        
        return consistency_score

    def _calculate_trend_consistency(self) -> float:
        # Use linear regression to check how well the data follows a consistent trend
        x = np.arange(len(self.df)).reshape(-1, 1)
        y = self.df['value'].values
        _, _, r_value, _, _ = stats.linregress(x.flatten(), y)
        return r_value ** 2  # R-squared value as a measure of trend consistency

    def _calculate_volatility_score(self) -> float:
        # Calculate the coefficient of variation (lower is better)
        cv = self.df['value'].std() / self.df['value'].mean()
        # Convert to a score where higher is better
        return 1 / (1 + cv)

    def _calculate_seasonality_consistency(self) -> float:
        if len(self.df) < 2:  # Not enough data for seasonality analysis
            return 1.0
        
        try:
            # Try to decompose the time series
            result = seasonal_decompose(self.df['value'], model='additive', period=self._detect_seasonality())
            # Calculate the strength of seasonality
            seasonality_strength = 1 - np.var(result.resid) / np.var(result.observed - result.trend)
            return max(0, min(seasonality_strength, 1))  # Ensure the score is between 0 and 1
        except Exception as e:
            logger.warning(f"Error in seasonality calculation for metric {self.metric_id}: {str(e)}")
            return 1.0  # Default to 1.0 if seasonality can't be calculated

    def _detect_seasonality(self) -> int:
        # Simple seasonality detection using autocorrelation
        if len(self.df) < 4:  # Not enough data for autocorrelation
            return 1
        
        acf = pd.Series(self.df['value']).autocorr(lag=1000)
        peaks = np.where((acf[1:] > acf[:-1]) & (acf[1:] > acf[2:]))[0] + 1
        
        if len(peaks) > 0:
            return int(peaks[0])
        
        potential_periods = [7, 12, 52, 365]  # weekly, monthly, yearly for daily data
        max_acf = 0
        best_period = 1
        
        for period in potential_periods:
            if len(self.df) > 2 * period:
                acf = self.df['value'].autocorr(lag=period)
                if acf > max_acf:
                    max_acf = acf
                    best_period = period
        return best_period

    def decompose_time_series(self) -> Dict[str, pd.Series]:
        stl = STL(self.df['value'], period=self._detect_seasonality())
        result = stl.fit()
        return {
            'trend': result.trend,
            'seasonal': result.seasonal,
            'residual': result.resid
        }

    def get_data_profile(self) -> Dict[str, float]:
        profile = super().get_data_profile()
        profile.update({
            "count": len(self.df),
            "mean": self.df['value'].mean(),
            "median": self.df['value'].median(),
            "std": self.df['value'].std(),
            "min": self.df['value'].min(),
            "max": self.df['value'].max(),
            "skew": self.df['value'].skew(),
            "kurtosis": self.df['value'].kurtosis(),
            "q1": self.df['value'].quantile(0.25),
            "q3": self.df['value'].quantile(0.75),
            "iqr": self.df['value'].quantile(0.75) - self.df['value'].quantile(0.25),
            "autocorrelation": self.df['value'].autocorr(),
            "is_stationary": self._check_stationarity()
        })
        return profile
    
    def _check_stationarity(self) -> bool:
        result = adfuller(self.df['value'].dropna())
        return result[1] <= 0.05  # p-value <= 0.05 indicates stationarity