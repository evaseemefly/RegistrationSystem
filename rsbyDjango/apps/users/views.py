from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import R_Author_Department
# Create your views here.

class UserListView(APIView):

    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication,BaseAuthentication)
    # permission_classes = (IsAuthenticated)

    def get(self,request):
        '''
        获取指定author所拥有的部门
        :param request:
        :return:
        '''
        content={
            'user':request.user,
            'auth':request.auth
        }
        author=request.user
        r_author_dep=R_Author_Department.objects.filter(aid_id=author.id)
        deps=[r.did for r in r_author_dep]
        return Response('')