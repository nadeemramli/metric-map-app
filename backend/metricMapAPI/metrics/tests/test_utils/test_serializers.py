# tests/test_serializers.py
from .test_utils import MetricsTestCase
from metrics.models import Category, Tag, Metric
from metrics.serializers import MetricSerializer, CategorySerializer, TagSerializer

class SerializerTests(MetricsTestCase):
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

    def test_metric_serializer(self):
        serializer = MetricSerializer(instance=self.metric)
        self.assertEqual(serializer.data['name'], 'Test Metric')
        self.assertEqual(serializer.data['type'], 'KPI')
        self.assertEqual(serializer.data['category'], self.category.id)
        self.assertIn(self.tag.id, serializer.data['tags'])

    def test_category_serializer(self):
        serializer = CategorySerializer(instance=self.category)
        self.assertEqual(serializer.data['name'], 'Test Category')
        self.assertEqual(serializer.data['project'], self.tenant.id)

    def test_tag_serializer(self):
        serializer = TagSerializer(instance=self.tag)
        self.assertEqual(serializer.data['name'], 'Test Tag')
        self.assertEqual(serializer.data['project'], self.tenant.id)

    # Add more serializer tests...