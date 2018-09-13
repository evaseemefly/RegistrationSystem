from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models.base import ModelBase
from django.contrib.auth.models import User

# User=get_user_model()

# class UserDetailSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         #type: class 'django.db.models.base.ModelBase'
#         #<class 'django.contrib.auth.models.User'>
#         model=User
#         fields=("name", "email")


class UserDetailSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    username=serializers.CharField(max_length=200)

class ContentSerializer(serializers.Serializer):
    user=UserDetailSerializer()
    # auth=serializers.CharField(max_length=200)、