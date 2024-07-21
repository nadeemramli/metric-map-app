# tests/test_views.py
from .test_utils import MetricsTestCase
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, Category

class ViewTests(MetricsTestCase):
    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(name='Test Category', project=self.tenant)
        self.metric = Metric.objects.create(
            name='Test Metric',
            type='KPI',
            category=self.category,
            project=self.tenant
        )

    def test_metric_list_view(self):
        url = reverse('metric-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Metric')

    def test_metric_detail_view(self):
        url = reverse('metric-detail', kwargs={'pk': self.metric.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Metric')



