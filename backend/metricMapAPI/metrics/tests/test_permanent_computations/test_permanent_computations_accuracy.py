import logging
import unittest
from django.test import TestCase
from django.utils import timezone
from django.db import IntegrityError, transaction
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
from scipy import stats
import time
from datetime import timedelta

from ...models import (
    Client, Domain, Project, Metric, HistoricalData, SeasonalityResult,
    Forecast, Anomaly, Trend, Correlation, MetricType, ValueType
)
from ...computations.permanent_computations import PermanentComputations
from ...computations.data_preparation import DataPreparation
from ...computations.feature_engineering import FeatureEngineering
from ...computations.computations_analyzer import Analyzer
from ...computations.computations_forecaster import Forecaster
from ...computations.computations_anomalies import AnomalyDetector
from ...computations.computations_relationships import RelationshipAnalyzer

logger = logging.getLogger(__name__)

class TestPermanentComputationsAccuracy(TestCase):
    def setUp(self):
        print("Starting setUp")
        # Create a test tenant
        self.tenant = Client.objects.create(
            name="Test Tenant",
            schema_name="test_tenant",
        )
        logger.info(f"Created test tenant: {self.tenant}")
        
        # Create a domain for the tenant
        self.domain = Domain.objects.create(
            domain="test.localhost",
            tenant=self.tenant,
            is_primary=True
        )
        logger.info(f"Created domain: {self.domain}")
        
        # Create a test project
        self.project = Project.objects.create(name="Test Project", tenant=self.tenant)
        logger.info(f"Created test project: {self.project}")
        
        # Create a test metric with the tenant and project
        self.metric = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="Test Metric",
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        logger.info(f"Created test metric: {self.metric}")
        
        self.related_metric = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="Related Test Metric",
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        logger.info(f"Created related test metric: {self.related_metric}")
        self.start_date = timezone.now().date() - timedelta(days=365)
        self.generate_historical_data()
        
        self.pc = PermanentComputations([self.metric.id], self.tenant)

    def generate_historical_data(self):
        dates = [self.start_date + timedelta(days=i) for i in range(365)]
        values = self.generate_benchmark_data()
        
        historical_data = [
            HistoricalData(
                tenant=self.tenant,
                metric=self.metric,
                date=date,
                value=value
            ) for date, value in zip(dates, values)
        ]
        HistoricalData.objects.bulk_create(historical_data)

    def generate_benchmark_data(self):
        trend = np.linspace(100, 200, 365)
        seasonality = 20 * np.sin(np.linspace(0, 2*np.pi, 365))
        noise = np.random.normal(0, 5, 365)
        
        # Add an obvious anomaly
        anomaly_index = np.random.randint(0, 365)
        anomaly = np.zeros(365)
        anomaly[anomaly_index] = 20  # A large spike
        
        return trend + seasonality + noise + anomaly

    def test_seasonality_accuracy(self):
        data_prep = DataPreparation(self.metric.id)
        prepared_data, metadata = data_prep.prepare_data()
        
        fe = FeatureEngineering(self.metric.id)
        dynamic_params = fe.compute_dynamic_parameters()
        engineered_features = fe.engineer_features()
        
        analyzer = Analyzer(self.metric.id, prepared_data, dynamic_params, engineered_features)
        analysis_results = analyzer.analyze()
        
        seasonality = SeasonalityResult.objects.filter(metric=self.metric, tenant=self.tenant).first()
        
        self.assertIsNotNone(seasonality)
        self.assertGreater(seasonality.strength, 0)
        self.assertLess(seasonality.strength, 1)
        self.assertIn(seasonality.period, [7, 30, 365])

    def test_forecast_accuracy(self):
        data_prep = DataPreparation(self.metric.id)
        prepared_data, metadata = data_prep.prepare_data()
        
        fe = FeatureEngineering(self.metric.id)
        dynamic_params = fe.compute_dynamic_parameters()
        engineered_features = fe.engineer_features()
        
        forecaster = Forecaster(self.metric.id, prepared_data, dynamic_params, engineered_features)
        forecast_results = forecaster.forecast()
        
        forecasts = Forecast.objects.filter(metric=self.metric, tenant=self.tenant, model_used='SARIMA')
        self.assertGreater(forecasts.count(), 0)

        future_values = self.generate_benchmark_data()[-dynamic_params['forecast_horizon']:]
        forecast_values = [f.forecast_value for f in forecasts]
        
        mape = np.mean(np.abs((future_values - forecast_values) / future_values)) * 100
        self.assertLess(mape, 20)

    def test_anomaly_detection_accuracy(self):
        fe = FeatureEngineering(self.metric.id)
        dynamic_params = fe.compute_dynamic_parameters()
        
        # Assert that we're using dynamic parameters
        self.assertEqual(fe._parameter_type, "dynamic", "Test data should trigger dynamic parameter computation")
        
        # Check if all expected parameters are present
        expected_params = ['seasonality_period', 'forecast_horizon', 'correlation_window', 'trend_window',
                           'anomaly_detection_window', 'base_threshold', 'window_size', 'context_window',
                           'global_threshold', 'imputation_method']
        for param in expected_params:
            self.assertIn(param, dynamic_params, f"Missing expected parameter: {param}")
        
        # Perform anomaly detection
        anomaly_detector = AnomalyDetector(self.metric.id)
        anomalies = anomaly_detector.detect_anomalies()
        
        # Check if anomalies were detected
        self.assertGreater(len(anomalies), 0, "No anomalies detected")
        
        # Check if the injected anomalies were detected
        detected_anomaly_dates = anomalies['date'].dt.dayofyear.tolist()
        for injected_anomaly in [31, 91, 181, 271]:  # day of year for injected anomalies
            self.assertIn(injected_anomaly, detected_anomaly_dates, f"Failed to detect injected anomaly on day {injected_anomaly}")
        
        # Check false positive rate
        false_positive_rate = (len(anomalies) - 4) / 365  # 4 is the number of injected anomalies
        self.assertLess(false_positive_rate, 0.05, f"False positive rate too high: {false_positive_rate:.2%}")

    def test_trend_accuracy(self):
        data_prep = DataPreparation(self.metric.id)
        prepared_data, metadata = data_prep.prepare_data()
        
        fe = FeatureEngineering(self.metric.id)
        dynamic_params = fe.compute_dynamic_parameters()
        engineered_features = fe.engineer_features()
        
        analyzer = Analyzer(self.metric.id, prepared_data, dynamic_params, engineered_features)
        analysis_results = analyzer.analyze()
        
        trend = Trend.objects.get(metric=self.metric, tenant=self.tenant)
        
        self.assertEqual(trend.trend_type, 'increasing')
        self.assertGreater(trend.slope, 0)

    def test_relationship_analysis_accuracy(self):
        related_metric, created = Metric.objects.get_or_create(
            name="Related Test Metric",
            project=self.project,
            tenant=self.tenant,
            defaults={
                'description': "A related test metric",
                'unit': "count",
                'data_type': "integer",
                'aggregation_type': "sum",
            }
        )
        
        correlated_values = self.generate_benchmark_data() + np.random.normal(0, 1, 365)
        dates = [self.start_date + timedelta(days=i) for i in range(365)]
        
        HistoricalData.objects.bulk_create([
            HistoricalData(
                tenant=self.tenant,
                metric=related_metric,
                date=date,
                value=value
            ) for date, value in zip(dates, correlated_values)
        ])
        
        data_prep = DataPreparation(self.metric.id)
        prepared_data, metadata = data_prep.prepare_data()
        
        fe = FeatureEngineering(self.metric.id)
        dynamic_params = fe.compute_dynamic_parameters()
        engineered_features = fe.engineer_features()
        
        relationship_analyzer = RelationshipAnalyzer(self.metric.id, prepared_data, dynamic_params, engineered_features)
        relationship_results = relationship_analyzer.analyze_relationships()
        
        correlation = Correlation.objects.filter(metric1=self.metric, metric2=related_metric, tenant=self.tenant).first()
        self.assertIsNotNone(correlation)
        
        df1 = pd.DataFrame({'value': self.generate_benchmark_data()}, index=dates)
        df2 = pd.DataFrame({'value': correlated_values}, index=dates)
        expected_pearson, _ = stats.pearsonr(df1['value'], df2['value'])
        self.assertAlmostEqual(correlation.pearson_correlation, expected_pearson, delta=0.1)

    def tearDown(self):
        try:
            with transaction.atomic():
                HistoricalData.objects.filter(tenant=self.tenant).delete()
        except Exception as e:
            print(f"Error in tearDown: {e}")
        Metric.objects.filter(tenant=self.tenant).delete()
        Project.objects.filter(tenant=self.tenant).delete()
        Domain.objects.filter(tenant=self.tenant).delete()
        self.tenant.delete()