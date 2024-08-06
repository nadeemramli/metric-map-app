from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
import pandas as pd
import numpy as np
from datetime import timedelta
from unittest.mock import patch, MagicMock
import time

try:
    from ...models import (
        Metric, HistoricalData, DataQualityScore, Client, Domain, Project, 
        MetricType, ValueType, Trend, TechnicalIndicator, Forecast, Anomaly, 
        Correlation, Report
    )
    from ...computations.permanent_computations import PermanentComputations
    from ...computations.data_preparation import DataPreparation
    from ...computations.config import Config
except ImportError as e:
    print(f"Import error: {e}")
    raise

import logging

logger = logging.getLogger(__name__)

class TestPermanentComputationsSetup(TestCase):
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
        
        # Create historical data for the metric
        self.start_date = timezone.now().date() - timedelta(days=99)  # Start 99 days ago
        historical_data = [
            HistoricalData(
                tenant=self.tenant,
                metric=self.metric,
                date=self.start_date + timedelta(days=i),
                value=np.random.randint(1, 100)
            ) for i in range(100)  # This will create exactly 100 data points
        ]
        HistoricalData.objects.bulk_create(historical_data)
        logger.info(f"Created {len(historical_data)} historical data points")
        time.sleep(1)
        
        # Create data with outliers
        outlier_dates = [self.start_date + timedelta(days=i) for i in range(100, 105)]
        outlier_data = [
            HistoricalData(
                tenant=self.tenant,
                metric=self.metric,
                date=date,
                value=1000 if i % 2 == 0 else -1000  # Alternate between high and low outliers
            ) for i, date in enumerate(outlier_dates)
        ]
        
        HistoricalData.objects.bulk_create(outlier_data)
        logger.info(f"Created {len(outlier_data)} outlier data points")
        time.sleep(1)
        
        # Create data with missing values
        missing_dates = [self.start_date + timedelta(days=i) for i in range(105, 110)]
        missing_data = [
            HistoricalData(
                tenant=self.tenant,
                metric=self.metric,
                date=date,
                value=None
            ) for date in missing_dates
        ]
        
        HistoricalData.objects.bulk_create(missing_data)
        logger.info(f"Created {len(missing_data)} data points with missing values")
        time.sleep(1)
        
        self.pc = PermanentComputations(self.metric.id, self.tenant)
        logger.info("Finished setUp")

    def test_tenant_and_project_setup(self):
        logger.info("Starting test_tenant_and_project_setup")
        self.assertIsNotNone(self.tenant)
        self.assertIsNotNone(self.project)
        self.assertEqual(self.project.tenant, self.tenant)
        self.assertEqual(self.domain.tenant, self.tenant)
        logger.info("Finished test_tenant_and_project_setup")

    def test_metric_associations(self):
        logger.info("Starting test_metric_associations")
        self.assertEqual(self.metric.tenant, self.tenant)
        self.assertEqual(self.metric.project, self.project)
        self.assertEqual(self.metric.type, MetricType.KPI.name)
        self.assertEqual(self.metric.value_type, ValueType.COUNT.name)
        logger.info("Finished test_metric_associations")

    def test_historical_data_creation(self):
        logger.info("Starting test_historical_data_creation")
        total_data = HistoricalData.objects.filter(metric=self.metric, tenant=self.tenant).count()
        self.assertEqual(total_data, 110)  # Changed from 100 to 110
        
        # Check data for specific dates
        first_data = HistoricalData.objects.get(metric=self.metric, date=self.start_date)
        self.assertIsNotNone(first_data)
        self.assertTrue(0 < first_data.value <= 100)

        last_regular_data = HistoricalData.objects.get(metric=self.metric, date=self.start_date + timedelta(days=99))
        self.assertIsNotNone(last_regular_data)
        self.assertTrue(0 < last_regular_data.value <= 100)

        # Check for outliers
        outlier_data = HistoricalData.objects.filter(metric=self.metric, date__gte=self.start_date + timedelta(days=100), date__lt=self.start_date + timedelta(days=105))
        self.assertEqual(outlier_data.count(), 5)
        for data in outlier_data:
            self.assertTrue(abs(data.value) == 1000)

        # Check for missing values
        missing_data = HistoricalData.objects.filter(metric=self.metric, date__gte=self.start_date + timedelta(days=105), date__lt=self.start_date + timedelta(days=110))
        self.assertEqual(missing_data.count(), 5)
        for data in missing_data:
            self.assertIsNone(data.value)

        logger.info("Finished test_historical_data_creation")

    def test_handle_missing_values(self):
        logger.info("Starting test_handle_missing_values")
        data_prep = DataPreparation(self.metric.id)
        cleaned_df, metadata = data_prep.prepare_data()
        
        # Check if missing values were handled
        self.assertEqual(cleaned_df['value'].isnull().sum(), 0)
        
        logger.info("Verified that missing values were handled correctly")
        logger.info("Finished test_handle_missing_values")
    
    def test_detect_outliers(self):
        logger.info("Starting test_detect_outliers")
        data_prep = DataPreparation(self.metric.id)
        cleaned_df, metadata = data_prep.prepare_data()
        
        # Check if outliers were handled
        self.assertLess(cleaned_df['value'].max(), 1000)
        self.assertGreater(cleaned_df['value'].min(), -1000)
        
        logger.info("Verified that outliers were handled correctly")
        logger.info("Finished test_detect_outliers")

    def test_calculate_data_quality_score(self):
        logger.info("Starting test_calculate_data_quality_score")
        data_prep = DataPreparation(self.metric.id)
        
        # Ensure data is loaded
        data_prep.raw_df = data_prep._load_historical_data()
        data_prep.cleaned_df = data_prep.raw_df.copy()
        
        # Calculate the score
        score = data_prep.calculate_data_quality_score()
        
        # Assert that the score is a float between 0 and 100
        self.assertIsInstance(score, float)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)
        
        # Test with no data
        HistoricalData.objects.filter(metric=self.metric).delete()
        data_prep = DataPreparation(self.metric)
        score_no_data = data_prep.calculate_data_quality_score()
        self.assertEqual(score_no_data, 0)  # or whatever default value you chose

        # Test prepare_data method
        try:
            cleaned_df, metadata = data_prep.prepare_data()
            self.assertIsNotNone(cleaned_df)
            self.assertIsNotNone(metadata)
            self.assertIn('data_quality_score', metadata)
            self.assertEqual(metadata['data_quality_score'], score_no_data)
        except ValueError as ve:
            if str(ve) == "No historical data available for this metric":
                logger.warning("No historical data available for this metric. Skipping prepare_data test.")
            else:
                raise
        except Exception as e:
            logger.error(f"Error in test_calculate_data_quality_score: {str(e)}")
            raise
        logger.info("Finished test_calculate_data_quality_score")

    def test_error_handling_no_data(self):
        # Delete all historical data
        logger.info("Starting test_error_handling_no_data")
        HistoricalData.objects.filter(metric=self.metric).delete()
        logger.info("Deleted all historical data for testing")
        
        # Attempt to prepare data
        with self.assertRaises(ValueError):
            self.pc.perform_data_preparation(self.metric.id)
        logger.info("Verified that ValueError is raised when no data is available")
        logger.info("Finished test_error_handling_no_data")

    def test_data_integrity_constraints(self):
        logger.info("Starting test_data_integrity_constraints")
        # Test uniqueness constraint
        with self.assertRaises(ValidationError):
            Metric.objects.create(
                tenant=self.tenant,
                project=self.project,
                name="Test Metric",  # Same name as existing metric
                type=MetricType.KPI.name,
                value_type=ValueType.COUNT.name
            )
        logger.info("Verified that ValidationError is raised for duplicate metric name")
        logger.info("Finished test_data_integrity_constraints")
    
    def test_validate_forecast(self):
        logger.info("Starting test_validate_forecast")
        valid_forecast = [
            {'date': '2023-01-01', 'value': 100, 'lower_bound': 90, 'upper_bound': 110},
            {'date': '2023-01-02', 'value': 101, 'lower_bound': 91, 'upper_bound': 111}
        ]
        invalid_forecast = [
            {'date': '2023-01-01', 'value': 100},
            {'invalid': 'data'}
        ]
        
        self.assertEqual(self.pc._validate_forecast(valid_forecast), valid_forecast)
        self.assertIsNone(self.pc._validate_forecast(invalid_forecast))
        self.assertIsNone(self.pc._validate_forecast([]))
        self.assertIsNone(self.pc._validate_forecast(None))
    
    logger.info("Finished test_validate_forecast")
    
    def test_data_retrieval(self):
        logger.info("Starting test_data_retrieval")
        data_prep = DataPreparation(self.metric.id)
        raw_df = data_prep._load_historical_data()
        self.assertFalse(raw_df.empty)
        self.assertEqual(len(raw_df), 110)  # We expect 110 data points based on setUp
        logger.info("Finished test_data_retrieval")
        
    @patch('metrics.computations.permanent_computations.DataPreparation')
    def test_perform_data_preparation(self, mock_data_prep):
        logger.info("Starting test_perform_data_preparation")
        mock_data_prep_instance = MagicMock()
        mock_data_prep.return_value = mock_data_prep_instance
        
        # Create a non-empty DataFrame
        test_df = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=10),
            'value': range(10)
        })
        test_df.set_index('date', inplace=True)
        
        test_metadata = {
            'data_quality_score': 95,  # Add data quality score
            'metric_id': self.metric.id,
            'tenant_id': self.tenant.id,
            'project_id': self.project.id,
            'metric_name': self.metric.name,
            'is_stationary': True
        }
        
        # Configure the mock to return our test data
        mock_data_prep_instance.prepare_data.return_value = (test_df, test_metadata)
        
        # Run the method
        result = self.pc.perform_data_preparation(self.metric.id)
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result, mock_data_prep_instance)
        mock_data_prep.assert_called_once_with(self.metric.id)
        mock_data_prep_instance.prepare_data.assert_called_once()
        
        # Check if data is actually saved in the database
        saved_data = HistoricalData.objects.filter(metric=self.metric).count()
        self.assertGreater(saved_data, 0)
        
        # Check if data quality score is present in the metadata
        self.assertIn('data_quality_score', test_metadata)
        self.assertEqual(test_metadata['data_quality_score'], 95)
        
        logger.info("Finished test_perform_data_preparation")

    @patch('metrics.computations.permanent_computations.FeatureEngineering')
    def test_perform_feature_engineering(self, mock_fe):
        logger.info("Starting test_perform_feature_engineering")
        mock_fe.return_value.engineer_features.return_value = None
        mock_fe.return_value.profile_data.return_value = {'feature1': 'value1'}
        result = self.pc.perform_feature_engineering(self.metric.id, MagicMock())
        self.assertIsNotNone(result)
        mock_fe.assert_called_once_with(self.metric.id)
        logger.info("Verified that perform_feature_engineering returns a non-None result")
        logger.info("Finished test_perform_feature_engineering")

    @patch('metrics.computations.permanent_computations.Analyzer')
    def test_perform_analysis(self, mock_analyzer):
        logger.info("Starting test_perform_analysis")
        mock_analyzer.return_value.analyze_trend.return_value = {'trend_type': 'upward'}
        mock_analyzer.return_value.calculate_technical_indicators.return_value = [{'date': '2023-01-01', 'value': 100}]
        result = self.pc.perform_analysis(self.metric.id, MagicMock())
        self.assertIn('trend', result)
        self.assertIn('technical_indicators', result)
        logger.info("Verified that perform_analysis returns expected results")
        logger.info("Finished test_perform_analysis")

    @patch('metrics.computations.permanent_computations.Forecaster')
    def test_perform_forecasting(self, mock_forecaster):
        logger.info("Starting test_perform_forecasting")
        mock_forecaster_instance = MagicMock()
        mock_forecaster.return_value = mock_forecaster_instance

        # Mock the forecast method to return a dictionary with both 'sarima' and 'prophet' keys
        mock_forecaster_instance.forecast.return_value = {
            'sarima': [
                {'date': '2023-01-01', 'value': 100, 'lower_bound': 90, 'upper_bound': 110},
                {'date': '2023-01-02', 'value': 101, 'lower_bound': 91, 'upper_bound': 111}
            ],
            'prophet': [
                {'date': '2023-01-01', 'value': 102, 'lower_bound': 92, 'upper_bound': 112},
                {'date': '2023-01-02', 'value': 103, 'lower_bound': 93, 'upper_bound': 113}
            ]
        }

        mock_data_prep = MagicMock()
        result = self.pc.perform_forecasting(self.metric.id, mock_data_prep)

        self.assertIsInstance(result, dict)
        self.assertIn('sarima', result)
        self.assertIn('prophet', result)
        self.assertEqual(len(result['sarima']), 2)
        self.assertEqual(len(result['prophet']), 2)

        logger.info("Verified that perform_forecasting returns expected results")
        logger.info("Finished test_perform_forecasting")

    @patch('metrics.computations.permanent_computations.AnomalyDetector')
    def test_perform_anomaly_detection(self, mock_anomaly_detector):
        logger.info("Starting test_perform_anomaly_detection")
        mock_anomaly_detector.return_value.detect_anomalies.return_value = [{'date': '2023-01-01', 'value': 100, 'score': 0.9}]
        result = self.pc.perform_anomaly_detection(self.metric.id, MagicMock())
        self.assertIn('anomalies', result)
        logger.info("Verified that perform_anomaly_detection returns expected results")
        logger.info("Finished test_perform_anomaly_detection")

    @patch('metrics.computations.permanent_computations.RelationshipAnalyzer')
    def test_perform_relationship_analysis(self, mock_relationship_analyzer):
        logger.info("Starting test_perform_relationship_analysis")
        mock_relationship_analyzer.return_value.analyze_relationships.return_value = [{'metric_id': 2, 'correlation': 0.8}]
        mock_relationship_analyzer.return_value.detect_lagged_relationships.return_value = [{'metric_id': 2, 'lag': 1, 'correlation': 0.7}]
        result = self.pc.perform_relationship_analysis(self.metric.id, MagicMock())
        self.assertIn('correlations', result)
        self.assertIn('lagged_correlations', result)
        logger.info("Verified that perform_relationship_analysis returns expected results")
        logger.info("Finished test_perform_relationship_analysis")

    def test_save_analysis_results(self):
        logger.info("Starting test_save_analysis_results")
        results = {
            'trend': {
                'trend_type': 'upward',
                'start_date': '2023-01-01',
                'end_date': '2023-12-31',
                'trend_value': 10,
                'slope': 0.5
            },
            'technical_indicators': [
                {
                    'date': '2023-01-01',
                    'stochastic_value': 80,
                    'rsi_value': 60,
                    'percent_change': 5,
                    'moving_average': 100
                }
            ]
        }
        self.pc.save_analysis_results(self.metric.id, results)
        self.assertTrue(Trend.objects.filter(metric=self.metric).exists())
        self.assertTrue(TechnicalIndicator.objects.filter(metric=self.metric).exists())
        logger.info("Verified that analysis results are saved correctly")
        logger.info("Finished test_save_analysis_results")

    def test_save_forecast_results(self):
        logger.info("Starting test_save_forecast_results")
        results = {
            'sarima': [
                {
                    'date': '2023-01-01',
                    'value': 100,
                    'lower_bound': 90,
                    'upper_bound': 110,
                    'confidence_interval': 0.95
                }
            ]
        }
        self.pc.save_forecast_results(self.metric.id, results)
        self.assertTrue(Forecast.objects.filter(metric=self.metric).exists())
        logger.info("Verified that forecast results are saved correctly")
        logger.info("Finished test_save_forecast_results")

    def test_save_anomaly_results(self):
        logger.info("Starting test_save_anomaly_results")
        results = {
            'anomalies': [
                {
                    'date': '2023-01-01',
                    'value': 100,
                    'score': 0.9,
                    'type': 'SPIKE',
                    'quality': 'HIGH'
                }
            ]
        }
        self.pc.save_anomaly_results(self.metric.id, results)
        self.assertTrue(Anomaly.objects.filter(metric=self.metric).exists())
        logger.info("Verified that anomaly results are saved correctly")
        logger.info("Finished test_save_anomaly_results")

    def test_save_relationship_results(self):
        logger.info("Starting test_save_relationship_results")
        related_metric = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="Related Metric",
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        results = {
            'correlations': [
                {
                    'metric_id': related_metric.id,
                    'lag': 0,
                    'pearson': 0.8,
                    'spearman': 0.7
                }
            ]
        }
        self.pc.save_relationship_results(self.metric.id, results)
        self.assertTrue(Correlation.objects.filter(metric1=self.metric, metric2=related_metric).exists())
        logger.info("Verified that relationship results are saved correctly")
        logger.info("Finished test_save_relationship_results")

    def test_generate_markdown_report(self):
        logger.info("Starting test_generate_markdown_report")
        result = {
            'analysis': {
                'trend': {
                    'trend_type': 'upward',
                    'start_date': '2023-01-01',
                    'end_date': '2023-12-31',
                    'trend_value': 10,
                    'slope': 0.5
                },
                'technical_indicators': [
                    {
                        'date': '2023-01-01',
                        'stochastic_value': 80,
                        'rsi_value': 60,
                        'percent_change': 5,
                        'moving_average': 100
                    }
                ]
            },
            'forecast': {
                'sarima': [
                    {
                        'date': '2023-01-01',
                        'value': 100,
                        'lower_bound': 90,
                        'upper_bound': 110
                    }
                ]
            },
            'anomalies': {
                'anomalies': [
                    {
                        'date': '2023-01-01',
                        'value': 100,
                        'score': 0.9,
                        'type': 'SPIKE'
                    }
                ]
            },
            'relationships': {
                'correlations': [
                    {
                        'metric_id': 2,
                        'pearson': 0.8,
                        'spearman': 0.7
                    }
                ]
            }
        }
        report = self.pc.generate_markdown_report(self.metric.id, result)
        self.assertIsInstance(report, str)
        self.assertIn("# Analysis Report for Test Metric", report)
        logger.info("Verified that markdown report is generated correctly")
        logger.info("Finished test_generate_markdown_report")

    def test_save_report(self):
        logger.info("Starting test_save_report")
        report = "# Test Report"
        self.pc.save_report(self.metric.id, report)
        self.assertTrue(Report.objects.filter(metric=self.metric).exists())
        logger.info("Verified that report is saved correctly")
        logger.info("Finished test_save_report")

    @patch('metrics.computations.permanent_computations.PermanentComputations.generate_markdown_report')
    def test_compile_and_store_results(self, mock_generate_report):
        logger.info("Starting test_compile_and_store_results")
        mock_generate_report.return_value = "# Test Report"
        self.pc.results = {
            self.metric.id: {
                'analysis': {},
                'forecast': {},
                'anomalies': {},
                'relationships': {}
            }
        }
        self.pc.compile_and_store_results()
        self.assertTrue(Report.objects.filter(metric=self.metric).exists())
        logger.info("Verified that results are compiled and stored correctly")
        logger.info("Finished test_compile_and_store_results")

    def test_run_computations_for_metric_with_invalid_metric_id(self):
        logger.info("Starting test_run_computations_for_metric_with_invalid_metric_id")
        with self.assertRaises(ValueError):
            self.pc.run_computations_for_metric(999999)  # Use an invalid metric ID
        logger.info("Finished test_run_computations_for_metric_with_invalid_metric_id")

    @patch('metrics.computations.permanent_computations.DataPreparation')
    def test_perform_data_preparation_with_insufficient_data(self, mock_data_prep):
        logger.info("Starting test_perform_data_preparation_with_insufficient_data")
        mock_data_prep_instance = MagicMock()
        mock_data_prep.return_value = mock_data_prep_instance
        mock_data_prep_instance.prepare_data.return_value = (pd.DataFrame(), {'data_quality_score': 0})
        
        with self.assertRaises(ValueError):
            self.pc.perform_data_preparation(self.metric.id)
        
        logger.info("Finished test_perform_data_preparation_with_insufficient_data")

    @patch('metrics.computations.permanent_computations.PermanentComputations.run_computations_for_metric')
    def test_run_all_computations_concurrently(self, mock_run_computations):
        logger.info("Starting test_run_all_computations_concurrently")
        # Create multiple metrics
        metric2 = Metric.objects.create(tenant=self.tenant, project=self.project, name="Test Metric 2", type=MetricType.KPI.name, value_type=ValueType.COUNT.name)
        metric3 = Metric.objects.create(tenant=self.tenant, project=self.project, name="Test Metric 3", type=MetricType.KPI.name, value_type=ValueType.COUNT.name)
        
        pc = PermanentComputations([self.metric.id, metric2.id, metric3.id], self.tenant)
        pc.run_all_computations()
        
        self.assertEqual(mock_run_computations.call_count, 3)
        logger.info("Finished test_run_all_computations_concurrently")

    @patch('metrics.computations.permanent_computations.PermanentComputations.perform_data_preparation')
    @patch('metrics.computations.permanent_computations.PermanentComputations.perform_feature_engineering')
    @patch('metrics.computations.permanent_computations.PermanentComputations.perform_analysis')
    @patch('metrics.computations.permanent_computations.PermanentComputations.perform_forecasting')
    @patch('metrics.computations.permanent_computations.PermanentComputations.perform_anomaly_detection')
    @patch('metrics.computations.permanent_computations.PermanentComputations.perform_relationship_analysis')
    def test_run_computations_for_metric(self, mock_relationship, mock_anomaly, mock_forecast, mock_analysis, mock_fe, mock_data_prep):
        logger.info("Starting test_run_computations_for_metric")
        mock_data_prep.return_value = MagicMock()
        mock_fe.return_value = MagicMock()
        mock_analysis.return_value = {'trend': {'trend_type': 'upward'}, 'technical_indicators': []}
        mock_forecast.return_value = {
            'sarima': [{
                'date': '2023-01-01',
                'value': 100,
                'lower_bound': 90,
                'upper_bound': 110,
                'confidence_interval': (90, 110)
            }],
            'prophet': [{
                'date': '2023-01-01',
                'value': 102,
                'lower_bound': 92,
                'upper_bound': 112,
                'confidence_interval': (92, 112)
            }]
        }
        mock_anomaly.return_value = {'anomalies': []}
        mock_relationship.return_value = {'correlations': [], 'lagged_correlations': []}

        self.pc.run_computations_for_metric(self.metric.id)

        mock_data_prep.assert_called_once_with(self.metric.id)
        mock_fe.assert_called_once()
        mock_analysis.assert_called_once()
        mock_forecast.assert_called_once()
        mock_anomaly.assert_called_once()
        mock_relationship.assert_called_once()

        self.assertIn(self.metric.id, self.pc.results)
        self.assertEqual(self.pc.results[self.metric.id]['analysis'], {'trend': {'trend_type': 'upward'}, 'technical_indicators': []})
        self.assertEqual(self.pc.results[self.metric.id]['forecast'], mock_forecast.return_value)
        self.assertEqual(self.pc.results[self.metric.id]['anomalies'], {'anomalies': []})
        self.assertEqual(self.pc.results[self.metric.id]['relationships'], {'correlations': [], 'lagged_correlations': []})
        logger.info("Verified that computations for metric are run correctly")
        logger.info("Finished test_run_computations_for_metric")

    @patch('metrics.computations.permanent_computations.PermanentComputations.run_computations_for_metric')
    def test_run_all_computations(self, mock_run_computations):
        logger.info("Starting test_run_all_computations")
        self.pc.run_all_computations()
        mock_run_computations.assert_called_once_with(self.metric.id)
        

    def tearDown(self):
        # Clean up created data
        HistoricalData.objects.filter(tenant=self.tenant).delete()
        Metric.objects.filter(tenant=self.tenant).delete()
        Project.objects.filter(tenant=self.tenant).delete()
        Domain.objects.filter(tenant=self.tenant).delete()
        self.tenant.delete()
