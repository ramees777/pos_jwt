from django.db import models
from rest_framework import fields, serializers
from rest_framework.exceptions import server_error

from . models import User



class RegisterSerielizer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)

    class Meta:
        model=User
        fields=['email','username','password']

    def validate(self, attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')         
        if not username.isalnum():
            raise serializers.ValidationError('the user name should only contain alpha num chars')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerielizer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=555)

    class Meta:
        model=User
        fields=['token']