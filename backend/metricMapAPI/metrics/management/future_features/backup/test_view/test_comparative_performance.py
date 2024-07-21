from django.urls import reverse
from rest_framework import status
from metrics.models import Metric, HistoricalData
from .test_utils import MetricsTestCase


class ComparativePerformanceTests(MetricsTestCase):
    def setUp(self):
        self.metric1 = Metric.objects.create(name='Metric 1', type='KPI')
        self.metric2 = Metric.objects.create(name='Metric 2', type='KPI')
        start_date = date(2023, 1, 1)
        for i in range(30):
            HistoricalData.objects.create(
                metric=self.metric1,
                date=start_date + timedelta(days=i),
                value=random.uniform(90, 110)
            )
            HistoricalData.objects.create(
                metric=self.metric2,
                date=start_date + timedelta(days=i),
                value=random.uniform(190, 210)
            )

    def test_comparative_performance(self):
        url = reverse('comparative-performance')
        response = self.client.get(url, {'metric_ids': f'{self.metric1.id},{self.metric2.id}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.metric1.name, response.data)
        self.assertIn(self.metric2.name, response.data)