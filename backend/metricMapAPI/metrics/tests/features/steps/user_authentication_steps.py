# features/steps/user_authentication_steps.py
from behave import given, when, then
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@given('a user with valid credentials')
def step_impl(context):
    context.user = User.objects.create_user(username='testuser', password='testpass')
    context.client = APIClient()

@when('the user attempts to log in')
def step_impl(context):
    context.response = context.client.post('/api/token/', {'username': 'testuser', 'password': 'testpass'})

@then('the user should be successfully logged in')
def step_impl(context):
    assert context.response.status_code == 200
    assert 'access' in context.response.data