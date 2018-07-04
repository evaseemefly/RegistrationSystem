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

from .models import UserInfo,DutyInfo,dutyschedule,R_DepartmentInfo_DutyInfo,DepartmentInfo,R_UserInfo_DepartmentInfo

#代理模型类
from .models import DutyScheduleProxyModel

from .serializers import DutyScheduleSerializer,UserSerializer,MergeScheduleSerializer,MergeDutyUserSerializer,R_Department_DutySerializer


class DutyScheduleBaseView(APIView):
    def getMergeScheduleListByDate(self,dids=[],pid=-1,target_date=datetime.now(),oneday=False):
        '''
        获取修改后的值班列表
        :param dids:
        :param pid:
        :param target_date:
        :return:
        '''
        schedule_list= self.getscheduleDetial(dids,pid,target_date,oneday)
        # 根据日期去重
        def MergeList(did,schedule_list,target_date=datetime.now()):
            '''

            :param did: 要合并的部门id
            :param target_date: 合并的日期
            :return:
            '''
            # 1 找到指定日的值班信息
            schedult_templist=schedule_list.filter(dutydate__year=target_date.year,dutydate__month=target_date.month,dutydate__day=target_date.day)

            # 2 列表推到过滤
            #6-21 修改
            # merge_templist=schedult_templist.filter(rDepartmentDuty__did__did==did)
            schedult_templist=schedult_templist.filter(rDepartmentDuty__did__did=did)
            # schedult_templist.filter(user__uid=1)

            # merge_templist = [MergeDutyUserSerializer(temp.user, temp.rDepartmentDuty) for temp in schedult_templist if
            #                   temp.rDepartmentDuty.did.did == did]

            # merge_templist=[MergeDutyUserSerializer(temp.user,temp.rDepartmentDuty) for temp in schedult_templist]
            merge_templist=[dict(user=UserSerializer(temp.user).data,dutydate=temp.dutydate,rDepartmentDuty=R_Department_DutySerializer(temp.rDepartmentDuty).data) for temp in schedult_templist]

            return merge_templist

        def DifferentDate(list):
            differntDate_list=[]
            for temp in list:
                if(temp.dutydate not in differntDate_list):
                    differntDate_list.append(temp.dutydate)
            return differntDate_list

        # 需要获取schedule_list中的不同的日期
        date_list=DifferentDate(schedule_list)
        merageSchedule_list=[]
        # for temp in date_list:
        if len(date_list)>0:
            merageSchedule_list=[dict(DutyUserList=MergeList(did,schedule_list,temp),dutydate=temp.strftime('%Y-%m-%d')) for did in dids for temp in date_list]
        # merageSchedule_list.append(dict_temp)
        # merageSchedule_list=[dict(DutyUserList=MergeList(did,schedule_list,target_date),dutydate=target_date.strftime('%Y-%m-%d')) for did in dids]
        # merageSchedule_list= [MergeScheduleSerializer(MergeList(did,schedule_list,target_date),target_date) for did in dids]
        return merageSchedule_list

    def getMergeScheduleListByOneDay(self,dids=[],pid=-1,target_date=datetime.now()):
        '''
                获取修改后的值班列表
                :param dids:
                :param pid:
                :param target_date:
                :return:
                '''
        schedule_list = self.getscheduleDetial(dids, pid, target_date)

        # 根据日期去重
        def MergeList(did, schedule_list, target_date=datetime.now()):
            '''

            :param did: 要合并的部门id
            :param target_date: 合并的日期
            :return:
            '''
            # 1 找到指定日的值班信息
            schedult_templist = schedule_list.filter(dutydate__year=target_date.year, dutydate__month=target_date.month,
                                                     dutydate__day=target_date.day)

            # 2 列表推到过滤
            # 6-21 修改
            # merge_templist=schedult_templist.filter(rDepartmentDuty__did__did==did)
            schedult_templist = schedult_templist.filter(rDepartmentDuty__did__did=did)
            # schedult_templist.filter(user__uid=1)

            # merge_templist = [MergeDutyUserSerializer(temp.user, temp.rDepartmentDuty) for temp in schedult_templist if
            #                   temp.rDepartmentDuty.did.did == did]

            # merge_templist=[MergeDutyUserSerializer(temp.user,temp.rDepartmentDuty) for temp in schedult_templist]
            merge_templist = [dict(user=UserSerializer(temp.user).data, dutydate=temp.dutydate,
                                   rDepartmentDuty=R_Department_DutySerializer(temp.rDepartmentDuty).data) for temp in
                              schedult_templist]

            return merge_templist

        def DifferentDate(list):
            differntDate_list = []
            for temp in list:
                if (temp.dutydate not in differntDate_list):
                    differntDate_list.append(temp.dutydate)
            return differntDate_list

        # 需要获取schedule_list中的不同的日期
        date_list = DifferentDate(schedule_list)
        merageSchedule_list = []
        # for temp in date_list:
        merageSchedule_list = [
            dict(DutyUserList=MergeList(did, schedule_list, temp), dutydate=temp.strftime('%Y-%m-%d')) for did in dids
            for temp in date_list]
        # merageSchedule_list.append(dict_temp)
        # merageSchedule_list=[dict(DutyUserList=MergeList(did,schedule_list,target_date),dutydate=target_date.strftime('%Y-%m-%d')) for did in dids]
        # merageSchedule_list= [MergeScheduleSerializer(MergeList(did,schedule_list,target_date),target_date) for did in dids]
        return merageSchedule_list

    def getscheduleDetial(self,dids=[],pid=-1,target_date=datetime.now(),oneday=False):
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
                schedule_list=[]
                # 2 根据id找到 值班表
                if oneday:
                    schedule_list=dutyschedule.objects.filter(rDepartmentDuty__in=rd_list,dutydate=target_date)
                else:
                    schedule_list = dutyschedule.objects.filter(rDepartmentDuty__in=rd_list,dutydate__year=target_date.year,dutydate__month=target_date.month)
                # 6-21 方式2
                # schedule_list=DutyScheduleProxyModel.objects.filter(rDepartmentDuty__in=rd_list,dutydate__year=target_date.year,dutydate__month=target_date.month)
        return schedule_list

class UserBaseView(APIView):
    def getuserlistbyuid(self,uids=None):
        '''
        根据用户ids获取制定的user list
        :param uids:
        :return:
        '''
        return UserInfo.objects.filter(uid__in=uids)

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

class R_Department_Duty_BaseView(APIView):
    def get_r_list(self,dids=[],duids=[]):
        '''
        根据 部门ids以及岗位ids获取指定的关系对象list
        :param dids:
        :param duids:
        :return:
        '''
        r_list=R_DepartmentInfo_DutyInfo.objects.filter(did_id__in=dids,duid_id__in=duids)
        return r_list
