__author__ = 'Bertrand'
from django.db import models
from sr_core.models.service import Service

class ServiceLog(models.Model):
    """
    model used to keep track of modification on services
    """
    #TBD : WARNING BUG - when a service is delete, we are to lose history !!! need to improve this mechanism
    service = models.ForeignKey(Service,
                                null=False,
                                on_delete=models.CASCADE)

    action = models.CharField(max_length=30,null=False)

