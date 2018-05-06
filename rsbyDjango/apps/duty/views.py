
'''
可抽象出来的父类view放在view_base.py文件中，此处仅放置路由中指向的类视图
'''

from django.shortcuts import render

# Create your views here.
# 获取指定组的班级情况
from django.views.generic import View
from datetime import datetime
from django.core import serializers
from django.http import JsonResponse,HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import DutyInfo,dutyschedule,R_DepartmentInfo_DutyInfo,DepartmentInfo,R_UserInfo_DepartmentInfo
from .serializers import DutyScheduleSerializer,UserSerializer,DutySerializer
from .view_base import DutyScheduleBaseView,UserBaseView,DutyBaseView

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
        # did=3
        dids = request.query_params.getlist('group_id')
        if targetmonth=='':
            targetmonth=datetime.now()
        # 分别获取指定日期的年和月
        search_year=targetmonth.year
        search_month=targetmonth.month
        # 获取指定组的对应的department的id
        # 根据部门id获取r_department_duty表中的记录（找到id）
        list_did=[out_r.id for out_r in R_DepartmentInfo_DutyInfo.objects.filter(did_id_in=dids)]
        json_list=[]
        # 查询指定年月的值班列表
        duty_arr=dutyschedule.objects.filter(dutydate__year=search_year,dutydate__month=search_month)
        duty_arr=duty_arr.filter(rDepartmentDuty__in=list_did)

        # print(len(duty_arr))
        # json_duty = serializers.serialize("json",duty_arr)
        # 使用drf实现序列化
        json_duty=DutyScheduleSerializer(duty_arr,many=True)
        return Response(json_duty.data)

class UserListView(UserBaseView):
    def get(self,request):
        # did = [3,5]
        # 注意使用此种方式无法获取list
        # dids= request.query_params.get('group_id',None)
        # 使用此种方式可以获取list
        dids=request.query_params.getlist('group_id')
        user_list=self.getuserlistbydepartment(dids)
        user_json = UserSerializer(user_list, many=True)
        return Response(user_json.data)

class ScheduleModificationView(APIView):
    def post(self,request):
        '''
        获取前端提交的修改数据
        :param request:
        :return:
        '''
        # 获取post提交过来的数据
        modification_data= request.data
        schedule_id=modification_data.get('id',None)
        schedule_code=modification_data.get('code',None)
        schedule_uid = modification_data.get('uid', None)
        # 以上三个变量均不为none
        if None in [schedule_id,schedule_code]:
            return
        '''
        下面使用工厂方法实现：
            判断schedule_code，执行不同的修改操作
        '''
        # 用户
        if schedule_code=='user':
            # 修改值班表中指定的用户信息
            # 1 查询
            '''
                先根据值班信息表id找到该行数据
                直接修改用户id
            '''
            schedule_obj= dutyschedule.objects.filter(id=schedule_id)
            # 注意此处可能会出错
            '''
                错误原因：
                   * 1、用户表中不存在该用户
            '''

            schedule_obj.update(user_id=schedule_uid)
        # 岗位职责
        if schedule_code=='duty':
            '''
                1、先根据值班信息表id找到该行数据
                2、获取 r_department_duty
                    在r_department_duty表中
                    根据传入的r_department_duty id
                    或
                    did与duid获取r_department_duty id
                将该id作为值班信息表的 rid
            '''
            # 获取前端传入的岗位及部门id
            schedule_duid=modification_data.get('duid',None)
            schedule_did= modification_data.get('did',None)
            # 非空
            if None not in[schedule_duid,schedule_did]:
                temp_schedule=dutyschedule.objects.filter(id=schedule_id)
                # 取出第一个
                temp_schedule=temp_schedule.first()
                if temp_schedule is not None:
                    # 在部门职责信息表中根据部门id以及职责id找到对应的行
                    rDerDuty= R_DepartmentInfo_DutyInfo.objects.filter(did=schedule_did,duid=schedule_duid)
                    # print(rDerDuty)
                    # 注意使用get,若不存在则会抛出异常
                    # rDerDuty_temp=R_DepartmentInfo_DutyInfo.objects.get(did_id=schedule_did,duid=schedule_duid)
                    if(rDerDuty.count()>0):
                        temp_schedule.rDepartmentDuty=rDerDuty.first()
                        temp_schedule.save()
                    # 若关联表中不存在（有可能），则1：先在关联表中创建；2：在写入值班信息表
                    else:
                        #分别获取部门以及岗位对象
                        depart_temp= DepartmentInfo.objects.filter(did=schedule_did)
                        duty_temp=DutyInfo.objects.filter(duid=schedule_duid)
                        r=R_DepartmentInfo_DutyInfo(did=depart_temp.first(),duid=duty_temp.first())
                        r.save()
                        # R_DepartmentInfo_DutyInfo.objects.create(did=schedule_did,duid=schedule_duid)
                        temp_schedule.rDepartmentDuty=r
                        temp_schedule.save()
                        # pass
                    # temp_schedule.update(rDepartmentDuty_id=rDerDuty.id)

            pass

        pass


class ScheduleListView(DutyScheduleBaseView):
    def get(self,request):
        '''
        根据部门id或组id获取人员list
        :param request:
        :return:
        '''
        did=[4]
        pid=-1
        # 传入了一组部门
        # 找到对应的部门
        # 返回dutyschedule（值班表）
        schedule_list=self.getscheduleDetial(dids=did)
        seredule_json = DutyScheduleSerializer(schedule_list, many=True)
        # return JsonResponse(seredule_json.data)
        return Response(seredule_json.data,status=status.HTTP_202_ACCEPTED)
        # return Response(seredule_json.data)

class DutyListView(DutyBaseView):
    def get(self,request):
        '''

        :param request:
        :return:
        '''
        dids = request.query_params.getlist('group_id')
        duty_list=self.getdutylistbydepartment(dids=dids)
        duty_json=DutySerializer(duty_list,many=True).data
        return Response(duty_json)

