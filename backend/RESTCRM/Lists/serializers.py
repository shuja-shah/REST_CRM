''' Serializer for Model List '''
from Lists.models import List
from rest_framework import serializers


class ModelList (serializers.ModelSerializer):
    '''Serializer for Model List'''
    class Meta:
        model = List
        fields = [
            'id',
            'task',
            'is_completed',
        ]
        