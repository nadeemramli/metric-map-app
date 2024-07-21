from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, Category, HistoricalData
from datetime import date, timedelta
import random
from django.core.cache import cache
from .test_utils import MetricsTestCase


class AggregatedViewsTests(MetricsTestCase):
    def setUp(self):
        self.metric = Metric.objects.create(name='Test Metric', type='KPI')
        
        # Create dummy data
        start_date = date(2022, 1, 1)
        for i in range(730):  # Two years of data
            HistoricalData.objects.create(
                metric=self.metric,
                date=start_date + timedelta(days=i),
                value=random.uniform(80, 120)
            )
        
        cache.clear()

    def test_aggregated_views(self):
        url = reverse('aggregated-views', kwargs={'metric_id': self.metric.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('monthly_aggregation', response.data)
        self.assertIn('yearly_aggregation', response.data)
        self.assertEqual(len(response.data['monthly_aggregation']), 24)  # 24 months
        self.assertEqual(len(response.data['yearly_aggregation']), 2)   # 2 years
    
    def test_caching(self):
        url = reverse('aggregated-views', kwargs={'metric_id': self.metric.id})
        
        # First request
        response1 = self.client.get(url)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        
        # Modify data
        HistoricalData.objects.create(
            metric=self.metric,
            date=date(2023, 7, 1),
            value=150
        )
        
        # Second request (should be cached)
        response2 = self.client.get(url)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response1.data, response2.data)  # Data