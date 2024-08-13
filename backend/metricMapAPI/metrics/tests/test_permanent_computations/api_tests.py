from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from .factories import *
from metrics.models import *
from rest_framework.authtoken.models import Token
from ..test_utils import MetricsTestCase
import logging
from django.db import connection
from django.utils.dateparse import parse_date

logger = logging.getLogger(__name__)

class APITestCase(MetricsTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        logger.info("Setting up API test case")

    def setUp(self):
        super().setUp()
        logger.info("Setting up API test")
        self.project = ProjectFactory(tenant=self.tenant_client)
        self.project.save()
        self.user = CustomUserFactory(tenant=self.tenant_client)
        self.user.save()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_object_creation(self):
        self.assertIsNotNone(self.tenant_client.id)
        self.assertIsNotNone(self.project.id)
        self.assertIsNotNone(self.user.id)

        # Verify objects can be retrieved from the database
        retrieved_tenant = Client.objects.get(id=self.tenant_client.id)
        retrieved_project = Project.objects.get(id=self.project.id)
        retrieved_user = get_user_model().objects.get(id=self.user.id)

        self.assertEqual(retrieved_tenant.name, self.tenant_client.name)
        self.assertEqual(retrieved_project.name, self.project.name)
        self.assertEqual(retrieved_user.username, self.user.username)

    def test_client_operations(self):
        # Create a client
        client_data = ClientFactory.build(name="Test Client", schema_name="test-client")
        post_data = {
            "name": client_data.name,
            "schema_name": client_data.schema_name
        }
        response = self.client.post(reverse('client-list'), post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client_id = response.data['id']
        self.assertIsNotNone(client_id)

        # Verify client creation in database
        created_client = Client.objects.get(id=client_id)
        self.assertEqual(created_client.name, post_data['name'])
        self.assertEqual(created_client.schema_name, post_data['schema_name'])

        # Get client details
        response = self.client.get(reverse('client-detail', args=[client_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], post_data['name'])
        self.assertEqual(response.data['schema_name'], post_data['schema_name'])

        # Update client
        update_data = {
            "name": "Updated Client",
            "schema_name": "updated-client"
        }
        response = self.client.put(reverse('client-detail', args=[client_id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_data['name'])
        self.assertEqual(response.data['schema_name'], update_data['schema_name'])

        # Verify client update in database
        updated_client = Client.objects.get(id=client_id)
        self.assertEqual(updated_client.name, update_data['name'])
        self.assertEqual(updated_client.schema_name, update_data['schema_name'])

        # Delete client
        response = self.client.delete(reverse('client-detail', args=[client_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify client deletion in database
        with self.assertRaises(Client.DoesNotExist):
            Client.objects.get(id=client_id)

        # Attempt to get deleted client (should return 404)
        response = self.client.get(reverse('client-detail', args=[client_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_project_operations(self):
        # Create a project
        project_data = ProjectFactory.build(tenant=self.tenant_client)
        post_data = {
            "name": project_data.name,
        }

        # Create project
        response = self.client.post(reverse('client-projects-list', args=[self.tenant_client.id]), post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        project_id = response.data['id']
        self.assertIsNotNone(project_id)

        # Verify project creation in database
        created_project = Project.objects.get(id=project_id)
        self.assertEqual(created_project.name, post_data['name'])
        self.assertEqual(created_project.description, post_data['description'])
        self.assertEqual(created_project.start_date, parse_date(post_data['start_date']))
        self.assertEqual(created_project.end_date, parse_date(post_data['end_date']))
        self.assertEqual(created_project.status, post_data['status'])
        self.assertEqual(created_project.tenant_id, self.tenant_client.id)

        # Get project details
        response = self.client.get(reverse('client-projects-detail', args=[self.tenant_client.id, project_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], post_data['name'])
        self.assertEqual(response.data['description'], post_data['description'])
        self.assertEqual(parse_date(response.data['start_date']), parse_date(post_data['start_date']))
        self.assertEqual(parse_date(response.data['end_date']), parse_date(post_data['end_date']))
        self.assertEqual(response.data['status'], post_data['status'])

        # Update project
        update_data = {
            "name": "Updated Project",
        }
        response = self.client.put(reverse('client-projects-detail', args=[self.tenant_client.id, project_id]), update_data)
        self.assertEqual(response.data['name'], update_data['name'])
        self.assertEqual(response.data['description'], update_data['description'])
        self.assertEqual(parse_date(response.data['start_date']), parse_date(update_data['start_date']))
        self.assertEqual(parse_date(response.data['end_date']), parse_date(update_data['end_date']))
        self.assertEqual(response.data['status'], update_data['status'])

        # Verify project update in database
        updated_project = Project.objects.get(id=project_id)
        self.assertEqual(updated_project.name, update_data['name'])
        self.assertEqual(updated_project.description, update_data['description'])
        self.assertEqual(updated_project.start_date, parse_date(update_data['start_date']))
        self.assertEqual(updated_project.end_date, parse_date(update_data['end_date']))
        self.assertEqual(updated_project.status, update_data['status'])

        # Delete project
        response = self.client.delete(reverse('client-projects-detail', args=[self.tenant_client.id, project_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify project deletion in database
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(id=project_id)

        # Attempt to get deleted project (should return 404)
        response = self.client.get(reverse('client-projects-detail', args=[self.tenant_client.id, project_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_metric_operations(self):
        # Create metric data using Factory.build()
        metric_data = MetricFactory.build(project=self.project, tenant=self.tenant_client)
        post_data = {
            "name": metric_data.name,
            "project": self.project.id,
            "type": metric_data.type,
            "value_type": metric_data.value_type,
        }
        
        # Create a metric via API
        response = self.client.post(reverse('project-metrics-list', args=[self.tenant_client.id, self.project.id]), post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        metric_id = response.data['id']
        self.assertIsNotNone(metric_id)

        # Verify metric creation in database
        created_metric = Metric.objects.get(id=metric_id)
        self.assertEqual(created_metric.name, post_data['name'])
        self.assertEqual(created_metric.project_id, post_data['project'])
        self.assertEqual(created_metric.type, post_data['type'])
        self.assertEqual(created_metric.value_type, post_data['value_type'])
        self.assertEqual(created_metric.description, post_data['description'])
        self.assertEqual(created_metric.unit, post_data['unit'])
        self.assertEqual(created_metric.data_source, post_data['data_source'])
        self.assertEqual(created_metric.tenant_id, self.tenant_client.id)

        # Get metric details
        response = self.client.get(reverse('project-metrics-detail', args=[self.tenant_client.id, self.project.id, metric_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], post_data['name'])
        self.assertEqual(response.data['project'], post_data['project'])
        self.assertEqual(response.data['type'], post_data['type'])
        self.assertEqual(response.data['value_type'], post_data['value_type'])
        self.assertEqual(response.data['description'], post_data['description'])
        self.assertEqual(response.data['unit'], post_data['unit'])
        self.assertEqual(response.data['data_source'], post_data['data_source'])

        # Update metric
        updated_data = MetricFactory.build(project=self.project, tenant=self.tenant_client)
        update_post_data = {
            "name": updated_data.name,
            "project": self.project.id,
            "type": updated_data.type,
            "value_type": updated_data.value_type,
        }
        response = self.client.put(reverse('project-metrics-detail', args=[self.tenant_client.id, self.project.id, metric_id]), update_post_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_post_data['name'])
        self.assertEqual(response.data['type'], update_post_data['type'])
        self.assertEqual(response.data['value_type'], update_post_data['value_type'])
        self.assertEqual(response.data['description'], update_post_data['description'])
        self.assertEqual(response.data['unit'], update_post_data['unit'])
        self.assertEqual(response.data['data_source'], update_post_data['data_source'])

        # Verify metric update in database
        updated_metric = Metric.objects.get(id=metric_id)
        self.assertEqual(updated_metric.name, update_post_data['name'])
        self.assertEqual(updated_metric.type, update_post_data['type'])
        self.assertEqual(updated_metric.value_type, update_post_data['value_type'])
        self.assertEqual(updated_metric.description, update_post_data['description'])
        self.assertEqual(updated_metric.unit, update_post_data['unit'])
        self.assertEqual(updated_metric.data_source, update_post_data['data_source'])

        # Delete metric
        response = self.client.delete(reverse('project-metrics-detail', args=[self.tenant_client.id, self.project.id, metric_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify metric deletion in database
        with self.assertRaises(Metric.DoesNotExist):
            Metric.objects.get(id=metric_id)

        # Attempt to get deleted metric (should return 404)
        response = self.client.get(reverse('project-metrics-detail', args=[self.tenant_client.id, self.project.id, metric_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_category_operations(self):
        # Create category data using Factory.build()
        category_data = CategoryFactory.build(project=self.project, tenant=self.tenant_client)
        post_data = {"name": category_data.name, "project": self.project.id}
        
        # Create a category via API
        response = self.client.post(reverse('project-categories-list', args=[self.tenant_client.id, self.project.id]), post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        category_id = response.data['id']
        self.assertIsNotNone(category_id)

        # Get category details
        response = self.client.get(reverse('project-categories-detail', args=[self.tenant_client.id, self.project.id, category_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], post_data["name"])

        # Update category
        updated_data = CategoryFactory.build(project=self.project, tenant=self.tenant_client)
        update_post_data = {"name": updated_data.name, "project": self.project.id}
        response = self.client.put(reverse('project-categories-detail', args=[self.tenant_client.id, self.project.id, category_id]), update_post_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_post_data["name"])

        # Delete category
        response = self.client.delete(reverse('project-categories-detail', args=[self.tenant_client.id, self.project.id, category_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Update other test methods similarly...

    def test_tag_operations(self):
        # Create tag data using Factory.build()
        tag_data = TagFactory.build(project=self.project, tenant=self.tenant_client)
        post_data = {"name": tag_data.name, "project": self.project.id}
        
        # Create a tag via API
        response = self.client.post(reverse('project-tags-list', args=[self.tenant_client.id, self.project.id]), post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tag_id = response.data['id']
        self.assertIsNotNone(tag_id)

        # Get tag details
        response = self.client.get(reverse('project-tags-detail', args=[self.tenant_client.id, self.project.id, tag_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], post_data["name"])

        # Update tag
        updated_data = TagFactory.build(project=self.project, tenant=self.tenant_client)
        update_post_data = {"name": updated_data.name, "project": self.project.id}
        response = self.client.put(reverse('project-tags-detail', args=[self.tenant_client.id, self.project.id, tag_id]), update_post_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_post_data["name"])

        # Delete tag
        response = self.client.delete(reverse('project-tags-detail', args=[self.tenant_client.id, self.project.id, tag_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_historical_data_operations(self):
        metric = MetricFactory(project=self.project, tenant=self.tenant_client)
        historical_data = HistoricalDataFactory.build(metric=metric)
        post_data = {
            "date": historical_data.date,
            "value": historical_data.value,
            "metric": metric.id
        }

        # Create historical data
        response = self.client.post(reverse('metric-historical-data-list', args=[self.tenant_client.id, self.project.id, metric.id]), post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        historical_data_id = response.data['id']
        self.assertIsNotNone(historical_data_id)

        # Get historical data details
        response = self.client.get(reverse('metric-historical-data-detail', args=[self.tenant_client.id, self.project.id, metric.id, historical_data_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['value'], str(historical_data.value))

        # Update historical data
        response = self.client.put(reverse('metric-historical-data-detail', args=[self.tenant_client.id, self.project.id, metric.id, historical_data_id]), {
            "date": historical_data.date,
            "value": 100
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['value'], '100')

        # Delete historical data
        response = self.client.delete(reverse('metric-historical-data-detail', args=[self.tenant_client.id, self.project.id, metric.id, historical_data_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_dashboard_operations(self):
        dashboard_data = DashboardFactory.build(project=self.project, tenant=self.tenant_client)
        post_data = {
            "name": dashboard_data.name,
            "layout": dashboard_data.layout,
            "project": self.project.id
        }

        # Create dashboard
        response = self.client.post(reverse('project-dashboards-list', args=[self.tenant_client.id, self.project.id]), post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        dashboard_id = response.data['id']
        self.assertIsNotNone(dashboard_id)

        # Get dashboard details
        response = self.client.get(reverse('project-dashboards-detail', args=[self.tenant_client.id, self.project.id, dashboard_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], dashboard_data.name)

        # Update dashboard
        response = self.client.put(reverse('project-dashboards-detail', args=[self.tenant_client.id, self.project.id, dashboard_id]), {
            "name": "Updated Dashboard",
            "layout": dashboard_data.layout
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Dashboard")

        # Delete dashboard
        response = self.client.delete(reverse('project-dashboards-detail', args=[self.tenant_client.id, self.project.id, dashboard_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_report_operations(self):
        report_data = ReportFactory.build(project=self.project, tenant=self.tenant_client)
        post_data = {
            "name": report_data.name,
            "configuration": report_data.configuration,
            "project": self.project.id
        }

        # Create report
        response = self.client.post(reverse('project-reports-list', args=[self.tenant_client.id, self.project.id]), post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        report_id = response.data['id']
        self.assertIsNotNone(report_id)

        # Get report details
        response = self.client.get(reverse('project-reports-detail', args=[self.tenant_client.id, self.project.id, report_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], report_data.name)

        # Update report
        response = self.client.put(reverse('project-reports-detail', args=[self.tenant_client.id, self.project.id, report_id]), {
            "name": "Updated Report",
            "configuration": report_data.configuration
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Report")

        # Delete report
        response = self.client.delete(reverse('project-reports-detail', args=[self.tenant_client.id, self.project.id, report_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_experiment_operations(self):
        experiment_data = ExperimentFactory.build(project=self.project, tenant=self.tenant_client)
        post_data = {
            "name": experiment_data.name,
            "description": experiment_data.description,
            "start_date": experiment_data.start_date,
            "end_date": experiment_data.end_date,
            "status": experiment_data.status,
            "project": self.project.id
        }

        # Create experiment
        response = self.client.post(reverse('project-experiments-list', args=[self.tenant_client.id, self.project.id]), post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        experiment_id = response.data['id']
        self.assertIsNotNone(experiment_id)

        # Verify experiment creation in database
        created_experiment = Experiment.objects.get(id=experiment_id)
        self.assertEqual(created_experiment.name, post_data['name'])
        self.assertEqual(created_experiment.description, post_data['description'])
        self.assertEqual(created_experiment.start_date, parse_date(post_data['start_date']))
        self.assertEqual(created_experiment.end_date, parse_date(post_data['end_date']))
        self.assertEqual(created_experiment.status, post_data['status'])
        self.assertEqual(created_experiment.project_id, post_data['project'])
        self.assertEqual(created_experiment.tenant_id, self.tenant_client.id)

        # Get experiment details
        response = self.client.get(reverse('project-experiments-detail', args=[self.tenant_client.id, self.project.id, experiment_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], post_data['name'])
        self.assertEqual(response.data['description'], post_data['description'])
        self.assertEqual(parse_date(response.data['start_date']), parse_date(post_data['start_date']))
        self.assertEqual(parse_date(response.data['end_date']), parse_date(post_data['end_date']))
        self.assertEqual(response.data['status'], post_data['status'])
        self.assertEqual(response.data['project'], post_data['project'])

        # Update experiment
        update_data = {
            "name": "Updated Experiment",
            "description": "Updated description",
            "start_date": experiment_data.start_date + timedelta(days=1),
            "end_date": experiment_data.end_date + timedelta(days=1),
            "status": "completed"
        }
        response = self.client.put(reverse('project-experiments-detail', args=[self.tenant_client.id, self.project.id, experiment_id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_data['name'])
        self.assertEqual(response.data['description'], update_data['description'])
        self.assertEqual(parse_date(response.data['start_date']), parse_date(update_data['start_date']))
        self.assertEqual(parse_date(response.data['end_date']), parse_date(update_data['end_date']))
        self.assertEqual(response.data['status'], update_data['status'])

        # Verify experiment update in database
        updated_experiment = Experiment.objects.get(id=experiment_id)
        self.assertEqual(updated_experiment.name, update_data['name'])
        self.assertEqual(updated_experiment.description, update_data['description'])
        self.assertEqual(updated_experiment.start_date, parse_date(update_data['start_date']))
        self.assertEqual(updated_experiment.end_date, parse_date(update_data['end_date']))
        self.assertEqual(updated_experiment.status, update_data['status'])

        # Delete experiment
        response = self.client.delete(reverse('project-experiments-detail', args=[self.tenant_client.id, self.project.id, experiment_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify experiment deletion in database
        with self.assertRaises(Experiment.DoesNotExist):
            Experiment.objects.get(id=experiment_id)

        # Attempt to get deleted experiment (should return 404)
        response = self.client.get(reverse('project-experiments-detail', args=[self.tenant_client.id, self.project.id, experiment_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def tearDown(self):
        # Clean up created data
        HistoricalData.objects.filter(tenant=self.tenant_client).delete()
        Metric.objects.filter(tenant=self.tenant_client).delete()
        Project.objects.filter(tenant=self.tenant_client).delete()
        Category.objects.filter(tenant=self.tenant_client).delete()
        Tag.objects.filter(tenant=self.tenant_client).delete()
        Dashboard.objects.filter(tenant=self.tenant_client).delete()
        Report.objects.filter(tenant=self.tenant_client).delete()
        Experiment.objects.filter(tenant=self.tenant_client).delete()
        self.user.delete()
        super().tearDown()

    @classmethod
    def tearDownClass(cls):
        # Ensure we're in the public schema before deleting the tenant
        connection.set_schema_to_public()
        super().tearDownClass()