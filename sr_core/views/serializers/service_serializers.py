__author__ = 'Bertrand'
from rest_framework import serializers
from sr_core.models.service import Service

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id','name','version')