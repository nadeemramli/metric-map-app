# features/steps/strategic_insights_steps.py
from behave import when, then

@when('the user views the "Strategy" dashboard')
def step_impl(context):
    context.response = context.client.get('/api/dashboards/strategy/')

@then('the system should display predictive analysis for all KPI metrics')
def step_impl(context):
    assert 'predictive_analysis' in context.response.data

# Implement similar steps for forecast vs. actual data, target setting, and chart type changes