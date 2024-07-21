# features/steps/metric_management_steps.py

from behave import given, when, then
from metrics.models import Metric, Category, Tag, Target, HistoricalData, Connection, Project
from django.contrib.auth.models import User
from rest_framework.test import APIClient
import json
from datetime import datetime, timedelta

@given('a logged-in user in the "{project_name}" project')
def step_impl(context, project_name):
    context.user = User.objects.create_user(username='testuser', password='testpass')
    context.client = APIClient()
    context.client.force_authenticate(user=context.user)
    context.project = Project.objects.create(name=project_name)

@when('the user creates a new metric "{metric_name}" of type "{metric_type}" with value type "{value_type}"')
def step_impl(context, metric_name, metric_type, value_type):
    context.response = context.client.post('/api/metrics/', {
        'name': metric_name,
        'type': metric_type,
        'value_type': value_type,
        'project': context.project.id
    })

@then('the metric "{metric_name}" should be saved successfully')
def step_impl(context, metric_name):
    assert context.response.status_code == 201
    assert Metric.objects.filter(name=metric_name, project=context.project).exists()

@when('the user creates a category "{category_name}" and assigns "{metric_name}" to it')
def step_impl(context, category_name, metric_name):
    category = Category.objects.create(name=category_name, project=context.project)
    metric = Metric.objects.get(name=metric_name, project=context.project)
    context.response = context.client.patch(f'/api/metrics/{metric.id}/', {
        'category': category.id
    })

@then('the category assignment should be saved successfully')
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.data['category'] is not None

@when('the user adds a tag "{tag_name}" to the "{metric_name}" metric')
def step_impl(context, tag_name, metric_name):
    metric = Metric.objects.get(name=metric_name, project=context.project)
    context.response = context.client.post('/api/tags/', {
        'name': tag_name,
        'project': context.project.id,
        'metrics': [metric.id]
    })

@then('the tag should be saved and associated with "{metric_name}"')
def step_impl(context, metric_name):
    assert context.response.status_code == 201
    metric = Metric.objects.get(name=metric_name, project=context.project)
    assert Tag.objects.filter(name=context.response.data['name'], metrics=metric).exists()

@when('the user sets a target of {target_value:d} for "{metric_name}" to be achieved by "{target_date}"')
def step_impl(context, target_value, metric_name, target_date):
    metric = Metric.objects.get(name=metric_name, project=context.project)
    context.response = context.client.post('/api/targets/', {
        'metric': metric.id,
        'target_value': target_value,
        'target_date': target_date
    })

@then('the target should be saved successfully for "{metric_name}"')
def step_impl(context, metric_name):
    assert context.response.status_code == 201
    metric = Metric.objects.get(name=metric_name, project=context.project)
    assert Target.objects.filter(metric=metric).exists()

@when('the user inputs historical data for "{metric_name}" from "{start_date}" to "{end_date}"')
def step_impl(context, metric_name, start_date, end_date):
    metric = Metric.objects.get(name=metric_name, project=context.project)
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    data = []
    current = start
    while current <= end:
        data.append({
            'date': current.strftime("%Y-%m-%d"),
            'value': 100  # Example value
        })
        current += timedelta(days=1)
    
    context.response = context.client.post(f'/api/metrics/{metric.id}/historical-data/', data=json.dumps(data), content_type='application/json')

@then('the historical data should be saved successfully for "{metric_name}"')
def step_impl(context, metric_name):
    assert context.response.status_code == 201
    metric = Metric.objects.get(name=metric_name, project=context.project)
    assert HistoricalData.objects.filter(metric=metric).exists()

@when('the user defines a connection between "{metric1}" and "{metric2}" with correlation {correlation:f}')
def step_impl(context, metric1, metric2, correlation):
    metric1_obj = Metric.objects.get(name=metric1, project=context.project)
    metric2_obj = Metric.objects.get(name=metric2, project=context.project)
    context.response = context.client.post('/api/connections/', {
        'from_metric': metric1_obj.id,
        'to_metric': metric2_obj.id,
        'correlation_coefficient': correlation
    })

@then('the connection should be saved successfully')
def step_impl(context):
    assert context.response.status_code == 201
    assert Connection.objects.filter(id=context.response.data['id']).exists()

@when('the user creates the following metrics')
def step_impl(context):
    for row in context.table:
        context.response = context.client.post('/api/metrics/', {
            'name': row['name'],
            'type': row['type'],
            'value_type': row['value_type'],
            'project': context.project.id
        })

@then('all metrics should be saved successfully')
def step_impl(context):
    for row in context.table:
        assert Metric.objects.filter(name=row['name'], project=context.project).exists()