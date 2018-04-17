# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/4/17 16:33'
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uid=models.AutoField(primary_key=True)
    username=models.CharField(default='值班员',max_length=20)
    isdel=models.BooleanField()
    createdate=models.DateField(auto_now_add=True)
    modeificateddate=models.DateField(auto_now=True)

class DepartmentInfo(models.Model):
    did=models.AutoField(primary_key=True)
    pid=models.IntegerField()
    derpartmentname=models.CharField(default='默认部门',max_length=20)

class DutyInfo(models.Model):
    duid=models.AutoField(primary_key=True)
    dutyname=models.CharField(default='主班',max_length=20)

class dutyschedule(models.Model):
    id=models.AutoField(primary_key=True)
    dutydate=models.DateField(auto_now=True)

class R_UserInfo_DepartmentInfo(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    did=models.ForeignKey(DepartmentInfo,on_delete=models.CASCADE)

class R_DepartmentInfo_DutyInfo(models.Model):
    id=models.AutoField(primary_key=True)
    did=models.ForeignKey(DepartmentInfo,on_delete=models.CASCADE)
    duid=models.ForeignKey(DutyInfo,on_delete=models.CASCADE)