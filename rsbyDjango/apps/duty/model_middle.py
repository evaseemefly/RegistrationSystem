# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/5/10 11:12'

from .models import R_UserInfo_DepartmentInfo,UserInfo,DepartmentInfo

class R_User_Department_Middle(object):
    def __init__(self):
        self.id
        self.user
        self.department

    def ToMiddle(self,r_user_dep):
        '''
        去重，对关系表中的department进行去重
        :param r_user_dep:
        :return:
        '''
        r_list= list(r_user_dep)
        for temp in r_list:
            pass
            # temp.
        pass

        pass
