''' Serializer for User and List '''
from rest_framework import serializers
from user.models import List, user


class ModelList (serializers.ModelSerializer):
    '''Serializer for Model List'''
    class Meta:
        model = List
        fields = [
            'id',
            'task',
            'is_completed',
        ]
class User_SERIALIZATION (serializers.ModelSerializer):
    '''Serializer for User'''
    class Meta:
        model = user
        fields = [
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}
        # def create(self, validated_data):
        #     user = user.objects.create_user(**validated_data)
        #     return user