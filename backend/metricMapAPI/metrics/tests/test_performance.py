# tests/test_performance.py
import time
from .test_utils import MetricsTestCase
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric

class PerformanceTests(MetricsTestCase):
    def setUp(self):
        super().setUp()
        for i in range(1000):
            Metric.objects.create(name=f'Metric {i}', type='KPI', project=self.tenant)

    def test_list_response_time(self):
        url = reverse('metric-list')
        start_time = time.time()
        response = self.client.get(url)
        end_time = time.time()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end_time - start_time, 1.0)  # Assert response time is less than 1 second

    def test_bulk_create(self):
        url = reverse('metric-list')
        data = [{'name': f'Bulk Metric {i}', 'type': 'KPI', 'project': self.tenant.id} for i in range(100)]
        
        start_time = time.time()
        response = self.client.post(url, data, format='json')
        end_time = time.time()
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertLess(end_time - start_time, 5.0)  # Assert bulk creation takes less than 5 seconds