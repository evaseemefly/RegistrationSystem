# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/4/17 16:33'

from datetime import datetime

from django.db import models

from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.



class UserInfo(models.Model):
    uid=models.AutoField(primary_key=True)
    username=models.CharField(default='值班员',max_length=20)
    isdel=models.BooleanField(default=False)
    #注意不能使用default=datetime.now
    createdate=models.DateField(auto_now_add=True,null=True)
    modeificateddate=models.DateField(auto_now=True,null=True)
    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username

class DepartmentInfo(models.Model):
    parent_department_choices={
        (1, '数值室'),
        (2, '气象室'),
        (3, '环境室'),
        (4, '预警室')
    }
    did=models.AutoField(primary_key=True)
    pid=models.IntegerField(choices=parent_department_choices)
    derpartmentname=models.CharField(default='默认部门',max_length=20)

    class Meta:
        # 设置了此名称后在xadmin中可以显示该别名
        verbose_name="部门信息"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.derpartmentname

class DutyInfo(models.Model):
    duid=models.AutoField(primary_key=True)
    dutyname=models.CharField(default='主班',max_length=20)
    isdel=models.BooleanField(default=False)
    createdate=models.DateField(auto_now_add=True,null=True)
    modeificateddate=models.DateField(auto_now=True,null=True)

    class Meta:
        verbose_name="值班类别"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.dutyname

class R_DepartmentInfo_DutyInfo(models.Model):
    id=models.AutoField(primary_key=True)
    did=models.ForeignKey(DepartmentInfo,on_delete=models.CASCADE)
    duid=models.ForeignKey(DutyInfo,on_delete=models.CASCADE)
    # desc=models.CharField(default=did.derpartmentname+"-"+duid.dutyname)
    class Meta:
        verbose_name="部门与岗位关系"
        verbose_name_plural=verbose_name
    def __str__(self):
        name=self.did.derpartmentname+"-"+self.duid.dutyname
        return name


class R_AuthUser_Department(models.Model):
    aid=models.ForeignKey(User,verbose_name=u"auth用户",on_delete=models.CASCADE)
    did=models.ForeignKey(DepartmentInfo,verbose_name=u"部门",on_delete=models.CASCADE)



class R_UserInfo_DepartmentInfo(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    did=models.ForeignKey(DepartmentInfo,on_delete=models.CASCADE)

    class Meta:
        verbose_name="人员与部门关系"
        verbose_name_plural=verbose_name

    def __str__(self):
        name=self.did.derpartmentname+"-"+self.uid.username
        return name

class R_Department_User_Simplify(models.Model):
    did=models.IntegerField()
    name=models.CharField()
    uid=models.ForeignKey(UserInfo,on_delete=models.CASCADE)

    class Meta:
        abstract=True

class dutyschedule(models.Model):
    id=models.AutoField(primary_key=True)
    rDepartmentDuty=models.ForeignKey(R_DepartmentInfo_DutyInfo,on_delete=models.CASCADE)
    # 注意需要把auto_now去掉，不然每次修改后都会重修修改该时间
    # dutydate=models.DateField(auto_now=True)
    dutydate = models.DateField()
    # duty=models.ForeignKey(DutyInfo,on_delete=models.CASCADE)
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    # department=models.ForeignKey(DepartmentInfo,on_delete=models.CASCADE)

# class MergeDutyUserInfo(UserInfo,R_DepartmentInfo_DutyInfo):
#     user=models.ManyToManyField(UserInfo)
#     rDepDuty=models.ManyToManyField(R_DepartmentInfo_DutyInfo)

# class DutyUserProxyModel(UserInfo,DutyInfo):
#     class Meta:
#         proxy=True

class DutyScheduleProxyModel(dutyschedule):
    class Meta:
        proxy=True

