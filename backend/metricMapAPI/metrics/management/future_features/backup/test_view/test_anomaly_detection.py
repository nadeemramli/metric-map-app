from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, HistoricalData
from datetime import date, timedelta
import random
from django.core.cache import cache
from .test_utils import MetricsTestCase


class AnomalyDetectionTests(MetricsTestCase):
    def setUp(self):
        self.metric = Metric.objects.create(name='Test Metric', type='KPI')
        
        # Create dummy data
        start_date = date(2023, 1, 1)
        for i in range(100):
            HistoricalData.objects.create(
                metric=self.metric,
                date=start_date + timedelta(days=i),
                value=random.normalvariate(100, 10)  # Normal distribution
            )
        
        # Add an anomaly
        HistoricalData.objects.create(
            metric=self.metric,
            date=start_date + timedelta(days=50),
            value=200  # This should be detected as an anomaly
        )
        
        cache.clear()

    def test_anomaly_detection(self):
        url = reverse('anomaly-detection', kwargs={'metric_id': self.metric.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('anomalies', response.data)
        self.assertEqual(len(response.data['anomalies']), 1)  # We expect one anomaly
    
    def test_nonexistent_metric(self):
        url = reverse('anomaly-detection', kwargs={'metric_id': 9999})  # Non-existent ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_metric_without_data(self):
        empty_metric = Metric.objects.create(name='Empty Metric', type='KPI')
        url = reverse('anomaly-detection', kwargs={'metric_id': empty_metric.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)