"""Module for performing permanent computations on metrics data."""

from typing import Dict, Tuple, Any
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.impute import SimpleImputer, KNNImputer
from django.core.exceptions import ObjectDoesNotExist
from .utils import log_exceptions, validate_metadata, safe_divide
from .config import Config
from django.db import transaction
from statsmodels.tsa.stattools import adfuller
import logging
from django.apps import apps

logger = logging.getLogger(__name__)

class DataPreparation:
    def __init__(self, metric_or_id, client):
        """Initialize the DataPreparation object.

        Args:
            metric_or_id (int or Metric): The ID or the Metric object of the metric to perform computations on.
        """
        print(f"Initializing DataPreparation for metric_id: {metric_or_id}")
        Metric = apps.get_model('metrics', 'Metric')
        if isinstance(metric_or_id, Metric):
            self.metric_id = metric_or_id.id
            self.metric = metric_or_id
        else:
            self.metric_id = metric_or_id
            self.metric = None
        self.client = client
        self._load_metric()  # This will set self.metric
        self.raw_df = None
        self.cleaned_df = None
        self.metadata = self._initialize_metadata()
        print("Finished initializing DataPreparation")


    @log_exceptions
    def _load_metric(self) -> None:
        Metric = apps.get_model('metrics', 'Metric')
        try:
            self.metric = Metric.objects.select_related('tenant').get(id=self.metric_id)
            logger.info(f"Loaded metric {self.metric_id} for client {self.client.id}")
        except ObjectDoesNotExist:
            logger.error(f"Metric with id {self.metric_id} does not exist")
            raise ValueError(f"Invalid metric_id: {self.metric_id}")

    def _initialize_metadata(self) -> Dict[str, Any]:
        return {
            'metric_id': self.metric_id,
            'client_id': self.client.id,
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
        unique_clients = self.raw_df['client_id'].nunique()
        if unique_clients != 1:
            logger.error(f"Data integrity issue: multiple clients found for metric {self.metric_id}")
            raise ValueError("Data integrity violation: multiple clients found")

    @log_exceptions
    def _load_historical_data(self) -> pd.DataFrame:
        HistoricalData = apps.get_model('metrics', 'HistoricalData')
        try:
            logger.info(f"Fetching historical data for metric {self.metric_id}")
            historical_data = HistoricalData.objects.filter(metric=self.metric).order_by('date')
            
            logger.info(f"Query: {historical_data.query}")
            logger.info(f"SQL: {historical_data.query.__str__()}")
            
            if not historical_data.exists():
                logger.warning(f"No historical data found for metric {self.metric_id}")
                return pd.DataFrame(columns=['date', 'value', 'client_id'])
            
            logger.info(f"Found {historical_data.count()} historical data points for metric {self.metric_id}")
            
            df = pd.DataFrame(list(historical_data.values('date', 'value', 'client_id')))
            df['date'] = pd.to_datetime(df['date'])
            df.set_index('date', inplace=True)
            
            logger.info(f"DataFrame shape after loading: {df.shape}")
            logger.info(f"DataFrame columns: {df.columns}")
            logger.info(f"DataFrame head: \n{df.head()}")
            
            return df
        except Exception as e:
            logger.error(f"Error loading historical data for metric {self.metric_id}: {str(e)}")
            return pd.DataFrame(columns=['date', 'value', 'client_id'])

    def _normalize_data(self):
        if self.metric.value_type == 'percentage':
            self.raw_df['value'] = self.raw_df['value'].astype(float) / 100
        elif self.metric.value_type == 'currency':
            self.raw_df['value'] = self.raw_df['value'].astype(float)
        # Add more normalization logic as needed

    @log_exceptions
    def handle_missing_values(self) -> None:
        if self.raw_df is None or self.raw_df.empty:
            logger.warning("No data available to handle missing values.")
            return

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

        # Add this line to store the imputation method in metadata
        self.metadata['imputation_method'] = imputation_method

        logger.info(f"Handled missing values using {imputation_method} method")

    @log_exceptions
    def _update_database_with_imputed_values(self) -> None:
        HistoricalData = apps.get_model('metrics', 'HistoricalData')
        try:
            with transaction.atomic():
                for index, row in self.raw_df.iterrows():
                    HistoricalData.objects.update_or_create(
                        metric=self.metric,
                        client=self.client,
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
        logger.info(f"Raw DataFrame shape: {self.raw_df.shape if self.raw_df is not None else 'None'}")
        logger.info(f"Raw DataFrame head: {self.raw_df.head() if self.raw_df is not None else 'None'}")
        if self.raw_df is None or self.raw_df.empty:
            logger.warning("No data available to calculate data quality score.")
            return 0.0

        completeness = 1 - (self.raw_df['value'].isnull().sum() / len(self.raw_df))
        accuracy = 1 - (len(self.cleaned_df) / len(self.raw_df)) if len(self.raw_df) > 0 else 0
        consistency = self._calculate_consistency_score()
        timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
        
        logger.info(f"Completeness: {completeness}, Accuracy: {accuracy}, Consistency: {consistency}, Timeliness: {timeliness}")
        
        scores = [completeness, accuracy, consistency, timeliness]
        overall_score = np.nanmean([score for score in scores if not np.isnan(score)]) * 100
        
        logger.info(f"Overall data quality score: {overall_score}")

        DataQualityScore = apps.get_model('metrics', 'DataQualityScore')
        self.data_quality_score, _ = DataQualityScore.objects.update_or_create(
            metric=self.metric,
            client=self.client,
            tenant=self.metric.tenant,  # Add this line
            defaults={
                'data_entry': f"Metric_{self.metric_id}",
                'completeness_score': completeness * 100,
                'accuracy_score': accuracy * 100,
                'consistency_score': consistency * 100,
                'timeliness_score': timeliness * 100,
                'overall_score': overall_score
            }
        )
        
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
            # Simple seasonality strength estimation, comprehensive seasonality at feature_engineering
            values = self.cleaned_df['value'].values
            seasonal_diff = pd.Series(values).diff(12).dropna()  # Assume annual seasonality for simplicity
            trend_diff = pd.Series(values).diff().dropna()
            
            if len(seasonal_diff) > 0 and len(trend_diff) > 0:
                seasonality_strength = 1 - np.var(seasonal_diff) / np.var(trend_diff)
                return max(0, min(seasonality_strength, 1))
            else:
                return 1.0
        except Exception as e:
            logger.warning(f"Error in simple seasonality calculation for metric {self.metric_id}: {str(e)}")
            return 1.0

    def check_stationarity(self) -> bool:
        result = adfuller(self.cleaned_df['value'].dropna())
        return result[1] <= 0.05  # p-value <= 0.05 indicates stationarity

    @log_exceptions
    def prepare_data(self) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Prepare data for computations."""
        print("Starting prepare_data")
        self.raw_df = self._load_historical_data()
        logger.info(f"Raw DataFrame shape after loading: {self.raw_df.shape}")
        logger.info(f"Raw DataFrame head after loading: {self.raw_df.head()}")
        
        if self.raw_df.empty or len(self.raw_df) == 0:
            logger.error(f"No data available for metric {self.metric_id}")
            raise ValueError("No historical data available for this metric")
        
        self._validate_data()
        self._normalize_data()
        self.handle_missing_values()
        self._update_database_with_imputed_values()
        self.handle_outliers()
        self.handle_extreme_values()
        
        self.cleaned_df = self.raw_df.copy()
        logger.info(f"Cleaned DataFrame shape: {self.cleaned_df.shape}")
        logger.info(f"Cleaned DataFrame head: {self.cleaned_df.head()}")
        
        data_quality_score = self.calculate_data_quality_score()
        logger.info(f"Data quality score: {data_quality_score}")
        
        if data_quality_score < Config.MIN_DATA_QUALITY_SCORE:
            logger.warning(f"Data quality score ({data_quality_score:.2f}%) is below threshold ({Config.MIN_DATA_QUALITY_SCORE}%). Stopping processing.")
            raise ValueError(f"Data quality is insufficient for further processing. Score: {data_quality_score:.2f}%, Threshold: {Config.MIN_DATA_QUALITY_SCORE}%")

        is_stationary = self.check_stationarity()
        self.metadata['is_stationary'] = is_stationary
        self.metadata['data_quality_score'] = data_quality_score
        self.metadata['outliers_handled'] = True
        
        # Compute and add profile to metadata
        self.metadata['profile'] = self.compute_profile()

        if not validate_metadata(self.metadata, ['metric_id', 'client_id', 'metric_name', 'is_stationary', 'data_quality_score']):
            logger.warning(f"Incomplete metadata for metric {self.metric_id}")
        
        logger.info(f"Final metadata: {self.metadata}")
        print("Finished prepare_data")
        
        if self.cleaned_df.empty:
            logger.error("Cleaned DataFrame is empty after processing")
            raise ValueError("Cleaned DataFrame is empty after processing")
        
        return self.cleaned_df, self.metadata

    def compute_profile(self):
        return {
            'mean': self.cleaned_df['value'].mean(),
            'median': self.cleaned_df['value'].median(),
            'std': self.cleaned_df['value'].std(),
            'min': self.cleaned_df['value'].min(),
            'max': self.cleaned_df['value'].max(),
            'skewness': self.cleaned_df['value'].skew(),
            'kurtosis': self.cleaned_df['value'].kurtosis(),
            'missing_percentage': (self.raw_df['value'].isnull().sum() / len(self.raw_df)) * 100
        }

    def get_cleaned_data(self):
        if self.cleaned_df is None:
            self.cleaned_df, _ = self.prepare_data()
        return self.cleaned_df

def get_prepared_data(metric_id: int, client):
    data_prep = DataPreparation(metric_id, client)
    cleaned_df, metadata = data_prep.prepare_data()
    return cleaned_df, metadata

"""
DataPreparation class for cleaning and preparing metric data for analysis.

This class handles the initial processing of raw metric data, including:
- Loading historical data
- Handling missing values
- Detecting and handling outliers
- Normalizing data
- Calculating data quality scores

Data Flow:
1. Load historical data from the database
2. Validate and normalize the data
3. Handle missing values through imputation
4. Detect and handle outliers
5. Handle extreme values
6. Calculate data quality score
7. Check for stationarity
8. Compute data profile

Output Format:
A tuple containing:
1. A pandas DataFrame with cleaned data
2. A dictionary containing metadata about the data preparation process

Output Example:
(
    pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'value': [100.0, 101.5, 99.8]
    }),
    {
        'metric_id': 1,
        'client_id': 1,
        'metric_name': 'Test Metric',
        'value_type': 'COUNT',
        'imputation_method': 'mean',
        'is_stationary': False,
        'data_quality_score': 85.5,
        'outliers_handled': True,
        'profile': {
            'mean': 100.43,
            'median': 100.0,
            'std': 0.85,
            'min': 99.8,
            'max': 101.5,
            'skewness': 0.23,
            'kurtosis': -0.5
        }
    }
)
"""