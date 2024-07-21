# tests/test_views/test_visualization.py
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, Connection, HistoricalData
from datetime import date, timedelta
import random
from .test_utils import MetricsTestCase

class VisualizationTests(MetricsTestCase):
    def setUp(self):
        self.metric1 = Metric.objects.create(name='Metric 1', type='KPI')
        self.metric2 = Metric.objects.create(name='Metric 2', type='KPI')
        Connection.objects.create(from_metric=self.metric1, to_metric=self.metric2)
        
        start_date = date(2022, 1, 1)
        for i in range(100):
            HistoricalData.objects.create(
                metric=self.metric1,
                date=start_date + timedelta(days=i),
                value=random.uniform(90, 110)
            )

    def test_metric_visualization(self):
        url = reverse('visualize-metric', kwargs={'metric_id': self.metric1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('metric', response.data)
        self.assertIn('visualization', response.data)

    def test_connections_visualization(self):
        url = reverse('visualize-connections')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('connections', response.data)