# tests/test_views/test_performance_dashboard.py
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, HistoricalData
from datetime import date, timedelta
import random
from .test_utils import MetricsTestCase


class PerformanceDashboardTests(MetricsTestCase):
    def setUp(self):
        self.metric = Metric.objects.create(name='Test Metric', type='KPI')
        start_date = date(2022, 1, 1)
        for i in range(365):
            HistoricalData.objects.create(
                metric=self.metric,
                date=start_date + timedelta(days=i),
                value=100 + i * 0.1 + random.uniform(-5, 5)
            )

    def test_performance_dashboard(self):
        url = reverse('performance-dashboard', kwargs={'metric_id': self.metric.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('historical_data', response.data)
        self.assertIn('wow_changes', response.data)
        self.assertIn('mom_changes', response.data)