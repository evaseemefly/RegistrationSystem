from django.shortcuts import render

# Create your views here.
# 获取指定组的班级情况
from django.views.generic import View
from datetime import datetime
from django.core import serializers
from django.http import JsonResponse,HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import DutyInfo,dutyschedule,R_DepartmentInfo_DutyInfo,DepartmentInfo
from .serializers import DutyScheduleSerializer

class DutyListView(APIView):
    '''
    指定班级列表
    '''
    def get(self,request):
        '''
        根据指定的部门id以及传入的时间获取班级所拥有的的列表
        :param request:
        :return:
        '''
        # 搜索的时间（可选）
        # 若不选，则默认是当前月
        targetmonth=request.GET.get('searchdate','')
        did=3
        if targetmonth=='':
            targetmonth=datetime.now()
        # 分别获取指定日期的年和月
        search_year=targetmonth.year
        search_month=targetmonth.month
        # 获取指定组的对应的department的id
        # 根据部门id获取r_department_duty表中的记录（找到id）
        list_did=[out_r.id for out_r in R_DepartmentInfo_DutyInfo.objects.filter(did_id=did)]
        json_list=[]
        # 查询指定年月的值班列表
        duty_arr=dutyschedule.objects.filter(dutydate__year=search_year,dutydate__month=search_month)
        duty_arr=duty_arr.filter(rDepartmentDuty__in=list_did)

        print(len(duty_arr))
        # json_duty = serializers.serialize("json",duty_arr)
        # 使用drf实现序列化
        json_duty=DutyScheduleSerializer(duty_arr,many=True)
        return Response(json_duty.data)


class UserListView(APIView):
    def get(self,request):
        '''
        根据部门id或组id获取人员list
        :param request:
        :return:
        '''
        did=[1]
        pid=-1
        # 若未传pid
        if pid!=None:
            if did!=None:
                # if len(did)>1:
                # 传入了一组部门
                # 找到对应的部门
                # 返回dutyschedule（值班表）

                # 1 根据部门找到 部门-岗位关联表 id
                rd_list= [temp.id for temp in R_DepartmentInfo_DutyInfo.objects.filter(did_id__in=did)]
                # DepartmentInfo.objects.filter()
                # 2 根据id找到 值班表
                schedule_list= dutyschedule.objects.filter(rDepartmentDuty__in=rd_list)
                # seredule_json=serializers.serialize("json",schedule_list.data)
                seredule_json = DutyScheduleSerializer(schedule_list,many=True)
                return Response(seredule_json.data)

        return Response(None)
