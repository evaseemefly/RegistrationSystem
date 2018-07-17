from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserListView(APIView):
    # authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication,BaseAuthentication)
    # permission_classes = (IsAuthenticated)

    def get(self,request):
        content={
            'user':request.user,
            'auth':request.auth
        }
        return Response(content)