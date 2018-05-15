# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/5/10 11:12'

from .models import R_UserInfo_DepartmentInfo,UserInfo,DepartmentInfo,R_Department_User_Simplify
from .serializers import R_Department_User_Simplify_Serializer

class R_User_Department_Middle(object):
    def __init__(self):
        pass
        # self.id
        # self.user
        # self.department

    def ToMiddle(self,r_user_dep):
        '''
        去重，对关系表中的department进行去重
        :param r_user_dep:
        :return:
        '''
        class User_Department_Middle(object):
            def __init__(self):
                self.uid=[]
                self.name=None
                self.did=None
        class User(object):
            def __init__(self,uid,name):
                self.uid=uid
                self.username=name

        r_list= list(r_user_dep)
        finial_list=[]
        # 向r_list第一位插入-1
        common_obj=User_Department_Middle()

        # r_list.insert(0,)
        # 注意此处训话时，会提示ListSerializer是不可迭代的
        # 解决：是因为传入的是序列化之后的对象
        for temp in r_user_dep:
            '''
                1 取出gid，判断gid.gid是否在finial_list中    
            '''
            temp_obj=User_Department_Middle()
            temp_obj.did=temp.did.did
            temp_obj.name=temp.did.derpartmentname
            # 判断当前did.did是否存在于finial_list中，不存在则插入
            match_list=[temp_list for temp_list in finial_list if temp_list.did==temp.did.did]
            user_temp = User(temp.uid.uid, temp.uid.username)
            if len(match_list)==0:
            # if finial_list.index(temp.did.did)<0:
                # 向temp_obj中插入当前的match_list的user
                temp_obj.uid.append(user_temp)
                finial_list.append(temp_obj)
            else:
                index=finial_list.index(match_list[0])
                obj=finial_list.pop(index)
                obj.uid.append(user_temp)
                finial_list.append(obj)
            print(temp)
            # temp

        return finial_list

    def ToMiddleSerializer(self,r_user_dep):
        class User_Department_Middle(object):
            def __init__(self):
                self.uid=[]
                self.name=None
                self.did=None

        r_list= list(r_user_dep)
        finial_list=[]
        # 注意此处训话时，会提示ListSerializer是不可迭代的
        # 解决：是因为传入的是序列化之后的对象
        for temp in r_user_dep:
            '''
                1 取出gid，判断gid.gid是否在finial_list中    
            '''

            temp_obj=R_Department_User_Simplify()
            temp_obj.did=temp.did.did
            temp_obj.name=temp.did.derpartmentname
            # 判断当前did.did是否存在于finial_list中，不存在则插入
            match_list=[temp_list for temp_list in finial_list if temp_list.did==temp.did.did]
            if len(match_list)==0:
            # if finial_list.index(temp.did.did)<0:
                # 向temp_obj中插入当前的match_list的user
                '''
                    ！！！！注意此处存在逻辑性的错误!!!!!
                    因为uid在R_Department_User_Simplify中是作为一个外键来使用，
                    也就是说一行数据中，该值只能对应一个值，所以不能转换为一个数组
                    所以，此处不能使用此种方式
                '''
                temp_obj.uid=[temp.uid]
                # temp_obj.uid.append(temp.uid)
                finial_list.append(temp_obj)
            else:
                index=finial_list.index(match_list[0])
                obj=finial_list.pop(index)
                obj_arr=obj.uid
                obj_arr.append(temp.uid)

                # obj.uid.append(temp.uid)
                finial_list.append(obj_arr)
            print(temp)
            # temp

        return finial_list

