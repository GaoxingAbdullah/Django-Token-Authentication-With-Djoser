
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import AccountUser

'''
This is the serializer that is used to create a new user. it overrides the default djoser serializer
'''
class UserCreateSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = AccountUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')