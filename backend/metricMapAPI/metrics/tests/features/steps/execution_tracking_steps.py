# features/steps/execution_tracking_steps.py
from behave import when, then
from metrics.models import ActionRemark, Insight, Experiment

@when('the user adds an "Action Remark" for launching a new product on "{date}"')
def step_impl(context, date):
    context.response = context.client.post('/api/action-remarks/', {
        'description': 'New product launch',
        'date': date,
        'project': context.project.id
    })

@then('the "Action Remark" should be saved and visible on the timeline')
def step_impl(context):
    assert context.response.status_code == 201
    assert ActionRemark.objects.filter(project=context.project, description='New product launch').exists()

# Implement similar steps for insights, experiments, and viewing the execution dashboard