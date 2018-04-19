# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/4/19 14:31'

import xadmin

from .models import DutyInfo,DepartmentInfo


class DutyInfoAdmin(object):
    # 注意不在继承admin，继承自obj
    list_display=['dutyname','createdate','modeificateddate','isdel']
    pass

class DepartmentInfoAdmin(object):
    list_display=['did','pid','derpartmentname']
    pass

xadmin.site.register(DutyInfo,DutyInfoAdmin)
xadmin.site.register(DepartmentInfo,DepartmentInfoAdmin)