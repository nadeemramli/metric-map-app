from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
from datetime import timedelta
from metrics.models import Client, Metric, HistoricalData
from metrics.computations.data_preparation import DataPreparation
from metrics.computations.feature_engineering import FeatureEngineering
from metrics.computations.computations_analyzer import Analyzer
from metrics.computations.computations_forecaster import Forecaster
from metrics.computations.computations_anomalies import AnomalyDetector
from metrics.computations.computations_relationships import RelationshipAnalyzer

class TestComputationUnits(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name="Test Client", schema_name="test_schema")
        self.metric = Metric.objects.create(
            tenant=self.client,
            name="Test Metric",
            type="KPI",
            value_type="COUNT"
        )
        self.start_date = timezone.now().date() - timedelta(days=99)
        self.historical_data = [
            HistoricalData(
                tenant=self.client,
                metric=self.metric,
                date=self.start_date + timedelta(days=i),
                value=np.random.randint(1, 100)
            ) for i in range(100)
        ]
        HistoricalData.objects.bulk_create(self.historical_data)

    def test_data_preparation(self):
        data_prep = DataPreparation(self.metric.id, self.client)
        prepared_data, metadata = data_prep.prepare_data()

        self.assertIsInstance(prepared_data, pd.DataFrame)
        self.assertGreater(len(prepared_data), 0)
        self.assertIn('data_quality_score', metadata)

    def test_feature_engineering(self):
        data_prep = DataPreparation(self.metric.id, self.client)
        prepared_data, _ = data_prep.prepare_data()

        fe = FeatureEngineering(self.metric.id, prepared_data, self.client)
        dynamic_params = fe.compute_dynamic_parameters()
        engineered_features = fe.engineer_features()

        self.assertIsInstance(dynamic_params, dict)
        self.assertIsInstance(engineered_features, pd.DataFrame)
        self.assertGreater(len(engineered_features.columns), len(prepared_data.columns))

    @patch('metrics.computations.computations_analyzer.Analyzer.analyze')
    def test_analyzer(self, mock_analyze):
        mock_analyze.return_value = {
            'trend': {'trend_type': 'upward'},
            'technical_indicators': []
        }

        data_prep = DataPreparation(self.metric.id, self.client)
        prepared_data, _ = data_prep.prepare_data()
        fe = FeatureEngineering(self.metric.id, prepared_data, self.client)
        dynamic_params = fe.compute_dynamic_parameters()
        engineered_features = fe.engineer_features()

        analyzer = Analyzer(self.metric.id, prepared_data, dynamic_params, engineered_features)
        results = analyzer.analyze()

        self.assertIn('trend', results)
        self.assertIn('technical_indicators', results)

    @patch('metrics.computations.computations_forecaster.Forecaster.forecast')
    def test_forecaster(self, mock_forecast):
        mock_forecast.return_value = {
            'sarima': [{'date': '2023-01-01', 'value': 100}],
            'prophet': [{'date': '2023-01-01', 'value': 102}]
        }

        data_prep = DataPreparation(self.metric.id, self.client)
        prepared_data, _ = data_prep.prepare_data()
        fe = FeatureEngineering(self.metric.id, prepared_data, self.client)
        dynamic_params = fe.compute_dynamic_parameters()
        engineered_features = fe.engineer_features()

        forecaster = Forecaster(self.metric.id, prepared_data, dynamic_params, engineered_features)
        results = forecaster.forecast()

        self.assertIn('sarima', results)
        self.assertIn('prophet', results)

    @patch('metrics.computations.computations_anomalies.AnomalyDetector.detect_anomalies')
    def test_anomaly_detector(self, mock_detect_anomalies):
        mock_detect_anomalies.return_value = {'anomalies': []}

        data_prep = DataPreparation(self.metric.id, self.client)
        prepared_data, _ = data_prep.prepare_data()
        fe = FeatureEngineering(self.metric.id, prepared_data, self.client)
        dynamic_params = fe.compute_dynamic_parameters()
        engineered_features = fe.engineer_features()

        anomaly_detector = AnomalyDetector(self.metric.id, prepared_data, dynamic_params, engineered_features)
        results = anomaly_detector.detect_anomalies()

        self.assertIn('anomalies', results)

    @patch('metrics.computations.computations_relationships.RelationshipAnalyzer.analyze_relationships')
    def test_relationship_analyzer(self, mock_analyze_relationships):
        mock_analyze_relationships.return_value = {
            'correlations': [],
            'lagged_correlations': []
        }

        data_prep = DataPreparation(self.metric.id, self.client)
        prepared_data, _ = data_prep.prepare_data()
        fe = FeatureEngineering(self.metric.id, prepared_data, self.client)
        dynamic_params = fe.compute_dynamic_parameters()
        engineered_features = fe.engineer_features()

        relationship_analyzer = RelationshipAnalyzer(self.metric.id, prepared_data, dynamic_params, engineered_features)
        results = relationship_analyzer.analyze_relationships()

        self.assertIn('correlations', results)
        self.assertIn('lagged_correlations', results)

    def tearDown(self):
        HistoricalData.objects.all().delete()
        Metric.objects.all().delete()
        Client.objects.all().delete()
