# tests/test_views/test_progress_tracking.py
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, HistoricalData, Target
from datetime import date
from .test_utils import MetricsTestCase


class ProgressTrackingTests(MetricsTestCase):
    def setUp(self):
        self.metric = Metric.objects.create(name='Test Metric', type='KPI')
        HistoricalData.objects.create(
            metric=self.metric,
            date=date(2023, 1, 1),
            value=50
        )
        Target.objects.create(
            metric=self.metric,
            target_value=100,
            target_date=date(2023, 12, 31)
        )

    def test_progress_tracking(self):
        url = reverse('progress-tracking', kwargs={'metric_id': self.metric.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('current_value', response.data)
        self.assertIn('target_value', response.data)
        self.assertIn('progress_percentage', response.data)
        self.assertEqual(response.data['progress_percentage'], 50.0)