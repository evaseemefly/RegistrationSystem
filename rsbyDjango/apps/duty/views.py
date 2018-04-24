from django.shortcuts import render

# Create your views here.
# 获取指定组的班级情况
from django.views.generic import View
from .models import DutyInfo
from datetime import datetime


class DutyListView(View):
    '''
    班级列表
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
        if targetmonth=='':
            targetmonth=datetime.now()
        # 分别获取指定日期的年和月
        search_year=targetmonth.year
        search_month=targetmonth.month

        json_list=[]
        duty_arr=DutyInfo.objects.filter(duid=1)


