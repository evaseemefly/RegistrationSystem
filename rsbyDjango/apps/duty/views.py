from django.shortcuts import render

# Create your views here.
# 获取指定组的班级情况
from django.views.generic import View
from .models import DutyInfo

class DutyListView(View):
    '''
    班级列表
    '''
    def get(self,request):
        '''
        根据指定的部门id获取班级所拥有的的列表
        :param request:
        :return:
        '''
        json_list=[]
        duty_arr=DutyInfo.objects.filter()

