# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/4/26 14:21'

'''
可抽闲出来的父类（view）放在此处
'''

import time
from datetime import datetime

from django.views.generic import View
from datetime import datetime
from django.core import serializers
from django.http import JsonResponse,HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import DutyInfo,dutyschedule,R_DepartmentInfo_DutyInfo,DepartmentInfo,R_UserInfo_DepartmentInfo
from .serializers import DutyScheduleSerializer,UserSerializer


class DutyScheduleBaseView(APIView):
    def getscheduleDetial(self,dids=[],pid=-1,target_date=datetime.now()):
        '''
        根据部门id list与所属的父级部门 获取符合条件的 值班信息（list）
        :param dids:
        :param pid:
        :return:
        '''
        schedule_list=[]
        if pid==-1:
            if len(dids)>0:
                # 1 根据部门找到 部门-岗位关联表 id
                rd_list = [temp.id for temp in R_DepartmentInfo_DutyInfo.objects.filter(did_id__in=dids)]
                # DepartmentInfo.objects.filter()
                # 2 根据id找到 值班表
                schedule_list = dutyschedule.objects.filter(rDepartmentDuty__in=rd_list,dutydate__year=target_date.year,dutydate__month=target_date.month)
        return schedule_list

class UserBaseView(APIView):
    def getuserlistbydepartment(self,dids=None):
        '''
        根据部门id获取该部门拥有的人员列表
        :param did:
        :return:
        '''
        if len(dids)>0:
            user_list=[r.uid for r in R_UserInfo_DepartmentInfo.objects.filter(did_id__in=dids) if r.uid.isdel==False]
        return user_list

class GroupBaseView(APIView):
    def getgroupByDepartment(self,did=None):
        '''
        根据传入的dids数组获取所有的群组,

        :param did:
        :return:R_UserInfo_DepartmentInfo
        '''
        groups= DepartmentInfo.objects.filter(pid=did)
        # r_user_depart= R_UserInfo_DepartmentInfo.objects.filter(did=groups)
        r_user_depart = R_UserInfo_DepartmentInfo.objects.filter(did_id__in=groups)
        return r_user_depart

class DutyBaseView(APIView):
    def getdutylistbydepartment(self,dids=[]):
        '''
        根据部门id，获取该部门拥有的岗位列表
        :param dids:
        :return:
        '''
        duty_list=[]
        if len(dids)>0:
            duty_list=[r.duid for r in R_DepartmentInfo_DutyInfo.objects.filter(did_id__in=dids)]
        return duty_list
