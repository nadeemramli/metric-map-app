from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from metrics.models import Client, Project, Metric, Category, Tag, HistoricalData, Dashboard, Report, Experiment
from django.contrib.auth import get_user_model

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_client_operations(self):
        # Create a client
        response = self.client.post(reverse('client-list'), {"name": "Test Client"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client_id = response.data['id']
        self.assertIsNotNone(client_id)

        # Get client details
        response = self.client.get(reverse('client-detail', args=[client_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Client")

        # Update client
        response = self.client.put(reverse('client-detail', args=[client_id]), {"name": "Updated Client"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Client")

        # Delete client
        response = self.client.delete(reverse('client-detail', args=[client_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_project_operations(self):
        # Create a client first
        client = Client.objects.create(name="Test Client")

        # Create a project
        response = self.client.post(reverse('project-list', args=[client.id]), {"name": "Test Project"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        project_id = response.data['id']
        self.assertIsNotNone(project_id)

        # Get project details
        response = self.client.get(reverse('project-detail', args=[client.id, project_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Project")

        # Update project
        response = self.client.put(reverse('project-detail', args=[client.id, project_id]), {"name": "Updated Project"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Project")

        # Delete project
        response = self.client.delete(reverse('project-detail', args=[client.id, project_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_metric_operations(self):
        # Create a client and project first
        client = Client.objects.create(name="Test Client")
        project = Project.objects.create(name="Test Project", client=client)

        # Create a metric
        response = self.client.post(reverse('metric-list', args=[client.id, project.id]), {
            "name": "Test Metric",
            "type": "KPI",
            "value_type": "numeric"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        metric_id = response.data['id']
        self.assertIsNotNone(metric_id)

        # Get metric details
        response = self.client.get(reverse('metric-detail', args=[client.id, project.id, metric_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Metric")

        # Update metric
        response = self.client.put(reverse('metric-detail', args=[client.id, project.id, metric_id]), {
            "name": "Updated Metric",
            "type": "KPI",
            "value_type": "numeric"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Metric")

        # Delete metric
        response = self.client.delete(reverse('metric-detail', args=[client.id, project.id, metric_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Add more test methods for other endpoints (categories, tags, historical data, etc.)