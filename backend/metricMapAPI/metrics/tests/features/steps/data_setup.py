from behave import given
from django.core.management import call_command

@given('the system has historical data')
def step_impl(context):
    call_command('generate_historical_data')