__author__ = 'Bertrand'

from behave import *
from rest_framework.test import APIClient
from rest_framework import status
from sr_core.models.service import Service
from sr_core.models.service_log import ServiceLog

client = APIClient()

@when('I update a service of id "{service_id}" by changing its name to "{new_name}" or its version to "{new_version}"')
def step_impl(context,service_id, new_name, new_version):
    patch_datas = {}
    patch_datas['id'] = service_id
    if new_name:
        patch_datas['name'] = new_name
    if new_version:
        patch_datas['version'] = new_version

    response = client.patch('/service/'+service_id+'/',patch_datas)
    assert response.status_code == status.HTTP_200_OK
    context.response = response
