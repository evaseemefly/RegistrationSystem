from .models import dutyschedule,UserInfo,DutyInfo,DepartmentInfo,R_DepartmentInfo_DutyInfo
from rest_framework import serializers,viewsets

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields='__all__'

class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model=DutyInfo
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepartmentInfo
        fields='__all__'

class R_Department_DutySerializer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    did=DepartmentSerializer()
    duid=DutySerializer()
    class Meta:
        model=R_DepartmentInfo_DutyInfo
        fields=('id','did','duid')


class DutyScheduleSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField ()
    rDepartmentDuty=R_Department_DutySerializer()
    dutydate=serializers.DateField()
    user=UserSerializer()
    class Meta:
        model=dutyschedule
        fields=('id','dutydate','user','rDepartmentDuty')

    # class Meta:
    #     model=dutyschedule
    #     fields='__all__'