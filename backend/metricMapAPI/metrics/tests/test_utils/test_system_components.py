from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch, MagicMock
from metrics.models import Client, Metric, ComputationStatus, Notification, PendingComputation
from metrics.tasks import run_computations
from metrics.signals import throttle_computations
from django.db.models.signals import post_save
from metrics.managers import MetricManager

class TestSystemComponents(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name="Test Client", schema_name="test_schema")
        self.metric = Metric.objects.create(
            tenant=self.client,
            name="Test Metric",
            type="KPI",
            value_type="COUNT"
        )

    def test_metric_manager(self):
        # Test the custom manager method
        with_pending_computations = Metric.objects.with_pending_computations()
        self.assertQuerysetEqual(with_pending_computations, [])

        # Create a pending computation
        PendingComputation.objects.create(tenant=self.client, metric=self.metric)
        with_pending_computations = Metric.objects.with_pending_computations()
        self.assertQuerysetEqual(with_pending_computations, [self.metric])

    @patch('metrics.signals.run_computations.delay')
    def test_throttle_computations(self, mock_run_computations):
        # Test that the signal throttles computations
        for _ in range(5):
            throttle_computations(sender=Metric, instance=self.metric)

        self.assertEqual(mock_run_computations.call_count, 1)

    @patch('metrics.tasks.PermanentComputations')
    def test_run_computations_task(self, mock_permanent_computations):
        # Test the Celery task
        run_computations(self.client.id, [self.metric.id])

        mock_permanent_computations.assert_called_once_with([self.metric.id], self.client)
        mock_permanent_computations.return_value.run_all_computations.assert_called_once()

        # Check that ComputationStatus and Notification were created
        self.assertTrue(ComputationStatus.objects.filter(tenant=self.client).exists())
        self.assertTrue(Notification.objects.filter(tenant=self.client).exists())

    def test_computation_status_creation(self):
        status = ComputationStatus.objects.create(
            tenant=self.client,
            status="PENDING"
        )
        self.assertEqual(ComputationStatus.objects.count(), 1)
        self.assertEqual(status.status, "PENDING")

    def test_notification_creation(self):
        notification = Notification.objects.create(
            tenant=self.client,
            message="Test notification"
        )
        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(notification.message, "Test notification")

    def test_pending_computation_creation(self):
        pending = PendingComputation.objects.create(
            tenant=self.client,
            metric=self.metric
        )
        self.assertEqual(PendingComputation.objects.count(), 1)
        self.assertEqual(pending.metric, self.metric)

    @patch('metrics.signals.run_computations.delay')
    def test_metric_creation_signal(self, mock_run_computations):
        new_metric = Metric.objects.create(
            tenant=self.client,
            name="New Test Metric",
            type="KPI",
            value_type="COUNT"
        )
        mock_run_computations.assert_called_once_with(self.client.id, [new_metric.id])

    def tearDown(self):
        Metric.objects.all().delete()
        Client.objects.all().delete()
        ComputationStatus.objects.all().delete()
        Notification.objects.all().delete()
        PendingComputation.objects.all().delete()
