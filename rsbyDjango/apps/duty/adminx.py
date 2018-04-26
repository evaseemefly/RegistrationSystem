# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/4/19 14:31'

import xadmin

from .models import DutyInfo,DepartmentInfo,UserInfo,R_DepartmentInfo_DutyInfo,R_UserInfo_DepartmentInfo

class UserInfoAdmin(object):
    list_display=['username','createdate','modeificateddate']

class DutyInfoAdmin(object):
    # 注意不在继承admin，继承自obj
    list_display=['dutyname','createdate','modeificateddate','isdel']
    pass

class DepartmentInfoAdmin(object):
    list_display=['did','pid','derpartmentname']
    pass

class R_DepartmentInfo_DutyInfoAdmin(object):
    list_dislpay=['uid','did']
    pass

class R_UserInfo_DepartmentInfoAdmin(object):
    list_display=['id','did','duid']
    pass

xadmin.site.register(DutyInfo,DutyInfoAdmin)
xadmin.site.register(DepartmentInfo,DepartmentInfoAdmin)
xadmin.site.register(UserInfo,UserInfoAdmin)
xadmin.site.register(R_DepartmentInfo_DutyInfo,R_DepartmentInfo_DutyInfoAdmin)
xadmin.site.register(R_UserInfo_DepartmentInfo,R_DepartmentInfo_DutyInfoAdmin)