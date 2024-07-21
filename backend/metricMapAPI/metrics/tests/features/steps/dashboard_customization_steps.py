# features/steps/dashboard_customization_steps.py
from pytest_bdd import scenarios, given, when, then, parsers
from metrics.models import Dashboard

@when('the user creates a new dashboard "{dashboard_name}"')
def step_impl(context, dashboard_name):
    context.response = context.client.post('/api/dashboards/', {'name': dashboard_name, 'project': context.project.id})

@then('the dashboard "{dashboard_name}" should be saved successfully')
def step_impl(context, dashboard_name):
    assert context.response.status_code == 201
    assert Dashboard.objects.filter(name=dashboard_name, project=context.project).exists()

# Implement similar steps for adding metrics to dashboard, arranging layout, and generating reports