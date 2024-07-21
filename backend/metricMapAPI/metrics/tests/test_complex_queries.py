# tests/test_complex_queries.py
from .test_utils import MetricsTestCase
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, Category

class ComplexQueryTests(MetricsTestCase):
    def setUp(self):
        super().setUp()
        self.category1 = Category.objects.create(name='Category 1', project=self.tenant)
        self.category2 = Category.objects.create(name='Category 2', project=self.tenant)
        
        for i in range(20):
            Metric.objects.create(
                name=f'Metric {i}',
                type='KPI' if i % 2 == 0 else 'Input Metric',
                category=self.category1 if i % 2 == 0 else self.category2,
                project=self.tenant
            )

    def test_filtering(self):
        url = reverse('metric-list')
        response = self.client.get(url, {'type': 'KPI'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

    def test_pagination(self):
        url = reverse('metric-list')
        response = self.client.get(url, {'page': 1, 'page_size': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)
        self.assertIsNotNone(response.data['next'])

    def test_ordering(self):
        url = reverse('metric-list')
        response = self.client.get(url, {'ordering': '-name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Metric 9')

    def test_complex_filtering(self):
        url = reverse('metric-list')
        response = self.client.get(url, {'type': 'KPI', 'category': self.category1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)