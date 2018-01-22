__author__ = 'Bertrand'

import os
from behave import *
from rest_framework.test import APIClient
from rest_framework import status
from django.core.management import call_command

client = APIClient()
common_fixture_dir = 'fixtures/'

app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
fixture_path = os.path.join(app_path, common_fixture_dir)

@given('there is a ServiceRegistry containing basic services')
def step_impl(context):
    call_command('loaddata', fixture_path +'services.json')
    assert True

@when('I search for a service "{service}" without version')
def step_impl(context,service):
    resp = client.get('/service/?name='+service)
    context.response = resp
    assert resp.status_code == status.HTTP_200_OK

@when('I search for a service "{service}" with version "{version}"')
def step_impl(context,service,version):
    resp = client.get('/service/?name='+service+'&version='+version)
    context.response = resp
    assert resp.status_code == status.HTTP_200_OK

@then('I should find count "{count}" services')
def step_impl(context,count):
    assert len(context.response.data) == int(count)

@then('the service "{service}" should have the correct version "{version}"')
def step_impl(context,service,version):
    assert True
