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
from .serializers import UserDetailSerializer,ContentSerializer
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

from django.contrib.auth import get_user_model
from rest_framework import serializers

class AuthorDetialView(APIView):
    # User=get_user_model()


    # class UserDetailSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model=User
    #         filed=("name")



    def get(self,request):
        '''
        根据用户获取该用户的信息并返回
        :param request:
        :return:
        '''

        class Content(object):
            def __init__(self, user, auth):
                self.user = user
                self.auth = auth
        content =Content(request.user,request.auth)
        serializer= ContentSerializer(content)
        print(serializer.data)
        # {
        #     'user': request.user,
        #     'auth': request.auth
        # }
        pass