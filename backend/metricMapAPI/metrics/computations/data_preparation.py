"""Module for performing permanent computations on metrics data."""

from typing import Dict, Tuple, Any
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.impute import SimpleImputer, KNNImputer
from django.core.exceptions import ObjectDoesNotExist
from utils import log_exceptions, validate_metadata, safe_divide
from config import config
from ..models import ( Metric, DataQualityScore, HistoricalData )
from django.db import transaction
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
import logging

logger = logging.getLogger(__name__)

class DataPreparation:
    def __init__(self, metric_id: int):
        """Initialize the DataPreparation object.

        Args:
            metric_id (int): The ID of the metric to perform computations on.
        """
        self.metric_id = metric_id
        self.metric = None
        self.tenant = None
        self.project = None
        self._load_metric()  # This will set self.metric, self.tenant, and self.project
        self.raw_df = self._load_historical_data()
        self.cleaned_df = None
        self.metadata = self._initialize_metadata()

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

    def _initialize_metadata(self) -> Dict[str, Any]:
        return {
            'metric_id': self.metric_id,
            'tenant_id': self.tenant.id,
            'project_id': self.project.id,
            'metric_name': self.metric.name,
            'value_type': self.metric.value_type
        }

    def _validate_data(self) -> None:
        if not isinstance(self.raw_df.index, pd.DatetimeIndex):
            raise ValueError("DataFrame index must be a DatetimeIndex")
        if 'value' not in self.raw_df.columns:
            raise ValueError("DataFrame must have a 'value' column")
        
        # Check for data integrity
        if self.raw_df.empty:
            logger.warning(f"No data available for metric {self.metric_id}")
            raise ValueError("No data available for processing")
        
        # Verify referential integrity
        unique_tenants = self.raw_df['tenant_id'].nunique()
        unique_projects = self.raw_df['project_id'].nunique()
        if unique_tenants != 1 or unique_projects != 1:
            logger.error(f"Data integrity issue: multiple tenants or projects found for metric {self.metric_id}")
            raise ValueError("Data integrity violation: multiple tenants or projects found")

    @log_exceptions
    def _load_historical_data(self):
        try:
            historical_data = HistoricalData.objects.filter(
                metric=self.metric,
                tenant=self.tenant,
                metric__project=self.project
            ).values('date', 'value', 'tenant_id', 'project_id')
            df = pd.DataFrame(historical_data)
            if df.empty:
                logger.warning(f"No historical data found for metric {self.metric_id}")
                return pd.DataFrame()
            df['date'] = pd.to_datetime(df['date'])
            df.set_index('date', inplace=True)
            df.sort_index(inplace=True)
            return df
        except Exception as e:
            logger.error(f"Error loading historical data for metric {self.metric_id}: {str(e)}")
            return pd.DataFrame()

    def _normalize_data(self):
        if self.metric.value_type == 'percentage':
            self.raw_df['value'] = self.raw_df['value'].astype(float) / 100
        elif self.metric.value_type == 'currency':
            self.raw_df['value'] = self.raw_df['value'].astype(float)
        # Add more normalization logic as needed

    @log_exceptions
    def handle_missing_values(self) -> None:
        missing_pct = self.raw_df['value'].isnull().sum() / len(self.raw_df) * 100
        logger.info(f"Found {missing_pct:.2f}% missing values in the data")

        if missing_pct < 5:
            imputation_method = 'mean'
            imputer = SimpleImputer(strategy='mean')
        elif missing_pct < 15:
            imputation_method = 'interpolate'
            self.raw_df['value'] = self.raw_df['value'].interpolate(method='time')
        else:
            imputation_method = 'knn'
            imputer = KNNImputer(n_neighbors=5)

        if imputation_method in ['mean', 'knn']:
            self.raw_df['value'] = imputer.fit_transform(self.raw_df[['value']])

        logger.info(f"Handled missing values using {imputation_method} method")

    @log_exceptions
    def _update_database_with_imputed_values(self) -> None:
        try:
            with transaction.atomic():
                for index, row in self.raw_df.iterrows():
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
        Q1 = self.raw_df['value'].quantile(0.25)
        Q3 = self.raw_df['value'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        self.raw_df['value'] = np.clip(self.raw_df['value'], lower_bound, upper_bound)
        logger.info("Handled outliers using IQR method")

    def handle_extreme_values(self) -> None:
        lower_bound = self.raw_df['value'].quantile(0.01)
        upper_bound = self.raw_df['value'].quantile(0.99)
        self.raw_df['value'] = np.clip(self.raw_df['value'], lower_bound, upper_bound)
        logger.info("Handled extreme values by capping at 1st and 99th percentiles")

    def calculate_data_quality_score(self) -> float:
        completeness = 1 - (self.raw_df['value'].isnull().sum() / len(self.raw_df))
        accuracy = 1 - (len(self.cleaned_df) / len(self.raw_df))
        consistency = self._calculate_consistency_score()
        timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days))
        
        overall_score = np.mean([completeness, accuracy, consistency, timeliness]) * 100
        
        self.data_quality_score, _ = DataQualityScore.objects.update_or_create(
            metric=self.metric,
            tenant=self.metric.tenant,
            project=self.metric.project,
            defaults={
                'data_entry': f"Metric_{self.metric_id}",
                'completeness_score': completeness * 100,
                'accuracy_score': accuracy * 100,
                'consistency_score': consistency * 100,
                'timeliness_score': timeliness * 100,
                'overall_score': overall_score
            }
        )
        logger.info(f"Calculated data quality score for metric {self.metric_id}: {overall_score:.2f}%")
        return overall_score

    def _calculate_consistency_score(self) -> float:
        trend_consistency = self._calculate_trend_consistency()
        volatility_score = self._calculate_volatility_score()
        seasonality_consistency = self._calculate_seasonality_consistency()
        
        consistency_score = (0.4 * trend_consistency + 
                             0.4 * volatility_score + 
                             0.2 * seasonality_consistency)
        
        return consistency_score

    def _calculate_trend_consistency(self) -> float:
        x = np.arange(len(self.cleaned_df)).reshape(-1, 1)
        y = self.cleaned_df['value'].values
        _, _, r_value, _, _ = stats.linregress(x.flatten(), y)
        return r_value ** 2

    def _calculate_volatility_score(self) -> float:
        cv = self.cleaned_df['value'].std() / self.cleaned_df['value'].mean()
        return 1 / (1 + cv)

    def _calculate_seasonality_consistency(self) -> float:
        if len(self.cleaned_df) < 2:
            return 1.0
        
        try:
            result = seasonal_decompose(self.cleaned_df['value'], model='additive', period=self._detect_seasonality())
            seasonality_strength = 1 - np.var(result.resid) / np.var(result.observed - result.trend)
            return max(0, min(seasonality_strength, 1))
        except Exception as e:
            logger.warning(f"Error in seasonality calculation for metric {self.metric_id}: {str(e)}")
            return 1.0

    def _detect_seasonality(self) -> int:
        if len(self.cleaned_df) < 4:
            return 1
        
        acf = pd.Series(self.cleaned_df['value']).autocorr(lag=1000)
        peaks = np.where((acf[1:] > acf[:-1]) & (acf[1:] > acf[2:]))[0] + 1
        
        if len(peaks) > 0:
            return int(peaks[0])
        
        potential_periods = [7, 12, 52, 365]
        max_acf = 0
        best_period = 1
        
        for period in potential_periods:
            if len(self.cleaned_df) > 2 * period:
                acf = self.cleaned_df['value'].autocorr(lag=period)
                if acf > max_acf:
                    max_acf = acf
                    best_period = period
        return best_period

    def check_stationarity(self) -> bool:
        result = adfuller(self.cleaned_df['value'].dropna())
        return result[1] <= 0.05  # p-value <= 0.05 indicates stationarity

    @log_exceptions
    def prepare_data(self) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Prepare data for computations."""
        if self.raw_df.empty:
            logger.error(f"No data available for metric {self.metric_id}")
            raise ValueError("No historical data available for this metric")
        
        self._validate_data()
        self._normalize_data()
        self.handle_missing_values()
        self._update_database_with_imputed_values()
        self.handle_outliers()
        self.handle_extreme_values()
        
        self.cleaned_df = self.raw_df.copy()
        
        data_quality_score = self.calculate_data_quality_score()
        if data_quality_score < 30:
            logger.warning(f"Data quality score ({data_quality_score:.2f}%) is below threshold. Stopping processing.")
            raise ValueError("Data quality is insufficient for further processing")

        is_stationary = self.check_stationarity()
        self.metadata['is_stationary'] = is_stationary
        
        if not validate_metadata(self.metadata, ['metric_id', 'tenant_id', 'project_id', 'metric_name', 'is_stationary']):
            logger.warning(f"Incomplete metadata for metric {self.metric_id}")
        
        return self.cleaned_df, self.metadata

    def get_cleaned_data(self):
        if self.cleaned_df is None:
            self.cleaned_df, _ = self.prepare_data()
        return self.cleaned_df

def get_prepared_data(metric_id: int):
    data_prep = DataPreparation(metric_id)
    cleaned_df, metadata = data_prep.prepare_data()
    return cleaned_df, metadata