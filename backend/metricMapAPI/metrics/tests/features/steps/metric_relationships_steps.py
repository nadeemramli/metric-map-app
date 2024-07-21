# features/steps/metric_relationships_steps.py
from behave import when, then

@when('the user views the metric relationship visualization')
def step_impl(context):
    context.response = context.client.get('/api/metrics/relationships/')

@then('the system should display a network graph of all metrics')
def step_impl(context):
    assert 'network_graph' in context.response.data

# Implement similar steps for viewing correlation coefficients and detailed relationship insights