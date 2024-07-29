from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
import pandas as pd
import numpy as np
from datetime import timedelta

from ...models import Metric, HistoricalData, DataQualityScore, Client, Domain, Project, MetricType, ValueType
from ...computations.permanent_computations import PermanentComputations

class TestPermanentComputationsSetup(TestCase):
    def setUp(self):
        # Create a test tenant
        self.tenant = Client.objects.create(
            name="Test Tenant",
            schema_name="test_tenant",
        )
        
        # Create a domain for the tenant
        self.domain = Domain.objects.create(
            domain="test.localhost",
            tenant=self.tenant,
            is_primary=True
        )
        
        # Create a test project
        self.project = Project.objects.create(name="Test Project", tenant=self.tenant)
        
        # Create a test metric with the tenant and project
        self.metric = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="Test Metric",
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        
        # Create historical data using bulk_create
        self.start_date = timezone.now().date() - timedelta(days=99)
        dates = [self.start_date + timedelta(days=i) for i in range(100)]
        historical_data = [
            HistoricalData(
                tenant=self.tenant,
                metric=self.metric,
                date=date,
                value=np.random.randint(1, 100)
            ) for date in dates
        ]
        HistoricalData.objects.bulk_create(historical_data)
        
        self.pc = PermanentComputations(self.metric.id)

    def test_tenant_and_project_setup(self):
        self.assertIsNotNone(self.tenant)
        self.assertIsNotNone(self.project)
        self.assertEqual(self.project.tenant, self.tenant)
        self.assertEqual(self.domain.tenant, self.tenant)

    def test_metric_associations(self):
        self.assertEqual(self.metric.tenant, self.tenant)
        self.assertEqual(self.metric.project, self.project)
        self.assertEqual(self.metric.type, MetricType.KPI.name)
        self.assertEqual(self.metric.value_type, ValueType.COUNT.name)

    def test_historical_data_creation(self):
        total_data = HistoricalData.objects.filter(metric=self.metric, tenant=self.tenant).count()
        self.assertEqual(total_data, 100)
        
        # Check data for specific dates
        first_data = HistoricalData.objects.get(metric=self.metric, date=self.start_date)
        self.assertIsNotNone(first_data)
        self.assertTrue(0 < first_data.value <= 100)

        last_data = HistoricalData.objects.get(metric=self.metric, date=self.start_date + timedelta(days=99))
        self.assertIsNotNone(last_data)
        self.assertTrue(0 < last_data.value <= 100)

    def test_load_historical_data(self):
        df = self.pc._load_historical_data()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 100)
        self.assertTrue('value' in df.columns)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df.index))
        self.assertTrue(pd.api.types.is_numeric_dtype(df['value']))

    def test_prepare_data(self):
        self.pc.prepare_data()
        self.assertIsNotNone(self.pc.df)
        self.assertIsInstance(self.pc.df, pd.DataFrame)
        self.assertIsNotNone(self.pc.data_quality_score)
        self.assertIsInstance(self.pc.data_quality_score, DataQualityScore)
        self.assertIsNotNone(self.pc.outliers)
        self.assertIsInstance(self.pc.outliers, pd.DataFrame)
        
        # Verify that the data quality score has been calculated and saved
        saved_score = DataQualityScore.objects.get(metric=self.metric, tenant=self.tenant, project=self.project)
        self.assertEqual(self.pc.data_quality_score, saved_score)

    def test_handle_missing_values(self):
       # Introduce some missing values
        historical_data = HistoricalData.objects.filter(metric=self.metric)
        for obj in list(historical_data)[::10]:
            obj.value = None
            obj.save()

        self.pc.raw_df = self.pc._load_historical_data()
        self.assertTrue(self.pc.raw_df['value'].isnull().any())  # Verify that we have null values
        
        self.pc.handle_missing_values()
        self.assertFalse(self.pc.raw_df['value'].isnull().any())
        
        # Verify that the values have been updated in the database
        updated_data = HistoricalData.objects.filter(metric=self.metric)
        self.assertFalse(any(obj.value is None for obj in updated_data))

    def test_detect_outliers(self):
        outliers = self.pc.detect_outliers()
        self.assertIsInstance(outliers, pd.DataFrame)
        self.assertTrue(len(outliers) < len(self.pc.raw_df))

    def test_calculate_data_quality_score(self):
        self.pc.raw_df = self.pc._load_historical_data()
        self.pc.outliers = self.pc.detect_outliers()
        self.pc.calculate_data_quality_score()
        
        self.assertIsNotNone(self.pc.data_quality_score)
        self.assertTrue(0 <= self.pc.data_quality_score.overall_score <= 1)
        self.assertEqual(self.pc.data_quality_score.metric, self.metric)
        self.assertEqual(self.pc.data_quality_score.tenant, self.tenant)
        self.assertEqual(self.pc.data_quality_score.project, self.project)
        
        # Verify that the score has been saved to the database
        saved_score = DataQualityScore.objects.get(metric=self.metric, tenant=self.tenant, project=self.project)
        self.assertEqual(self.pc.data_quality_score, saved_score)

    def test_error_handling_no_data(self):
        # Delete all historical data
        HistoricalData.objects.filter(metric=self.metric).delete()
        
        # Attempt to prepare data
        with self.assertRaises(ValueError):
            self.pc.prepare_data()

    def test_data_integrity_constraints(self):
        # Test uniqueness constraint
        with self.assertRaises(ValidationError):
            Metric.objects.create(
                tenant=self.tenant,
                project=self.project,
                name="Test Metric",  # Same name as existing metric
                type=MetricType.KPI.name,
                value_type=ValueType.COUNT.name
            )

    def tearDown(self):
        # Clean up created data
        HistoricalData.objects.filter(tenant=self.tenant).delete()
        Metric.objects.filter(tenant=self.tenant).delete()
        Project.objects.filter(tenant=self.tenant).delete()
        Domain.objects.filter(tenant=self.tenant).delete()
        self.tenant.delete()

if __name__ == '__main__':
    from django.core.management import call_command
    call_command('test', 'metrics.tests.test_permanent_computations_setup')