from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, HistoricalData
from .test_utils import MetricsTestCase


class ActionRemarksTests(MetricsTestCase):
    def setUp(self):
        self.metric = Metric.objects.create(name='Test Metric', type='KPI')
        self.url = reverse('action-remarks', kwargs={'metric_id': self.metric.id})

    def test_create_action_remark(self):
        data = {
            'date': '2023-01-01',
            'description': 'Test remark',
            'impact': 'High'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_action_remarks(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)