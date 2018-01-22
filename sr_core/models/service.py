__author__ = 'Bertrand'
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=30)
    version = models.CharField(max_length=30)