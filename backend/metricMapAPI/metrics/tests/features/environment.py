from behave import use_fixture
from behave_django.fixtures import django_test_runner
from django.contrib.auth.models import User

def before_all(context):
    use_fixture(django_test_runner, context)

def before_scenario(context, scenario):
    # Create a test user
    context.test.user = User.objects.create_user(username='testuser', password='12345')
    context.test.client.force_login(context.test.user)
    
    if 'historical data' in scenario.tags:
        call_command('generate_historical_data')

def after_scenario(context, scenario):
    # Clean up after each scenario
    User.objects.all().delete()

def after_all(context):
    # Clean up after all tests
    pass