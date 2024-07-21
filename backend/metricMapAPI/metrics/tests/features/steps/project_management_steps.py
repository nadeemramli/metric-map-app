# features/steps/project_management_steps.py
from behave import given, when, then
from metrics.models import Project

@given('a logged-in user')
def step_impl(context):
    # Assume user is already logged in from previous steps
    pass

@when('the user creates a new project called "{project_name}"')
def step_impl(context, project_name):
    context.response = context.client.post('/api/projects/', {'name': project_name})

@then('the project "{project_name}" should be saved successfully')
def step_impl(context, project_name):
    assert context.response.status_code == 201
    assert Project.objects.filter(name=project_name).exists()

@when('the user switches to the "{project_name}" project')
def step_impl(context, project_name):
    project = Project.objects.get(name=project_name)
    context.response = context.client.post(f'/api/projects/{project.id}/switch/')

@then('the active project should be updated to "{project_name}"')
def step_impl(context, project_name):
    assert context.response.status_code == 200
    assert context.response.data['active_project'] == project_name