from django.db import connection
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from ..models import (
    Client, Domain, Project, Metric, Category, Tag, 
    Connection, HistoricalData, Dashboard, Experiment, 
    Target, Report, ActionRemark
)
from ..serializers import MetricSerializer, ProjectSerializer
from .test_utils import MetricsTestCase, TenantAPIClient

class APITests(MetricsTestCase):
    def setUp(self):
        super().setUp()
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)

        self.project = Project.objects.create(name='Test Project', tenant=self.tenant_client)
        self.category = Category.objects.create(name='Test Category', tenant=self.tenant_client)
        self.tag = Tag.objects.create(name='Test Tag', project=self.project, tenant=self.tenant_client)
        self.metric = Metric.objects.create(
            name='Test Metric',
            type=Metric.Type.KPI,
            value_type=Metric.ValueType.COUNT,
            rhythm=Metric.Rhythm.DAILY,
            category=self.category,
            tenant=self.tenant_client
        )
        self.metric.tags.add(self.tag)

    def get_client_project_url(self, viewname, client_pk=None, project_pk=None, **kwargs):
        if client_pk is None:
            client_pk = self.tenant_client.pk
        if project_pk is None:
            project_pk = self.project.pk
        
        if viewname.startswith('client-'):
            return reverse(viewname, kwargs={'client__pk': client_pk, **kwargs})
        elif viewname.startswith('project-'):
            return reverse(viewname, kwargs={'client__pk': client_pk, 'project__pk': project_pk, **kwargs})
        elif viewname.startswith('metric-'):
            return reverse(viewname, kwargs={'client__pk': client_pk, 'project__pk': project_pk, 'metric__pk': kwargs.get('pk'), **kwargs})
        else:
            return reverse(viewname, kwargs=kwargs)

    def test_get_clients_list(self):
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_client_detail(self):
        url = reverse('client-detail', kwargs={'pk': self.tenant_client.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Client')

    def test_get_projects_list(self):
        url = self.get_client_project_url('client-projects-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_project_detail(self):
        url = self.get_client_project_url('client-projects-detail', pk=self.project.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Project')

    def test_get_metrics_list(self):
        url = self.get_client_project_url('project-metrics-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_metric_detail(self):
        url = self.get_client_project_url('project-metrics-detail', pk=self.metric.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Metric')

    def test_create_metric(self):
        url = self.get_client_project_url('project-metrics-list')
        data = {
            'name': 'New Metric',
            'type': Metric.Type.KPI,
            'value_type': Metric.ValueType.COUNT,
            'rhythm': Metric.Rhythm.DAILY,
            'category': self.category.id,
            'tags': [self.tag.id]
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Metric.objects.count(), 2)

    def test_update_metric(self):
        url = self.get_client_project_url('project-metrics-detail', pk=self.metric.pk)
        data = {
            'name': 'Updated Metric',
            'type': Metric.Type.KPI,
            'value_type': Metric.ValueType.COUNT,
            'rhythm': Metric.Rhythm.DAILY,
            'category': self.category.id,
            'tags': [self.tag.id]
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Metric.objects.get(id=self.metric.id).name, 'Updated Metric')

    def test_delete_metric(self):
        url = self.get_client_project_url('project-metrics-detail', pk=self.metric.pk)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Metric.objects.count(), 0)

    def test_get_historical_data(self):
        url = self.get_client_project_url('metric-historical-data', metric_pk=self.metric.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_metric_connections(self):
        url = self.get_client_project_url('project-connections-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_metric_action_remarks(self):
        url = self.get_client_project_url('metric-action-remarks-list', metric_pk=self.metric.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_action_remark(self):
        url = self.get_client_project_url('metric-action-remarks-list', metric_pk=self.metric.pk)
        data = {
            'description': 'Test Action Remark',
            'impact': 'Positive'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_metric_targets(self):
        url = self.get_client_project_url('project-targets-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_metric_reports(self):
        url = self.get_client_project_url('project-reports-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_dashboards(self):
        url = self.get_client_project_url('project-dashboards-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_dashboard(self):
        url = self.get_client_project_url('project-dashboards-list')
        data = {
            'name': 'Test Dashboard',
            'layout': {'layout': 'test_layout'}
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_experiments(self):
        url = self.get_client_project_url('project-experiments-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_experiment(self):
        url = self.get_client_project_url('project-experiments-list')
        data = {
            'name': 'Test Experiment',
            'description': 'Test Description',
            'start_date': '2023-01-01',
            'status': 'Ongoing'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_categories(self):
        url = self.get_client_project_url('project-categories-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tags(self):
        url = self.get_client_project_url('project-tags-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_connections(self):
        url = self.get_client_project_url('project-connections-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_targets(self):
        url = self.get_client_project_url('project-targets-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reports(self):
        url = self.get_client_project_url('project-reports-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_metric_serializer(self):
        serializer = MetricSerializer(instance=self.metric)
        data = serializer.data
        self.assertEqual(data['name'], 'Test Metric')
        self.assertEqual(data['type'], Metric.Type.KPI)
        self.assertEqual(data['value_type'], Metric.ValueType.COUNT)
        self.assertEqual(data['rhythm'], Metric.Rhythm.DAILY)
        self.assertEqual(data['category'], self.category.id)

    def test_project_serializer(self):
        serializer = ProjectSerializer(instance=self.project)
        data = serializer.data
        self.assertEqual(data['name'], 'Test Project')
        self.assertEqual(data['tenant'], self.tenant_client.id)

    def test_url_patterns(self):
        self.assertEqual(
            self.get_client_project_url('project-metrics-list'),
            f'/api/clients/{self.tenant_client.pk}/projects/{self.project.pk}/metrics/'
        )
        self.assertEqual(
            self.get_client_project_url('project-metrics-detail', pk=1),
            f'/api/clients/{self.tenant_client.pk}/projects/{self.project.pk}/metrics/1/'
        )
        self.assertEqual(
            self.get_client_project_url('project-dashboards-list'),
            f'/api/clients/{self.tenant_client.pk}/projects/{self.project.pk}/dashboards/'
        )
        self.assertEqual(
            self.get_client_project_url('project-experiments-list'),
            f'/api/clients/{self.tenant_client.pk}/projects/{self.project.pk}/experiments/'
        )

    def test_authentication_required(self):
        self.client.logout()
        url = self.get_client_project_url('project-metrics-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)