# tests/test_views.py

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from metrics.models import Metric, Project  # Import your models

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def sample_project(db):
    return Project.objects.create(name="Test Project")

@pytest.fixture
def sample_metric(db, sample_project):
    return Metric.objects.create(name="Test Metric", project=sample_project)

@pytest.mark.django_db
def test_list_metrics(api_client, sample_metric):
    url = reverse('metric-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == "Test Metric"

@pytest.mark.django_db
def test_create_metric(api_client, sample_project):
    url = reverse('metric-list')
    data = {
        'name': 'New Metric',
        'project': sample_project.id
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Metric.objects.count() == 1
    assert Metric.objects.get().name == 'New Metric'

# Add more tests for other views and endpoints