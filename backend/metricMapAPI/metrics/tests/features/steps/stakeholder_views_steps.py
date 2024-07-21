# features/steps/stakeholder_views_steps.py

from behave import given, when, then
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient
from metrics.models import Project, Metric, Dashboard

@given('a logged-in user with roles "{role1}" and "{role2}"')
def step_impl(context, role1, role2):
    context.user = User.objects.create_user(username='testuser', password='testpass')
    group1 = Group.objects.create(name=role1)
    group2 = Group.objects.create(name=role2)
    context.user.groups.add(group1, group2)
    context.client = APIClient()
    context.client.force_authenticate(user=context.user)

@given('a "{project_name}" project with historical data')
def step_impl(context, project_name):
    context.project = Project.objects.create(name=project_name)
    # Assume historical data is already generated

@when('the user views the dashboard as "{role}"')
def step_impl(context, role):
    context.response = context.client.get(f'/api/dashboards/?role={role}')

@then('the dashboard should show high-level KPIs across all projects')
def step_impl(context):
    assert context.response.status_code == 200
    assert 'high_level_kpis' in context.response.data
    assert len(context.response.data['high_level_kpis']) > 0

@then('highlight underperforming metrics')
def step_impl(context):
    assert 'underperforming_metrics' in context.response.data
    assert len(context.response.data['underperforming_metrics']) > 0

@when('the user switches to "{role}" role')
def step_impl(context, role):
    context.response = context.client.post('/api/switch-role/', {'role': role})

@then('the dashboard should focus on marketing-related metrics')
def step_impl(context):
    assert 'marketing_metrics' in context.response.data
    assert len(context.response.data['marketing_metrics']) > 0

@then('show detailed trends for "{metric1}" and "{metric2}"')
def step_impl(context, metric1, metric2):
    assert metric1 in context.response.data['detailed_trends']
    assert metric2 in context.response.data['detailed_trends']

@when('the user drills down into the underperforming "{metric_name}" metric')
def step_impl(context, metric_name):
    metric = Metric.objects.get(name=metric_name, project=context.project)
    context.response = context.client.get(f'/api/metrics/{metric.id}/drill-down/')

@then('the system should provide a detailed analysis of "{metric_name}"')
def step_impl(context, metric_name):
    assert context.response.status_code == 200
    assert 'detailed_analysis' in context.response.data
    assert context.response.data['detailed_analysis']['metric_name'] == metric_name

@then('suggest potential actions to improve "{metric_name}"')
def step_impl(context, metric_name):
    assert 'suggested_actions' in context.response.data
    assert len(context.response.data['suggested_actions']) > 0