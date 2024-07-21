# tests/test_views/test_correlation_analysis.py
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, HistoricalData
from datetime import date, timedelta
import random
from .test_utils import MetricsTestCase


class CorrelationAnalysisTests(MetricsTestCase):
    def setUp(self):
        self.metric1 = Metric.objects.create(name='Metric 1', type='KPI')
        self.metric2 = Metric.objects.create(name='Metric 2', type='KPI')
        start_date = date(2022, 1, 1)
        for i in range(100):
            value1 = 100 + i * 0.5 + random.uniform(-5, 5)
            value2 = 200 - i * 0.5 + random.uniform(-5, 5)
            HistoricalData.objects.create(metric=self.metric1, date=start_date + timedelta(days=i), value=value1)
            HistoricalData.objects.create(metric=self.metric2, date=start_date + timedelta(days=i), value=value2)

    def test_correlation_analysis(self):
        url = reverse('correlation-analysis')
        data = {'metric_a': self.metric1.id, 'metric_b': self.metric2.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('correlation', response.data)
        self.assertTrue(-1 <= response.data['correlation'] <= 1)