__author__ = 'Bertrand'

from behave import *
from rest_framework.test import APIClient
from rest_framework import status
from sr_core.models.service_log import ServiceLog

client = APIClient()


@given('there is an empty ServiceRegistry')
def step_impl(context):
    assert True

@when('I add a service "{service}" with version "{version}"')
def step_impl(context,service,version):
    create_datas = {}
    create_datas['name'] = service
    create_datas['version'] = version

    response = client.post('/service/',create_datas)
    assert response.status_code == status.HTTP_201_CREATED
    context.response = response


@then('I should be notified with a change "{change}"')
def step_impl(context,change):
    #check there is log entry in the service log table
    log_entry = ServiceLog.objects.filter(service__pk=context.response.data['id'])
    assert len(log_entry) == 1
    assert log_entry.first().action == change
