from django.db import models
from django.contrib.auth import get_user_model
from duty.models import DepartmentInfo
# Create your models here.

User=get_user_model()
# class R_AuthUser_Department(models.Model):
#     id = models.AutoField(primary_key=True)
#     aid = models.ForeignKey(User, verbose_name=u"auth用户", on_delete=models.CASCADE)
#     did = models.ForeignKey(DepartmentInfo, verbose_name=u"部门", on_delete=models.CASCADE)

class R_Author_Department(models.Model):
    id = models.AutoField(primary_key=True)
    aid = models.ForeignKey(User, verbose_name=u"auth用户", on_delete=models.CASCADE)
    did = models.ForeignKey(DepartmentInfo, verbose_name=u"部门", on_delete=models.CASCADE)


class MyTest(models.Model):
    name=models.CharField(default=None,max_length=20)