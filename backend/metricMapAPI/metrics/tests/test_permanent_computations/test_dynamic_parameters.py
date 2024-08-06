from django.test import TestCase
from django.utils import timezone
from datetime import timedelta, datetime
import numpy as np
import pandas as pd
from ...models import Metric, HistoricalData, Client, Domain, Project, Category, ValueType, MetricType
from ...computations.feature_engineering import FeatureEngineering, get_dynamic_parameters, get_engineered_features
from unittest.mock import patch, MagicMock
import logging
from statsmodels.tsa.seasonal import seasonal_decompose


class TestFeatureEngineering(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger('metrics.computations.feature_engineering')
        logger.setLevel(logging.DEBUG)

    @classmethod
    def setUpTestData(cls):
        # Create a test client (tenant)
        cls.tenant = Client.objects.create(
            schema_name='test',
            name='Test Client'
        )
        cls.domain = Domain.objects.create(
            domain='test.localhost',
            tenant=cls.tenant,
            is_primary=True
        )
        
        # Create a test project
        cls.project = Project.objects.create(name="Test Project", tenant=cls.tenant)
        
        # Create a test category
        cls.category = Category.objects.create(name="Test Category", tenant=cls.tenant)
        
        # Create a test metric
        cls.metric = Metric.objects.create(
            name="Test Metric",
            tenant=cls.tenant,
            project=cls.project,
            category=cls.category,
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        
        # Create some test data
        cls.start_date = timezone.now().date() - timedelta(days=110)
        data = []
        for i in range(110):
            value = 10 + i + 5 * np.sin(i / 7 * 2 * np.pi)  # Create a sinusoidal pattern with trend
            if i >= 100 and i < 105:
                value = 1000 if i % 2 == 0 else -1000  # Add some outliers
            elif i >= 105:
                value = None  # Add some missing values
            data.append(HistoricalData(
                tenant=cls.tenant,
                metric=cls.metric,
                date=cls.start_date + timedelta(days=i),
                value=value
            ))
        HistoricalData.objects.bulk_create(data)

    def setUp(self):
        self.fe = FeatureEngineering(self.metric.id)

    def test_low_quality_data(self):
        # Mock a low-quality dataset
        low_quality_data = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=100),
            'value': np.random.normal(100, 50, 100)  # High variance, potentially outliers
        })
        low_quality_data.loc[10:20, 'value'] = np.nan  # Add missing values

        with patch('metrics.computations.data_preparation.DataPreparation.prepare_data') as mock_prepare:
            mock_prepare.return_value = (low_quality_data, {'data_quality_score': 30, 'is_stationary': False})
            fe = FeatureEngineering(self.metric.id)
            params = fe.compute_dynamic_parameters()

        self.assertIn('base_threshold', params)
        self.assertGreater(params['base_threshold'], 3.0)  # Expect higher threshold for noisy data
        self.assertEqual(params['forecast_horizon'], 7)  # Expect shorter forecast horizon for low-quality data

    def test_small_dataset(self):
        small_data = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=20),
            'value': np.random.normal(100, 10, 20)
        })

        with patch('metrics.computations.data_preparation.DataPreparation.prepare_data') as mock_prepare:
            mock_prepare.return_value = (small_data, {'data_quality_score': 80, 'is_stationary': True})
            fe = FeatureEngineering(self.metric.id)
            params = fe.compute_dynamic_parameters()

        self.assertEqual(params['seasonality_period'], 7)  # Default weekly seasonality for small datasets
        self.assertEqual(params['forecast_horizon'], 7)
        self.assertEqual(params['trend_window'], 20)  # Should use full dataset length for small datasets

    def test_large_high_quality_dataset(self):
        # Generate 3 years of daily data with a clear yearly pattern
        dates = pd.date_range(start='2020-01-01', end='2022-12-31', freq='D')
        values = 100 + 50 * np.sin(2 * np.pi * np.arange(len(dates)) / 365) + np.random.normal(0, 5, len(dates))
        large_data = pd.DataFrame({'date': dates, 'value': values})

        with patch('metrics.computations.data_preparation.DataPreparation.prepare_data') as mock_prepare:
            mock_prepare.return_value = (large_data, {'data_quality_score': 95, 'is_stationary': False})
            fe = FeatureEngineering(self.metric.id)
            params = fe.compute_dynamic_parameters()

        print(f"Computed parameters: {params}")  # Add this line for debugging
        self.assertAlmostEqual(params['seasonality_period'], 365, delta=5)  # Should detect yearly seasonality
        self.assertEqual(params['forecast_horizon'], 30)  # Max forecast horizon for large datasets
        self.assertGreater(params['trend_window'], 90)  # Longer trend window for large datasets

    def test_parameter_consistency(self):
        data1 = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=500),
            'value': np.sin(np.arange(500) * 2 * np.pi / 30) + np.random.normal(0, 0.1, 500)  # Monthly seasonality
        })
        data2 = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=510),
            'value': np.sin(np.arange(510) * 2 * np.pi / 30) + np.random.normal(0, 0.1, 510)  # Similar data, slightly longer
        })

        with patch('metrics.computations.data_preparation.DataPreparation.prepare_data') as mock_prepare:
            mock_prepare.side_effect = [(data1, {'data_quality_score': 90, 'is_stationary': False}),
                                        (data2, {'data_quality_score': 90, 'is_stationary': False})]
            fe1 = FeatureEngineering(self.metric.id)
            fe2 = FeatureEngineering(self.metric.id)
            params1 = fe1.compute_dynamic_parameters()
            params2 = fe2.compute_dynamic_parameters()

        self.assertAlmostEqual(params1['seasonality_period'], params2['seasonality_period'], delta=2)
        self.assertEqual(params1['forecast_horizon'], params2['forecast_horizon'])
        self.assertAlmostEqual(params1['base_threshold'], params2['base_threshold'], delta=0.5)

    def test_parameter_accuracy(self):
        # Create a dataset with known characteristics
        dates = pd.date_range(start='2023-01-01', periods=730)  # 2 years of daily data
        values = 100 + 20 * np.sin(np.arange(730) * 2 * np.pi / 365) + np.arange(730) * 0.05 + np.random.normal(0, 5, 730)  # Yearly seasonality with trend and noise
        data = pd.DataFrame({'date': dates, 'value': values})

        with patch('metrics.computations.data_preparation.DataPreparation.prepare_data') as mock_prepare:
            mock_prepare.return_value = (data, {'data_quality_score': 95, 'is_stationary': False})
            fe = FeatureEngineering(self.metric.id)
            params = fe.compute_dynamic_parameters()

        self.assertAlmostEqual(params['seasonality_period'], 365, delta=10)  # Should detect yearly seasonality
        self.assertGreaterEqual(params['trend_window'], 60)  # Should have a reasonably long trend window
        self.assertLess(params['trend_window'], 180)  # But not too long
        self.assertGreaterEqual(params['base_threshold'], 10)  # Minimum threshold is now 10
        self.assertLessEqual(params['base_threshold'], data['value'].std())  # Should not exceed the standard deviation
        
        # Add a check for seasonality influence
        if params['seasonality_period']:
            seasonal_component = seasonal_decompose(data['value'], model='additive', period=params['seasonality_period']).seasonal
            seasonality_amplitude = (seasonal_component.max() - seasonal_component.min()) / 2
            self.assertGreaterEqual(params['base_threshold'], 0.5 * seasonality_amplitude)

    def test_compute_dynamic_parameters(self):
        params = self.fe.compute_dynamic_parameters()
        expected_params = [
            'seasonality_period', 'forecast_horizon', 'correlation_window',
            'trend_window', 'anomaly_detection_window', 'base_threshold',
            'imputation_method'
        ]
        for param in expected_params:
            self.assertIn(param, params)

        # Check if imputation_method is in metadata
        self.assertIn('imputation_method', self.fe.metadata)

    def test_profile_data(self):
        profile = self.fe.profile_data()
        expected_keys = [
            'length', 'mean', 'median', 'std', 'min', 'max', 'skewness', 'kurtosis',
            'q1', 'q3', 'iqr', 'missing_percentage', 'autocorrelation', 'is_stationary'
        ]
        for key in expected_keys:
            self.assertIn(key, profile)

    def test_detect_seasonality(self):
        fe = FeatureEngineering(self.metric.id)
        seasonality = fe.detect_seasonality()
        
        self.assertIsInstance(seasonality, dict)
        self.assertIn('period', seasonality)
        self.assertIn('strength', seasonality)
        self.assertIn('amplitude', seasonality)
        self.assertIn('component', seasonality)

        # Additional checks can be added here
        if seasonality['period'] is not None:
            self.assertGreater(seasonality['strength'], 0)
            self.assertGreater(seasonality['amplitude'], 0)
            self.assertIsNotNone(seasonality['component'])
        else:
            self.assertEqual(seasonality['strength'], 0)
            self.assertEqual(seasonality['amplitude'], 0)
            self.assertIsNone(seasonality['component'])

    def test_detect_trend_changes(self):
        trend_changes = self.fe.detect_trend_changes()
        self.assertIn('is_stationary', trend_changes)
        self.assertIn('num_change_points', trend_changes)
        if len(self.fe.df) < 2:
            self.assertIsNone(trend_changes['is_stationary'])
            self.assertEqual(trend_changes['num_change_points'], 0)

    def test_get_dynamic_parameters(self):
        params = get_dynamic_parameters(self.metric.id)
        self.assertIsInstance(params, dict)

    def test_get_engineered_features(self):
        fe = FeatureEngineering(self.metric.id)
        features = fe.engineer_features()

        self.assertIn('seasonality_period', features)
        self.assertIn('seasonality_strength', features)
        self.assertIn('seasonality_amplitude', features)
        self.assertIn('trend_changes', features)
        self.assertIn('volatility', features)
        self.assertIn('profile', features)

        # Check seasonality
        if features['seasonality_period'] is not None:
            self.assertGreater(features['seasonality_period'], 0)
            self.assertGreaterEqual(features['seasonality_strength'], 0)
            self.assertGreaterEqual(features['seasonality_amplitude'], 0)
        else:
            self.assertEqual(features['seasonality_strength'], 0)
            self.assertEqual(features['seasonality_amplitude'], 0)

        # Check trend changes
        self.assertIsInstance(features['trend_changes'], dict)
        self.assertIn('is_stationary', features['trend_changes'])
        self.assertIn('num_change_points', features['trend_changes'])
        self.assertIn('change_points', features['trend_changes'])
        
        # Check if is_stationary is a boolean or can be converted to a boolean
        self.assertIn(features['trend_changes']['is_stationary'], [True, False, 0, 1])
        
        self.assertIsInstance(features['trend_changes']['num_change_points'], int)
        self.assertIsInstance(features['trend_changes']['change_points'], list)

        # Check volatility
        self.assertIsInstance(features['volatility'], dict)
        self.assertIn('std_dev', features['volatility'])
        self.assertIn('coefficient_of_variation', features['volatility'])
        self.assertIn('average_true_range', features['volatility'])

        # Check profile
        self.assertIsInstance(features['profile'], dict)
        # Add more specific checks for profile if needed

    def test_small_dataset(self):
        small_metric = Metric.objects.create(
            name="Small Test Metric",
            tenant=self.tenant,
            project=self.project,
            category=self.category,
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        for i in range(10):
            HistoricalData.objects.create(
                tenant=self.tenant,
                metric=small_metric,
                date=self.start_date + timedelta(days=i),
                value=10 + i
            )
        fe_small = FeatureEngineering(small_metric.id)
        params = fe_small.compute_dynamic_parameters()
        self.assertEqual(params['seasonality_period'], 7)
        self.assertLessEqual(params['forecast_horizon'], 7)

    def test_edge_cases(self):
        empty_metric = Metric.objects.create(
            name="Empty Metric",
            tenant=self.tenant,
            project=self.project,
            category=self.category,
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        fe_empty = FeatureEngineering(empty_metric.id)
        params = fe_empty.compute_dynamic_parameters()
        self.assertIsInstance(params, dict)
        self.assertEqual(params['seasonality_period'], 7)  # Default value for small datasets

    def test_constant_value_dataset(self):
        constant_data = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=100),
            'value': [10] * 100
        })
        with patch('metrics.computations.data_preparation.DataPreparation.prepare_data') as mock_prepare:
            mock_prepare.return_value = (constant_data, {'data_quality_score': 80, 'is_stationary': True})
            fe = FeatureEngineering(self.metric.id)
            params = fe.compute_dynamic_parameters()

        self.assertIsNone(params['seasonality_period'])
        self.assertEqual(params['base_threshold'], 0)

    def test_consistency_across_runs(self):
        data = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=365),
            'value': np.sin(np.arange(365) * 2 * np.pi / 365) + np.random.normal(0, 0.1, 365)
        })
        with patch('metrics.computations.data_preparation.DataPreparation.prepare_data') as mock_prepare:
            mock_prepare.return_value = (data, {'data_quality_score': 90, 'is_stationary': False})
            fe = FeatureEngineering(self.metric.id)
            params1 = fe.compute_dynamic_parameters()
            params2 = fe.compute_dynamic_parameters()

        for key in params1.keys():
            self.assertEqual(params1[key], params2[key])

    def test_parameter_bounds(self):
        data = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=1000),
            'value': np.random.normal(0, 1, 1000)
        })
        with patch('metrics.computations.data_preparation.DataPreparation.prepare_data') as mock_prepare:
            mock_prepare.return_value = (data, {'data_quality_score': 90, 'is_stationary': False})
            fe = FeatureEngineering(self.metric.id)
            params = fe.compute_dynamic_parameters()

        self.assertLessEqual(params['forecast_horizon'], 30)
        self.assertLessEqual(params['correlation_window'], 90)
        self.assertGreaterEqual(params['trend_window'], 7)
        self.assertLessEqual(params['anomaly_detection_window'], 30)
        self.assertGreaterEqual(params['base_threshold'], 1.5)
        self.assertLessEqual(params['base_threshold'], 5.0)

    @classmethod
    def tearDownClass(cls):
        # Clean up created data
        HistoricalData.objects.filter(tenant=cls.tenant).delete()
        Metric.objects.filter(tenant=cls.tenant).delete()
        Project.objects.filter(tenant=cls.tenant).delete()
        Category.objects.filter(tenant=cls.tenant).delete()
        Domain.objects.filter(tenant=cls.tenant).delete()
        cls.tenant.delete()
        super().tearDownClass()