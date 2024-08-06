from django.test import TestCase
from django.utils import timezone
from metrics.models import HistoricalData, Connection, Metric, Tenant, Project
from metrics.computations.permanent_computations import PermanentComputations
from unittest.mock import patch

class TestSignals(TestCase):
    def setUp(self):
        self.tenant = Tenant.objects.create(name="Test Tenant")
        self.project = Project.objects.create(name="Test Project", tenant=self.tenant)
        self.metric1 = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="Metric 1",
            type="KPI",
            value_type="COUNT"
        )
        self.metric2 = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="Metric 2",
            type="KPI",
            value_type="COUNT"
        )

    @patch.object(PermanentComputations, 'run_all_computations')
    def test_historical_data_creation_signal(self, mock_run_all_computations):
        historical_data = HistoricalData.objects.create(
            metric=self.metric1,
            date=timezone.now().date(),
            value=100,
            tenant=self.tenant
        )
        mock_run_all_computations.assert_called_once_with()
        args, kwargs = mock_run_all_computations.call_args
        self.assertEqual(args[0], [self.metric1.id])
        self.assertEqual(kwargs['tenant'], self.tenant)

    @patch.object(PermanentComputations, 'run_all_computations')
    def test_historical_data_update_signal(self, mock_run_all_computations):
        historical_data = HistoricalData.objects.create(
            metric=self.metric1,
            date=timezone.now().date(),
            value=100,
            tenant=self.tenant
        )
        mock_run_all_computations.reset_mock()
        
        historical_data.value = 200
        historical_data.save()
        
        mock_run_all_computations.assert_called_once_with()
        args, kwargs = mock_run_all_computations.call_args
        self.assertEqual(args[0], [self.metric1.id])
        self.assertEqual(kwargs['tenant'], self.tenant)

    @patch.object(PermanentComputations, 'run_all_computations')
    def test_historical_data_deletion_signal(self, mock_run_all_computations):
        historical_data = HistoricalData.objects.create(
            metric=self.metric1,
            date=timezone.now().date(),
            value=100,
            tenant=self.tenant
        )
        mock_run_all_computations.reset_mock()
        
        historical_data.delete()
        
        mock_run_all_computations.assert_called_once_with()
        args, kwargs = mock_run_all_computations.call_args
        self.assertEqual(args[0], [self.metric1.id])
        self.assertEqual(kwargs['tenant'], self.tenant)

    @patch.object(PermanentComputations, 'run_all_computations')
    def test_connection_creation_signal(self, mock_run_all_computations):
        connection = Connection.objects.create(
            from_metric=self.metric1,
            to_metric=self.metric2,
            tenant=self.tenant,
            strength=0.5
        )
        mock_run_all_computations.assert_called_once_with()
        args, kwargs = mock_run_all_computations.call_args
        self.assertCountEqual(args[0], [self.metric1.id, self.metric2.id])
        self.assertEqual(kwargs['tenant'], self.tenant)

    @patch.object(PermanentComputations, 'run_all_computations')
    def test_connection_update_signal(self, mock_run_all_computations):
        connection = Connection.objects.create(
            from_metric=self.metric1,
            to_metric=self.metric2,
            tenant=self.tenant,
            strength=0.5
        )
        mock_run_all_computations.reset_mock()
        
        connection.strength = 0.7
        connection.save()
        
        mock_run_all_computations.assert_called_once_with()
        args, kwargs = mock_run_all_computations.call_args
        self.assertCountEqual(args[0], [self.metric1.id, self.metric2.id])
        self.assertEqual(kwargs['tenant'], self.tenant)

    @patch.object(PermanentComputations, 'run_all_computations')
    def test_connection_deletion_signal(self, mock_run_all_computations):
        connection = Connection.objects.create(
            from_metric=self.metric1,
            to_metric=self.metric2,
            tenant=self.tenant,
            strength=0.5
        )
        mock_run_all_computations.reset_mock()
        
        connection.delete()
        
        mock_run_all_computations.assert_called_once_with()
        args, kwargs = mock_run_all_computations.call_args
        self.assertCountEqual(args[0], [self.metric1.id, self.metric2.id])
        self.assertEqual(kwargs['tenant'], self.tenant)

    @patch.object(PermanentComputations, 'run_all_computations')
    def test_metric_creation_signal(self, mock_run_all_computations):
        new_metric = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="New Test Metric",
            type="KPI",
            value_type="COUNT"
        )
        mock_run_all_computations.assert_called_once_with()
        args, kwargs = mock_run_all_computations.call_args
        self.assertEqual(args[0], [new_metric.id])
        self.assertEqual(kwargs['tenant'], self.tenant)

    @patch.object(PermanentComputations, 'run_all_computations')
    def test_metric_update_signal(self, mock_run_all_computations):
        self.metric1.name = "Updated Metric 1"
        self.metric1.save()
        
        # Metric updates should not trigger computations
        mock_run_all_computations.assert_not_called()
