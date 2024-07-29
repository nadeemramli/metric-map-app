# tests/test_data_integrity.py
from .test_utils import MetricsTestCase
from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, Category, Tag

class DataIntegrityTests(MetricsTestCase):
    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(name='Test Category', project=self.tenant)
        self.tag = Tag.objects.create(name='Test Tag', project=self.tenant)
        self.metric = Metric.objects.create(
            name='Test Metric',
            type='KPI',
            category=self.category,
            project=self.tenant
        )
        self.metric.tags.add(self.tag)

    def test_cascading_delete(self):
        self.category.delete()
        with self.assertRaises(Metric.DoesNotExist):
            Metric.objects.get(id=self.metric.id)

    def test_related_objects_creation(self):
        url = reverse('metric-list')
        data = {
            'name': 'New Metric',
            'type': 'KPI',
            'category': self.category.id,
            'tags': [self.tag.id],
            'project': self.tenant.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        new_metric = Metric.objects.get(name='New Metric')
        self.assertEqual(new_metric.category, self.category)
        self.assertIn(self.tag, new_metric.tags.all())