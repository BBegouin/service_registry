__author__ = 'Bertrand'
from rest_framework import permissions
from rest_framework import viewsets
from sr_core.models.service import Service
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

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceSerializer
        elif self.action == 'retrieve' \
            or self.action == 'destroy'\
            or self.action == 'update'\
            or self.action == 'partial_update'\
            or self.action == 'create':
            return None

