__author__ = 'Bertrand'
from rest_framework import permissions
from rest_framework import viewsets
from sr_core.models.service import Service
from sr_core.models.service_log import ServiceLog
from sr_core.views.serializers.service_serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    Service end point.
    TBD : access should be restricted, using authentication or whitelist
    """
    queryset = Service.objects.all()

    def get_queryset(self):
        """
        perform filtering and request optimizations using select related / prefetch related if needed
        :return:
        """
        param_name = self.request.query_params.get('name', None)
        param_version = self.request.query_params.get('version', None)

        queryset  = Service.objects.all()

        if param_name is not None:
            queryset = queryset.filter(name=param_name)

        if param_version is not None:
            queryset = queryset.filter(version=param_version)

        return queryset

    def perform_create(self, serializer):
        """
        used to create a service, if everything is ok, insert an entry in the log table
        :type request: rest_framework.request.Request
        :param args:
        :param kwargs:
        :return:
        """
        service_object = serializer.save()
        sl = ServiceLog(service=service_object,action="created")
        sl.save()

    def perform_update(self, serializer):
        """
        used to update a service and add an entry "changed" in th log table
        :param serializer:
        :return:
        """
        service_object = serializer.save()
        sl = ServiceLog(service=service_object,action="changed")
        sl.save()

    def get_serializer_class(self):
        if self.action == 'list'\
            or self.action == 'create'\
            or self.action == 'update'\
            or self.action == 'partial_update':
                return ServiceSerializer
        elif self.action == 'retrieve' \
            or self.action == 'destroy':
                return None

