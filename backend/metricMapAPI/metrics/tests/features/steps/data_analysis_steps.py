# features/steps/data_analysis_steps.py

from behave import given, when, then
from metrics.models import Metric, Project
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@given('a logged-in user in the "{project_name}" project with historical data')
def step_impl(context, project_name):
    context.user = User.objects.create_user(username='testuser', password='testpass')
    context.client = APIClient()
    context.client.force_authenticate(user=context.user)
    context.project = Project.objects.create(name=project_name)
    # Assume historical data is already generated

@when('the user views the "{metric_name}" metric')
def step_impl(context, metric_name):
    metric = Metric.objects.get(name=metric_name, project=context.project)
    context.response = context.client.get(f'/api/metrics/{metric.id}/analysis/')

@then('the system should display the "{metric_name}" trend over time')
def step_impl(context, metric_name):
    assert context.response.status_code == 200
    assert 'trend' in context.response.data
    assert len(context.response.data['trend']) > 0

@then('the system should highlight any anomalies in "{metric_name}"')
def step_impl(context, metric_name):
    assert 'anomalies' in context.response.data

@when('the user compares "{metric1}" with "{metric2}"')
def step_impl(context, metric1, metric2):
    metric1_obj = Metric.objects.get(name=metric1, project=context.project)
    metric2_obj = Metric.objects.get(name=metric2, project=context.project)
    context.response = context.client.get(f'/api/metrics/compare/?metric1={metric1_obj.id}&metric2={metric2_obj.id}')

@then('the system should show the correlation between "{metric1}" and "{metric2}"')
def step_impl(context, metric1, metric2):
    assert context.response.status_code == 200
    assert 'correlation' in context.response.data
    assert -1 <= context.response.data['correlation'] <= 1

@then('provide insights on how changes in "{metric1}" affect "{metric2}"')
def step_impl(context, metric1, metric2):
    assert 'insights' in context.response.data
    assert len(context.response.data['insights']) > 0

@when('the user runs a what-if scenario decreasing "{metric_name}" by {percentage:d}%')
def step_impl(context, metric_name, percentage):
    metric = Metric.objects.get(name=metric_name, project=context.project)
    context.response = context.client.post(f'/api/metrics/{metric.id}/what-if/', {
        'change': -percentage,
        'metric_id': metric.id
    })

@then('the system should simulate the impact on "{metric1}" and "{metric2}"')
def step_impl(context, metric1, metric2):
    assert context.response.status_code == 200
    assert 'impact' in context.response.data
    assert metric1 in context.response.data['impact']
    assert metric2 in context.response.data['impact']