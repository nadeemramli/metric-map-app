# tests/test_edge_cases.py
from .test_utils import MetricsTestCase
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric

class EdgeCaseTests(MetricsTestCase):
    def setUp(self):
        super().setUp()

    def test_invalid_data_submission(self):
        url = reverse('metric-list')
        data = {
            'name': '',  # Empty name should be invalid
            'type': 'INVALID_TYPE',
            'project': self.tenant.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_large_payload(self):
        url = reverse('metric-list')
        data = {
            'name': 'A' * 1000,  # Assuming there's a max length for name
            'type': 'KPI',
            'project': self.tenant.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_boundary_conditions(self):
        url = reverse('metric-list')
        data = {
            'name': 'A' * 100,  # Assuming max length is 100
            'type': 'KPI',
            'project': self.tenant.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data['name'] = 'A' * 101  # Exceeding max length by 1
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)