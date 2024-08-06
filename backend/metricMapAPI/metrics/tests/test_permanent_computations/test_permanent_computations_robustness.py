import unittest
from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.utils import timezone
import pandas as pd
import numpy as np
import time
from datetime import timedelta

from metrics.models import Metric, HistoricalData, Forecast, Anomaly, Connection, Client, Domain, Project, MetricType, ValueType
from metrics.computations.computations_anomalies import AnomalyDetector
from metrics.computations.computations_forecaster import Forecaster
from metrics.computations.permanent_computations import PermanentComputations
from metrics.computations.computations_analyzer import Analyzer
from metrics.computations.computations_relationships import RelationshipAnalyzer
from metrics.computations.data_preparation import DataPreparation

import logging

logger = logging.getLogger(__name__)

class TestComputationsRobustness(TestCase):

    def setUp(self):
        print("Starting setUp")
        self.tenant = Client.objects.create(name="Test Tenant", schema_name="test_tenant")
        self.domain = Domain.objects.create(domain="test.localhost", tenant=self.tenant, is_primary=True)
        self.project = Project.objects.create(name="Test Project", tenant=self.tenant)
        self.metric1 = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="Test Metric 1",
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        self.metric2 = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="Test Metric 2",
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        
        self.dates = pd.date_range(start='2023-01-01', periods=1000)
        self.values = np.random.normal(100, 10, 1000)
        self.df = pd.DataFrame({'date': self.dates, 'value': self.values})
        
        for date, value in zip(self.dates, self.values):
            HistoricalData.objects.create(
                metric=self.metric1,
                date=date,
                value=value,
                tenant=self.tenant
            )
            HistoricalData.objects.create(
                metric=self.metric2,
                date=date,
                value=value * 1.1,
                tenant=self.tenant
            )

        self.params = {
            'window_size': 30,
            'seasonality_period': 7,
            'base_threshold': 3.0,
            'context_window': 5,
            'global_threshold': 4.0,
            'forecast_horizon': 7
        }

        self.pc = PermanentComputations([self.metric1.id, self.metric2.id], self.tenant)
        self.analyzer = Analyzer(self.metric1.id)
        self.relationship_analyzer = RelationshipAnalyzer(self.metric1.id)

        logger.info("Setup completed")

    @patch('metrics.computations.computations_anomalies.logger')
    def test_anomaly_detection_robustness(self, mock_logger):
        detector = AnomalyDetector(metric_id=self.metric1.id, prepared_data=self.df, dynamic_params=self.params)
        
        self.assertEqual(detector.window_size, self.params['window_size'])
        self.assertEqual(detector.seasonality_period, self.params['seasonality_period'])
        
        detector.df = pd.DataFrame()
        result = detector.detect_anomalies()
        
        self.assertTrue(mock_logger.warning.called)
        self.assertEqual(len(result), 0)

        detector.df = self.df
        result = detector.detect_anomalies()
        
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(all(col in result.columns for col in ['date', 'value', 'anomaly_score', 'type']))

    @patch('metrics.computations.computations_forecaster.logger')
    def test_forecast_computation_robustness(self, mock_logger):
        data_prep = DataPreparation(self.metric1.id)
        prepared_data = data_prep.prepare_data()
        forecaster = Forecaster(self.metric1.id, prepared_data, self.params, {})
        
        self.assertEqual(forecaster.params['forecast_horizon'], self.params['forecast_horizon'])
        
        forecaster.data = pd.DataFrame()
        result = forecaster.forecast()
        
        self.assertTrue(mock_logger.error.called)
        self.assertIsNone(result)

        forecaster.data = self.df
        result = forecaster.forecast()
        
        self.assertIsInstance(result, dict)
        self.assertTrue(all(isinstance(forecasts, list) for forecasts in result.values()))

    def test_computation_with_missing_data(self):
        # Introduce missing values
        df_with_missing = self.df.copy()
        df_with_missing.loc[10:15, 'value'] = np.nan

        data_prep = DataPreparation(self.metric1.id)
        prepared_data = data_prep.prepare_data()

        detector = AnomalyDetector(self.metric1.id, prepared_data, self.params, {})
        anomalies = detector.detect_anomalies()
        self.assertIsInstance(anomalies, dict)

        forecaster = Forecaster(self.metric1.id, prepared_data, self.params, {})
        forecast = forecaster.forecast()
        self.assertIsInstance(forecast, dict)

    def test_computation_with_extreme_values(self):
        # Introduce extreme values
        df_with_extremes = self.df.copy()
        df_with_extremes.loc[20, 'value'] = 1000000
        df_with_extremes.loc[30, 'value'] = -1000000

        data_prep = DataPreparation(self.metric1.id)
        prepared_data = data_prep.prepare_data()

        detector = AnomalyDetector(self.metric1.id, prepared_data, self.params, {})
        anomalies = detector.detect_anomalies()
        self.assertIsInstance(anomalies, dict)

        # Add extreme values to the historical data
        HistoricalData.objects.create(metric=self.metric1, date=timezone.now(), value=1000000, tenant=self.tenant)
        HistoricalData.objects.create(metric=self.metric1, date=timezone.now() - timedelta(days=1), value=-1000000, tenant=self.tenant)

        # Initialize Forecaster with prepared data
        forecaster = Forecaster(self.metric1.id, prepared_data, self.params, {})
        forecast = forecaster.forecast()
        self.assertIsInstance(forecast, dict)

    def test_permanent_computations_robustness(self):
        self.pc.run_all_computations()
        self.assertTrue(Forecast.objects.filter(metric=self.metric1).exists())
        self.assertTrue(Anomaly.objects.filter(metric=self.metric1).exists())
        
        to_delete = list(HistoricalData.objects.filter(metric=self.metric1, tenant=self.tenant)[::10])
        HistoricalData.objects.filter(id__in=[obj.id for obj in to_delete]).delete()
        self.pc.run_all_computations()
        self.assertTrue(Forecast.objects.filter(metric=self.metric1).exists())
        
        HistoricalData.objects.create(metric=self.metric1, tenant=self.tenant, date=timezone.now(), value=1000000)
        HistoricalData.objects.create(metric=self.metric1, tenant=self.tenant, date=timezone.now() + timezone.timedelta(days=1), value=-1000000)
        self.pc.run_all_computations()
        self.assertTrue(Anomaly.objects.filter(metric=self.metric1, anomaly_value__in=[1000000, -1000000]).exists())
        
        start_time = time.time()
        self.pc.run_all_computations()
        end_time = time.time()
        self.assertLess(end_time - start_time, 30)
        print(f"Permanent Computation time: {end_time - start_time} seconds")

    def test_analyzer_robustness(self):
        result = self.analyzer.analyze()
        self.assertIsNotNone(result)

        to_delete = list(HistoricalData.objects.filter(metric=self.metric1, tenant=self.tenant)[::10])
        HistoricalData.objects.filter(id__in=[obj.id for obj in to_delete]).delete()
        result = self.analyzer.analyze()
        self.assertIsNotNone(result)

        HistoricalData.objects.create(metric=self.metric1, tenant=self.tenant, date=timezone.now(), value=1000000)
        result = self.analyzer.analyze()
        self.assertIsNotNone(result)

        start_time = time.time()
        self.analyzer.analyze()
        end_time = time.time()
        self.assertLess(end_time - start_time, 30)
        print(f"Analyzer Computation time: {end_time - start_time} seconds")

    def test_relationships_robustness(self):
        connection = Connection.objects.create(
            from_metric=self.metric1,
            to_metric=self.metric2,
            tenant=self.tenant,
            strength=0.5
        )

        result = self.relationship_analyzer.analyze_relationships([self.metric2.id])
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertIn('pearson', result[0])
        self.assertIn('spearman', result[0])

        to_delete = list(HistoricalData.objects.filter(metric=self.metric1, tenant=self.tenant)[::10])
        HistoricalData.objects.filter(id__in=[obj.id for obj in to_delete]).delete()
        result = self.relationship_analyzer.analyze_relationships([self.metric2.id])
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)

        HistoricalData.objects.create(metric=self.metric1, date=timezone.now(), value=1000000, tenant=self.tenant)
        result = self.relationship_analyzer.analyze_relationships([self.metric2.id])
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)

        start_time = time.time()
        self.relationship_analyzer.analyze_relationships([self.metric2.id])
        end_time = time.time()
        self.assertLess(end_time - start_time, 30)
        print(f"Relationship Analyzer Computation time: {end_time - start_time} seconds")

        self.relationship_analyzer.analyze_connections()
        connection.refresh_from_db()
        self.assertNotEqual(connection.strength, 0.5)

        lagged_results = self.relationship_analyzer.detect_lagged_relationships([self.metric2.id])
        self.assertIsNotNone(lagged_results)
        self.assertEqual(len(lagged_results), 1)
        self.assertIn('lagged_correlations', lagged_results[0])

    def tearDown(self):
        HistoricalData.objects.filter(tenant=self.tenant).delete()
        Metric.objects.filter(tenant=self.tenant).delete()
        Project.objects.filter(tenant=self.tenant).delete()
        Domain.objects.filter(tenant=self.tenant).delete()
        self.tenant.delete()
        logger.info("Teardown completed")

if __name__ == '__main__':
    unittest.main()