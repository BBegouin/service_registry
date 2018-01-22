__author__ = 'Bertrand'

# from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from sr_core.views.service_viewset import ServiceViewSet


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'service', ServiceViewSet)

urlpatterns = [
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
