from .models import dutyschedule,UserInfo,DutyInfo,DepartmentInfo,R_DepartmentInfo_DutyInfo,R_UserInfo_DepartmentInfo
from rest_framework import serializers,viewsets

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields='__all__'

class User_Simplify_Serializer(serializers.ModelSerializer):
    '''
    精简后的user序列化对象，只保留uid以及username
    '''
    uid=serializers.IntegerField()
    username=serializers.CharField()
    class Meta:
        model=UserInfo
        fields=('uid','username')

class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model=DutyInfo
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepartmentInfo
        fields='__all__'

class Department_Simplify_Serializer(serializers.ModelSerializer):
    '''
    精简后的department序列化对象，只保留did,pid,name
    '''
    did=serializers.IntegerField()
    pid=serializers.IntegerField()
    derpartmentname=serializers.CharField()
    class Meta:
        model=DepartmentInfo
        fields = ('did', 'pid','derpartmentname')

class R_Department_DutySerializer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    did=DepartmentSerializer()
    duid=DutySerializer()
    class Meta:
        model=R_DepartmentInfo_DutyInfo
        fields=('id','did','duid')

class R_User_DepartmentSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    uid=UserSerializer()
    did=DepartmentSerializer()

    class Meta:
        model=R_UserInfo_DepartmentInfo
        fields=('id','uid','did')

class R_User_Department_Simplify_Serializer(serializers.ModelSerializer):
    '''
    精简后的关联表
    '''
    id=serializers.IntegerField()
    uid=serializers.SerializerMethodField()
    # uid=User_Simplify_Serializer()
    # uid=serializers.PrimaryKeyRelatedField(required=True,queryset=UserInfo.objects.all())
    # uid=User_Simplify_Serializer()
    did=Department_Simplify_Serializer()

    def get_uid(self,obj):
        '''
        自定义的获取uid的方法
        :param obj:
        :return:
        '''
        # 注意此处的obj.uid是UserInfo，若获取其uid，需要obj.uid.uid

        all_users= UserInfo.objects.filter(uid=obj.uid.uid)
        users_serializer=User_Simplify_Serializer(all_users,many=True)
        return users_serializer.data
    def get_did(self,obj):
        '''
        自定义的获取did的方法
        :param obj:
        :return:
        '''

        pass

    class Meta:
        model=R_UserInfo_DepartmentInfo
        fields=('id','uid','did')

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