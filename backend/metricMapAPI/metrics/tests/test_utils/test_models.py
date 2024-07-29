# tests/test_models.py
from .test_utils import MetricsTestCase
from metrics.models import Category, Tag, Metric, Connection, HistoricalData, Target, ActionRemark, Dashboard, Report

class ModelTests(MetricsTestCase):
    def test_project_creation(self):
        self.assertEqual(self.tenant.name, 'Test Project')

    def test_category_creation(self):
        category = Category.objects.create(name='Test Category', project=self.tenant)
        self.assertEqual(category.name, 'Test Category')
        self.assertEqual(category.project, self.tenant)

    def test_tag_creation(self):
        tag = Tag.objects.create(name='Test Tag', project=self.tenant)
        self.assertEqual(tag.name, 'Test Tag')
        self.assertEqual(tag.project, self.tenant)

    def test_metric_creation(self):
        category = Category.objects.create(name='Test Category', project=self.tenant)
        metric = Metric.objects.create(
            name='Test Metric',
            type='KPI',
            category=category,
            project=self.tenant
        )
        self.assertEqual(metric.name, 'Test Metric')
        self.assertEqual(metric.type, 'KPI')
        self.assertEqual(metric.category, category)
        self.assertEqual(metric.project, self.tenant)

    # Add more tests for other models...