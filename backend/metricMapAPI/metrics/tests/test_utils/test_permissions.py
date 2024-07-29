# tests/test_permissions.py
from .test_utils import MetricsTestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User, Group
from metrics.models import Metric

class PermissionTests(MetricsTestCase):
    def setUp(self):
        super().setUp()
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        
        self.metric = Metric.objects.create(name='Test Metric', type='KPI', project=self.tenant)

    def test_user_can_view_own_metrics(self):
        self.client.force_login(self.user1)
        url = reverse('metric-detail', kwargs={'pk': self.metric.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_edit_other_user_metrics(self):
        self.client.force_login(self.user2)
        url = reverse('metric-detail', kwargs={'pk': self.metric.id})
        data = {'name': 'Updated Metric'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_edit_all_metrics(self):
        self.client.force_login(self.admin_user)
        url = reverse('metric-detail', kwargs={'pk': self.metric.id})
        data = {'name': 'Updated by Admin'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)