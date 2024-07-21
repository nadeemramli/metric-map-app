# tests/test_views/test_forecast_vs_actual.py
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, HistoricalData
from datetime import date, timedelta
import random
from .test_utils import MetricsTestCase


class ForecastVsActualTests(MetricsTestCase):
    def setUp(self):
        self.metric = Metric.objects.create(name='Test Metric', type='KPI')
        start_date = date(2022, 1, 1)
        for i in range(365):
            HistoricalData.objects.create(
                metric=self.metric,
                date=start_date + timedelta(days=i),
                value=100 + i * 0.1 + random.uniform(-5, 5)
            )

    def test_forecast_vs_actual(self):
        url = reverse('forecast-vs-actual', kwargs={'metric_id': self.metric.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('metric', response.data)
        self.assertIn('forecast_vs_actual', response.data)
        self.assertTrue(len(response.data['forecast_vs_actual']) > 0)