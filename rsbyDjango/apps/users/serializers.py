from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("name", "gender", "birthday", "email")

class ContentSerializer(serializers.Serializer):
    user=UserDetailSerializer()
    auth=serializers.CharField(max_length=200)