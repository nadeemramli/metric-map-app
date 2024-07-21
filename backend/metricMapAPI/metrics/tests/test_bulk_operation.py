# tests/test_views/test_bulk_operations.py
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric
import time
from .test_utils import MetricsTestCase

class BulkOperationsTests(MetricsTestCase):
    def setUp(self):
        self.url = reverse('metric-bulk-create')

    def test_bulk_create(self):
        data = [
            {'name': f'Bulk Metric {i}', 'type': 'KPI'} for i in range(100)
        ]
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Metric.objects.count(), 100)

    def test_bulk_create_performance(self):
        data = [
            {'name': f'Bulk Metric {i}', 'type': 'KPI'} for i in range(1000)
        ]
        start_time = time.time()
        response = self.client.post(self.url, data, format='json')
        end_time = time.time()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertLess(end_time - start_time, 5)  # Assert it takes less than 5 seconds