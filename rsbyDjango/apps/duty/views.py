
'''
可抽象出来的父类view放在view_base.py文件中，此处仅放置路由中指向的类视图
'''

from django.shortcuts import render

# Create your views here.
# 获取指定组的班级情况

from datetime import datetime
import json

from django.views.generic import View
from django.core import serializers
from django.http import JsonResponse,HttpResponse

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

# drf权限验证
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import DutyInfo,dutyschedule,R_DepartmentInfo_DutyInfo,DepartmentInfo,R_UserInfo_DepartmentInfo,UserInfo,dutyschedule
from .serializers import DutyScheduleSerializer,UserSerializer,DutySerializer,R_User_DepartmentSerializer,R_User_Department_Simplify_Serializer,User_Simplify_Serializer,R_Department_User_Simplify_Serializer,UserSerializer,SchedulelSerializer,DepartmentSerializer

# from .serializers import DutyScheduleSerializer,UserSerializer,DutySerializer,R_User_DepartmentSerializer,R_User_Department_Simplify_Serializer,User_Simplify_Serializer,R_Department_User_Simplify_Serializer, DepartmentDutyUserSerializer,UserSerializer

from .view_base import DutyScheduleBaseView,UserBaseView,DutyBaseView,GroupBaseView,R_Department_Duty_BaseView
from .model_middle import R_User_Department_Middle,DepartmentMidModel
from .forms import ScheduleForm
from Common.MyJsonEncoder import DateTimeEncoder
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class DepartmentListView(APIView):
    def get(self,request):
        '''
            获取全部的department（且pid=0的）
        :param request:
        :return:
        '''
        query_dic = request.query_params
        departments=DepartmentInfo.objects.filter(Q(pid=0),~Q(did=-999),Q(isShow=True))
        json_list= DepartmentSerializer(departments,many=True).data
        return Response(json_list)


class DutyListView(APIView):
    # authentication_classes = (SessionAuthentication,BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
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

class GroupListView(GroupBaseView):
    def get(self,request):
        '''
        根据传入的pid获取该pid所拥有的群组，以及群组中包含的人员
        :param request:
        :return:
        '''

        def user_department_middle2dict(m):
            return {
                'name':m.name,
                'did':m.did,
                'uid':m.uid
            }

        user=UserInfo()
        user.id=1
        user.username='123'
        user.isdel=True

        did=request.query_params.get('department_id',None)
        # user_json=User_Simplify_Serializer([user],many=True).data
        # r_user_department=self.getgroupByDepartment(int(did))
        r_user_department = self.getgroup(int(did))
        r_json=R_User_Department_Simplify_Serializer(r_user_department,many=True)
        r=R_User_Department_Middle()
        # finial_list=r.ToMiddleSerializer(r_user_department)
        # r_json=R_Department_User_Simplify_Serializer(finial_list,many=True)
        finial_list=r.ToMiddle(r_user_department)
        # r_json=json.dumps(finial_list,default=user_department_middle2dict)
        # 注意当序列化的内容包含中文时，需要设置ensure_ascii为false
        r_json=json.dumps(finial_list,cls=DateTimeEncoder,default=lambda obj:obj.__dict__,ensure_ascii=False)
        # 注意以下此种方式只能序列化类型为QuerySet的对象
        # r_json=serializers.serialize(finial_list)

        # r_json = R_User_Department_Simplify_Serializer(r_user_department)
        # return Response(r_json)
        # return JsonResponse(finial_list,safe=False)
        return HttpResponse(r_json,content_type='application/json')

class ScheduleCreateView(DutyScheduleBaseView,R_Department_Duty_BaseView,UserBaseView):

    def post(self,request):
        '''
            根据前台提交的内容新建该日的记录
        :param request:
        :return:
        '''

        '''
            1、查询数据库指定group以及指定日期是否已经存在值班信息
            2、若不存在则创建，并赋予默认值
        '''
        query_dic = request.data
        # 分别获取users_id,groups_id,selected_date
        # 注意前端传过来的使用bootstrap-table get 时传递的data中若为数组会自动在原有名字后面加上一个[]，注意！
        # 前端传递过来的did是一个int数值，需要改为[]
        # 注意python三元运算符
        did = query_dic.get('did', None)
        dids=[did] if did!=None else []
        uid=query_dic.get('uid',-999)
        # duid = query_dic.get('duid',None)
        target_date = query_dic.get('selected_date',None)
        schedule_dutydate = datetime.strptime(target_date, '%Y-%m-%d')
        duids=query_dic.get('duids',None)

        schedulelist= self.getMergeScheduleListByDate(dids=dids,target_date=datetime.strptime(target_date, '%Y-%m-%d'),oneday=True)
        if(len(schedulelist)==0):
            # 指定日期，指定的group未有值班信息，则创建新的
            schedule_rd_list = self.get_r_list([did], duids)
            search_user = self.getuserlistbyuid([uid])
            for temp in schedule_rd_list:
                dutyschedule.objects.create(
                    rDepartmentDuty_id=temp.id,
                    user_id=search_user.first().uid,
                    dutydate=schedule_dutydate)
            pass
        elif(len(schedulelist)==1):
            if(len(schedulelist[0].get('DutyUserList'))==0):
                # 指定日期，指定的group未有值班信息，则创建新的
                schedule_rd_list=self.get_r_list([did],duids)
                search_user=self.getuserlistbyuid([uid])
                for temp in schedule_rd_list:
                    dutyschedule.objects.create(
                        rDepartmentDuty_id=temp.id,
                        user_id=search_user.first().uid,
                        dutydate=schedule_dutydate)
                # (dutyschedule.objects.create(
                #     rDepartmentDuty_id=rd_temp.id,
                #     user_id=search_user.first().uid,
                #     dutydate=schedule_dutydate
                # )
                #     for rd_temp in schedule_rd_list)
                pass
        return Response(status=status.HTTP_200_OK)

class ScheduleModificationView(R_Department_Duty_BaseView,UserBaseView):
    def post(self,request):
        '''
        获取前端提交的修改数据
        :param request:
        :return:
        '''
        # 获取post提交过来的数据
        modification_data= request.data
        form= ScheduleForm(request.POST)
        schedule_id=modification_data.get('id',None)
        schedule_code=modification_data.get('code',None)
        schedule_uid = modification_data.get('uid', None)
        schedule_did=modification_data.get('did',None)
        schedule_duid=modification_data.get('duid',None)

        schedule_dutydate=modification_data.get('dutydate',None) or datetime.now().strftime('%Y-%m-%d')
        schedule_dutydate=datetime.strptime(schedule_dutydate,'%Y-%m-%d')
        # 以上三个变量均不为none
        if None in [schedule_code]:
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
            # 获取指定的duty与department的关系
            r_dep_duty= R_DepartmentInfo_DutyInfo.objects.filter(did=schedule_did,duid=schedule_duid)
            schedule_obj= dutyschedule.objects.filter(rDepartmentDuty=r_dep_duty[0],dutydate=schedule_dutydate)
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
                # 取出第一个值班信息
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

        # 修改日期
        if schedule_code=='date':
            schedule_obj=dutyschedule.objects.filter(id=schedule_id)
            schedule_obj.update(dutydate=schedule_dutydate)
            pass

        # 提交的为 user以及 duty（说明为新建）
        # 提交时应提交具体的group_id（部门），而非默认值（-999）
        if schedule_code=='all':
            schedule_rd=self.get_r_list([schedule_did],[schedule_duid])
            search_user=self.getuserlistbyuid([schedule_uid])
            dutyschedule.objects.create(
                rDepartmentDuty_id=schedule_rd.first().id,
                user_id=search_user.first().uid,
                dutydate=schedule_dutydate
            )

        return Response(status=status.HTTP_200_OK)

'''根据输入的起止时间和department的did信息，统计时间范围内指定department值班总数'''
class DepartmentStatisticsView(APIView):
    '''
    根据起止日期（yyyy-mm-dd）获取
        :param request:
          必须包含：
              startDate：起始时间
              endDat: 终止时间
              isMonth: 是否统计起止时间范围内，还是只统计该月
              did：department的did
        :return:
    by：wb
    '''
    def get(self,request):
        startDate = request.query_params.getlist('startDate')
        endDate = request.query_params.getlist('endDate')
        isMonth = request.query_params.getlist('isMonth')
        did = request.query_params.getlist('did')
        count = 0

        if isMonth[0] == '0':
            dutyStatic_list = [r for r in dutyschedule.objects.filter(dutydate=startDate[0])]

            for line in dutyStatic_list:
                if (line.user.username != '默认值') & (line.rDepartmentDuty.did.did == int(did[0])):
                    count += 1
        else:
            dutyStatic_list = [r for r in dutyschedule.objects.filter(dutydate__gte=startDate[0], dutydate__lte=endDate[0])]
            for line in dutyStatic_list:
                if (line.user.username != '默认值') & (line.rDepartmentDuty.did.did == int(did[0])):
                    count += 1
        result = {'count': count}
        json_str = json.dumps(result, ensure_ascii=False)

        return HttpResponse(json_str, content_type='application/json')

class ScheduleShowListView(APIView):
    '''
        获取指定日期及指定部门的所有值班人员
    '''
    def get_backup_1(self,request):
        '''
        根据日期（yyyy-mm-dd）获取
        :param request:
          必须包含：
              user_id，
              isdel，
              isdel
        :return:
        '''

        target_date = request.query_params.getlist('datetime')
        schedule_list = [r for r in dutyschedule.objects.filter(dutydate=target_date[0])]

        '''取出查询日期当天的uer，department和duty信息'''
        user_list = [t.user for t in schedule_list]
        department_list = [t.rDepartmentDuty.did for t in schedule_list]
        duty_list = [t.rDepartmentDuty.duid for t in schedule_list]

        '''刘思晗的东西'''
        #
        # '''以department id 为标识组合值班查询结果'''
        #
        # class DutyUserMiddelModel(object):
        #     def __init__(self,duty,users):
        #         duty=duty
        #         user_list=users
        #
        # class DepartmentDutyMiddelModel(object):
        #     def __init__(self,deparment,duty_list):
        #         deparment=deparment
        #         duty_list=duty_list
        #
        # class SearchModel(object):
        #     def __init__(self,deps):
        #         department_list=deps
        # from .serializers import DutyUserSerializer,DepartmentDutySerializer,SchedulelSerializer
        # dutyuser_list=DutyUserMiddelModel(duty_list[0],user_list[:2])
        # temp= DutyUserSerializer(dutyuser_list).data
        #
        # DepartmentDutyMiddelModel(department_list[0],DutyUserMiddelModel)
        # merage_json=

        '''找到指定日期下所有deparment的id，并去除重复id'''
        list_deparmentID = []
        for i in range(len(department_list)):
            list_deparmentID.append(department_list[i].did)
        list_noRepeat = []
        index = 0
        for i in list_deparmentID:
            if not i in [x[0] for x in list_noRepeat]:
                list_noRepeat.append([i, index])
            index = index +1

        append_deparment = {}
        append_deparment_list = {}
        append_duty_list = {}
        append_user_list = {}
        append_user = {}

        '''遍历无重复值的departmentID，依据该id找出对应department的user信息'''
        for i in list_noRepeat:
            for j in range(len(department_list)):
                if i[0] == department_list[j].did:
                    append_user["uid"] = user_list[j].uid
                    append_user["isdel"] = user_list[j].isdel
                    append_user["username"] = user_list[j].username
                    append_user_list[str(user_list[j].username)] = append_user
                    append_duty_list[str(duty_list[j])] = append_user_list

            append_deparment_list[str(department_list[i[1]].derpartmentname)] = append_duty_list
            append_duty_list = {}
            append_user_list = {}
        append_deparment[str(target_date[0])] = append_deparment_list

        json_str = json.dumps(append_deparment,ensure_ascii=False)
        print(json_str)

        return HttpResponse(json_str,content_type='application/json')

		
class ScheduleShowListView(APIView):
    def get_old(self,request):
        '''
        根据日期（yyyy-mm-dd）获取
        :param request:
          必须包含：
              user_id，
              group，
              selected_date
          可选：
            （均为数组）
             users_id，
             groups_id
        :return:
        '''
        query_dic=request.query_params
        # 分别获取users_id,groups_id,selected_date
        # 注意前端传过来的使用bootstrap-table get 时传递的data中若为数组会自动在原有名字后面加上一个[]，注意！
        uids=query_dic.get('users_id[]')
        dids=query_dic.get('group_id_new')
        # dids=query_dic.get('groups_id[]')
        target_date=query_dic.get('selected_date')
		
		#王豹的东西
		# target_date = request.query_params.getlist('datetime')
        # target_date = request.query_params.getlist('datetime')
        # target_datetime = datetime.strptime(target_date[0], "%Y-%m-%d")

        # 以下此种方式无法序列化
        # serializer=DutyScheduleMiddleSerializer(schedule_list)
        # schedule_data=serializer.data
        '''
            取出查询日期当天的uer，department和duty信息
            2018-08-28 重新修改
            具体流程：
                1 根据rDepartmentDuty找到所有的department对象，存在department_list中
                2 获取所有的顶部department（pid=0）
                注意，此处存在问题：
                    由于保存的关系表中均为组一级别（实际包含室领导，是否加入管理组？），
                    所以获取pid为0需要单独获取
                3 获取取到的所有的department所对应的user list
        '''
        # schedule_list = [r for r in dutyschedule.objects.filter(dutydate=target_date)]
        # schedule_list=dutyschedule.objects.filter(dutydate=target_date).exclude(user_id=-999)
        # 根据传入的值班日期获取该日的值班信息
        # 1
        schedule_list = dutyschedule.objects.filter(Q(dutydate=target_date), ~Q(user=-999))
        department_list = [t.rDepartmentDuty.did for t in schedule_list]
        # 2-1 去重
        department_list=list(set(department_list))
        # departemnt_top_list=[d for d in department_list if d.pid==0]
        # 2-2 找到顶部department
        departemnt_top_list = DepartmentInfo.objects.filter(pid=0)
        # 暂时注释掉，放在model_middle.py中
        # class DepartmentMidModel():
        #     def __init__(self,dep_top,list):
        #         department_parent=dep_top
        #         departments_child=list
        # 2-3 找到指定日期的值班信息中包含的全部department list
        list_dep_mid=[]
        # 方式1：此种方式有问题，会将所有的top department全部输出，暂时注释掉
        # for d_part in departemnt_top_list:
        #     list_temp=[]
        #     for d_child in department_list:
        #         if(d_part.did==d_child.pid):
        #             list_temp.append(d_child)
        #
        #     list_dep_mid.append(DepartmentMidModel(d_part,list_temp))
        # 方式2：优先遍历schedule中有的department
        for d_child in department_list:
            list_temp=[]
            for d_part in departemnt_top_list:
                if(d_part.did==d_child.pid):
                    list_temp.append(d_child)
            list_dep_mid.append(DepartmentMidModel(d_part,list_temp))
        # 方式3：使用列表推导
        # list=[DepartmentMidModel(d_part) for d_child in department_list for d_part in departemnt_top_list if d_child.pid==d_part.did]

        # department_mid_list=[{d_child,d_part} for d_child in department_list for d_part in departemnt_top_list if d_part.did==d_child.pid]


        user_list = [t.user for t in schedule_list]

        duty_list = [t.rDepartmentDuty.duid for t in schedule_list]

        '''以department id 为标识组合值班查询结果'''

        class DutyUserMiddelModel(object):
            def __init__(self,duty,users):
                duty=duty
                user_list=users

        class DepartmentDutyMiddelModel(object):
            def __init__(self,deparment,duty_list):
                deparment=deparment
                duty_list=duty_list

        class SearchModel(object):
            def __init__(self,deps):
                department_list=deps
        from .serializers import DutyUserSerializer,DepartmentDutySerializer

        dutyuser_list=DutyUserMiddelModel(duty_list[0],user_list[:2])
        temp= DutyUserSerializer(dutyuser_list).data

        DepartmentDutyMiddelModel(department_list[0],DutyUserMiddelModel)
        # merage_json=


        # list_deparmentID = []
        # for i in range(len(department_list)):
        #     list_deparmentID.append(department_list[i].did)
        # list_noRepeat = []
        # index = 0
        # for i in list_deparmentID:
        #     if not i in [x[0] for x in list_noRepeat]:
        #         list_noRepeat.append([i, index])
        #     index = index +1
        #
        # append_deparment = {}
        # append_deparment_list = {}
        # append_duty_list = {}
        # append_user_list = {}
        # append_user = {}

        # for i in list_noRepeat:
        #     for j in range(len(department_list)):
        #         if i[0] == department_list[j].did:
        #             append_user["uid"] = user_list[j].uid
        #             append_user["isdel"] = user_list[j].isdel
        #             append_user["username"] = user_list[j].username
        #             append_user_list[str(user_list[j].username)] = append_user
        #             append_user_list[]
        #             append_duty_list[str(duty_list[j])] = append_user_list
        #
        #     append_deparment_list[str(department_list[i[1]].derpartmentname)] = append_duty_list
        #     append_duty_list = {}
        #     append_user_list = {}
        # append_deparment[str(target_date[0])] = append_deparment_list

        # append_deparment_list = {}
        # append_duty_list = []
        # for i in list_noRepeat:
        #     for j in range(len(department_list)):
        #         if i[0] == department_list[j].did:
        #             append_duty = duty_user(duty_list[j], user_list[j])
        #             append_duty_list.append(append_duty)
        #     append_department = department_duty_user(department_list[i[1]], append_duty_list)
        #     append_duty_list = []
        #     # append_duty_list[0].append(user_list[j])
        #     # append_deparment_list.append(append_department)
        #     append_deparment_list[department_list[i[1]].derpartmentname] = append_department

        json_str = json.dumps(append_deparment,ensure_ascii=False)
        print(json_str)
        # json_department = DepartmentDutyUserSerializer(append_deparment_list, many=True)
        # return JsonResponse(append_deparment,encoder=)
        return HttpResponse(json_str,content_type='application/json')
        # return Response(json_str)
    
    def get(selfs,request):
        '''
            根据selected_date与did获取所有匹配的值班人员名单
        :param request:
        :return:
        '''
        query_dic = request.query_params
        # 分别获取users_id,groups_id,selected_date
        # 注意前端传过来的使用bootstrap-table get 时传递的data中若为数组会自动在原有名字后面加上一个[]，注意！
        # 1 获取指定的 日期 与 部门id
        target_date = query_dic.get('selectedDate')
        target_department=query_dic.get('did')

        # 2 过滤值班信息表，并去掉user_id为-999的
        # 注意此处有一个bug，现已修改：
        # 过滤的是department的pid为传入的did（查询某个部门的全部的值班信息）
        list= dutyschedule.objects.filter(Q(dutydate=target_date),Q(rDepartmentDuty__did__pid__in=target_department),~Q(user_id=-999))

        # 3
        json_list=DutyScheduleSerializer(list,many=True).data

        return Response(json_list)

    def get_test(self, request):
            '''
            根据日期（yyyy-mm-dd）获取
            :param request:
              必须包含：
                  user_id，
                  group，
                  selected_date
              可选：
                （均为数组）
                 users_id，
                 groups_id
            :return:
            '''
            query_dic = request.query_params
            # 分别获取users_id,groups_id,selected_date
            # 注意前端传过来的使用bootstrap-table get 时传递的data中若为数组会自动在原有名字后面加上一个[]，注意！
            target_date = query_dic.get('selected_date')

            # 以下此种方式无法序列化
            # serializer=DutyScheduleMiddleSerializer(schedule_list)
            # schedule_data=serializer.data
            '''
                取出查询日期当天的uer，department和duty信息
                2018-08-28 重新修改
                具体流程：
                    1 根据rDepartmentDuty找到所有的department对象，存在department_list中
                    2 获取所有的顶部department（pid=0）
                    注意，此处存在问题：
                        由于保存的关系表中均为组一级别（实际包含室领导，是否加入管理组？），
                        所以获取pid为0需要单独获取
                    3 获取取到的所有的department所对应的user list
            '''
            # schedule_list = [r for r in dutyschedule.objects.filter(dutydate=target_date)]
            # schedule_list=dutyschedule.objects.filter(dutydate=target_date).exclude(user_id=-999)
            # 根据传入的值班日期获取该日的值班信息
            # 1
            schedule_list = dutyschedule.objects.filter(Q(dutydate=target_date), ~Q(user=-999))
            department_list = [t.rDepartmentDuty.did for t in schedule_list]
            # 2-1 去重
            department_list = list(set(department_list))
            # departemnt_top_list=[d for d in department_list if d.pid==0]
            # 2-2 找到顶部department
            departemnt_top_list = DepartmentInfo.objects.filter(pid=0)
            # 暂时注释掉，放在model_middle.py中
            # class DepartmentMidModel():
            #     def __init__(self,dep_top,list):
            #         department_parent=dep_top
            #         departments_child=list
            # 2-3 找到指定日期的值班信息中包含的全部department list
            list_dep_mid = []
            # 方式1：此种方式有问题，会将所有的top department全部输出，暂时注释掉
            # for d_part in departemnt_top_list:
            #     list_temp=[]
            #     for d_child in department_list:
            #         if(d_part.did==d_child.pid):
            #             list_temp.append(d_child)
            #
            #     list_dep_mid.append(DepartmentMidModel(d_part,list_temp))
            # 方式2：优先遍历schedule中有的department
            for d_child in department_list:
                list_temp = []
                for d_part in departemnt_top_list:
                    if (d_part.did == d_child.pid):
                        list_temp.append(d_child)
                list_dep_mid.append(DepartmentMidModel(d_part, list_temp))
            # 方式3：使用列表推导
            # list=[DepartmentMidModel(d_part) for d_child in department_list for d_part in departemnt_top_list if d_child.pid==d_part.did]

            # department_mid_list=[{d_child,d_part} for d_child in department_list for d_part in departemnt_top_list if d_part.did==d_child.pid]

            user_list = [t.user for t in schedule_list]

            duty_list = [t.rDepartmentDuty.duid for t in schedule_list]

            '''以department id 为标识组合值班查询结果'''

            class DutyUserMiddelModel(object):
                def __init__(self, duty, users):
                    duty = duty
                    user_list = users

            class DepartmentDutyMiddelModel(object):
                def __init__(self, deparment, duty_list):
                    deparment = deparment
                    duty_list = duty_list

            class SearchModel(object):
                def __init__(self, deps):
                    department_list = deps

            from .serializers import DutyUserSerializer, DepartmentDutySerializer

            dutyuser_list = DutyUserMiddelModel(duty_list[0], user_list[:2])
            temp = DutyUserSerializer(dutyuser_list).data

            DepartmentDutyMiddelModel(department_list[0], DutyUserMiddelModel)

            json_str = json.dumps(append_deparment, ensure_ascii=False)
            print(json_str)
            # json_department = DepartmentDutyUserSerializer(append_deparment_list, many=True)
            # return JsonResponse(append_deparment,encoder=)
            return HttpResponse(json_str, content_type='application/json')
            # return Response(json_str)

class ScheduleShowStaticListView(APIView):
    '''
        读取左侧导航栏的中心领导以及业务处领导
        只需要传入日期selectedDate即可
    '''
    def get(self,request):
        query_dic = request.query_params
        # 1 获取指定的 日期 与 部门id
        target_date = query_dic.get('selectedDate')

        # 2 过滤值班信息表，并去掉user_id为-999的
        # 注意此处有一个bug，现已修改：
        # 过滤的是department的pid为传入的did（查询某个部门的全部的值班信息）
        list = dutyschedule.objects.filter(Q(dutydate=target_date), Q(user__level__lte=2),
                                           ~Q(user_id=-999))
        # 3
        json_list = DutyScheduleSerializer(list, many=True).data
        return Response(json_list)

class ScheduleListView(DutyScheduleBaseView):
    def get(self,request):
        '''
        根据部门id或组id获取人员list
        :param request:
          必须包含：
              user_id，
              group，
              selected_date
          可选：
            （均为数组）
             users_id，
             groups_id
        :return:
        '''
        query_dic=request.query_params
        # 分别获取users_id,groups_id,selected_date
        # 注意前端传过来的使用bootstrap-table get 时传递的data中若为数组会自动在原有名字后面加上一个[]，注意！
        uids=query_dic.get('users_id[]')
        dids=query_dic.get('group_id_new')
        # dids=query_dic.get('groups_id[]')
        target_date=query_dic.get('selected_date')

        # dids=map(lambda x:int(x),dids.split(','))
        dids=[int(temp) for temp in dids.split(',')]
        # uids=map(lambda x:int(x),list(uids))
        uids=[int(temp) for temp in uids.split(',')]

        # dids=list(dids)
        # uids = list(uids)
        # 传入了一组部门
        # 找到对应的部门
        # 返回dutyschedule（值班表）
        # datetime.strptime(target_date,'')
        # convert_date=datetime.strptime(target_date, '%Y-%m-%d')
        schedule_list=self.getMergeScheduleListByDate(dids=dids,target_date=datetime.strptime(target_date, '%Y-%m-%d'))
        # schedule_list=self.getscheduleDetial(dids=dids,target_date=datetime.strptime(target_date, '%Y-%m-%d'))
        # seredule_json = DutyScheduleSerializer(schedule_list, many=True)

        # seredule_json=serializers.serialize("json",schedule_list)
        class Date_Encoder(json.JSONEncoder):
            def default(self, value):
                if isinstance(value, datetime):
                    return value.strftime('%Y-%m-%d %H:%M:%S')
                elif isinstance(value, datetime.date):
                    return value.strftime('%Y-%m-%d')
                else:
                    return value.__dict__
        # seredule_json = json.dumps(schedule_list,skipkeys=True,cls=json_default,ensure_ascii=False, default=lambda obj:obj.__dict__)
        seredule_json = json.dumps(schedule_list,ensure_ascii=False,cls=DateTimeEncoder)

        # return JsonResponse(seredule_json.data)
        print(seredule_json)
        # return JsonResponse(seredule_json)
        return HttpResponse(seredule_json, content_type="application/json")
        # return Response(seredule_json,status=status.HTTP_202_ACCEPTED)
        # return HttpResponse(seredule_json.data)
        # return Response(seredule_json.data)
        # return Response(seredule_json.data)

    def post(self,request):
        ids=request.POST.getlist('id[]',None)
        # id= request.post.get('id',None)
        dutyschedule.objects.filter(id__in=ids).delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ScheduleDelView(DutyScheduleBaseView,R_Department_Duty_BaseView):
    def post(self,request):
        # 1 获取值班日期与group id
        query_dic=request.data
        target_date=query_dic.get('target_date',None)
        did=query_dic.get('group_id',None)
        r_list= self.get_r_list([did])
        # 2 根据日期与部门id查询符合条件的值班信息（多个）
        [dutyschedule.objects.filter(dutydate=datetime.strptime(target_date, '%Y-%m-%d'),
                                        rDepartmentDuty=r).delete() for r in r_list]
        # for r in r_list:
        #     dutyschedule.objects.filter(dutydate=datetime.strptime(target_date, '%Y-%m-%d'),
        #                                 rDepartmentDuty=r).delete()
        # ids = request.POST.getlist('id[]', None)
        # id= request.post.get('id',None)
        return Response(status=status.HTTP_202_ACCEPTED)

class DutyListView(DutyBaseView):
    def get(self,request):
        '''
        根据部门id获取该部门所拥有的的岗位信息
        :param request:
        :return:
        '''
        dids = request.query_params.getlist('group_id')
        duty_list=self.getdutylistbydepartment(dids=dids)
        duty_json=DutySerializer(duty_list,many=True).data
        return Response(duty_json)

from rest_framework.authtoken.models import Token

class CreateUserView(APIView):
    def post(self,request):

        user=User.objects.get(username='admin')

        token=Token.objects.create(user=user)
        print(token.key)
        pass
class DutyDemoView(View):
    def get(self,request):
        return render(request,"index.html")


