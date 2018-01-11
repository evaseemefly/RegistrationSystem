'''
    主要用来获取指定路径下的当月的上传的excel文件
'''


import os
import conf.settings
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
import datetime
import time
from conf import settings
from core import Persistence

class ExcelOper:
    def __init__(self,source_dir,target_dir):
        # ftp根目录
        # self.ftpdirpath=conf.settings.FtpSourcePath
        self.ftpdirpath = source_dir
        self.savedirpath=target_dir
        self._derpartement_dirs=[]
        # self.__privated_dirs=[]
        # self._protected_dirs=[]
        # self.test_list=[1,2]
        # self.test2_list = []
        # self.__length=22
        pass

    def build(self):
        '''
            遍历符合条件的部门集合：
            读取每一个部门的excel文件
            并最终合并为一个dataframe
            并分别存储至excel与pickle中（本地持久化保存的方式）
        :return:
        '''
        # 当部门dirs集合中有内容时
        # 使用的时间格式必须是datetime.datetime类型！！
        target_date=datetime.datetime.now()
        # target_date=time.localtime(time.time())
        result=None
        if len(self.derpartments)>0:
            # 根据每一个部门的名字拼接处最终的地址
            for derpartment_name in self._derpartement_dirs:
                engineer= self.DerpartmentData_Engineer()
                if result is None:
                    result= engineer.construct_derpartmentData(self,target_date,self.ftpdirpath,derpartment_name)
                else:
                    result=self.merageDataFrame(result,engineer.construct_derpartmentData(self,target_date,self.ftpdirpath,derpartment_name))
        # 分别存储至excel与pickle中
        excel_pers=Persistence.Persistence_Environment(Persistence.Excel_Persistence(result,self.getSavePath(target_date,'excel')))
        excel_pers.make_persistence()
        #
        pickle_pers=Persistence.Persistence_Environment(Persistence.Pickle_Persistence(result,self.getSavePath(target_date,'pickle')))
        pickle_pers.make_persistence()
        return result



    @property
    def derpartments(self):
        '''
        获取ftp根目录下的第一级目录，实际就是部门的名称
        :return:
        '''
        # 若没有初始化，需要从指定路径下获取该路径下的全部文件夹名称
        if len(self._derpartement_dirs)==0:
            self._derpartement_dirs=os.listdir(self.ftpdirpath)
            return self._derpartement_dirs

    class DerpartmentData_Engineer:
        def __init__(self):
            self.builder=None

        def construct_derpartmentData(self,parent,target_date,path,name):
            '''
            部门建造者，由建造者去创建 对象并执行相关的操作
            :return:
            '''
            self.builder=parent.DerpartmentData(name,path)
            '''
                下面执行几个步骤：
                1、获取当前部门所在的文件最终目录
                2、读取目标文件，返回dataframe格式的对象
                3、将需要处理的其他部门对象做如下处理
            '''
            final_path= self.builder.getTargetFilePath(target_date)
            result_dataframe= self.builder.readExcelColumns(final_path,name)
            return result_dataframe


    class DerpartmentData:
        def __init__(self,name,path):
            #ftp根目录
            self.root_dir = path
            #部门名称
            self.name=name
            # self.now_date=now_date

        def build(self):
            pass

        def getTargetFilePath(self,now_date):
            '''
            根据当前时间、根目录以及部门名称获取最终的路径
            :param now_date:
            :return:
            '''
            # Dir / departmentname / yyyy / mm / yyyymm.xls
            str_year=now_date.strftime("%Y")
            str_month=now_date.strftime("%m")
            targetFileName="%s%s.xlsx"%(str_year,str_month)
            targetFilePath=os.path.join(self.root_dir,self.name,str_year,str_month,targetFileName)
            return  targetFilePath
            # pass

        def __validate_columns(self, df):
            '''
            验证columns是否正确
                columns正确：columns中没有空值
            true：验证通过
            false：验证不通过
            :param df:
            :return:
            '''
            if self.isnan(df):
                return False
            else:
                return True

        def __isnan(self, df):
            '''
            判断传入的dataframe是否存在nan值，若存在返回true，不存在返回false
            :param df:
            :return:
            '''
            return True if df.isnull().values.sum() > 0 else False

        def readExcelColumns(self, path,derpartment_name):
            '''
            读取指定文件的头文件
            在本方法执行前需要加入一个装饰器用来判断文件是否存在
            :param path:
            :return:
            '''
            # file_name = 'data/convert_2.xlsx'
            # 1、读取excel中的全部数据
            read_data = pd.read_excel(path, sheetname=0, header=None)

            # 1.1去掉第一列，取剩下的前两行
            '''
             	0 	     1 	     2  	3        4 	     5 	     6
            0 	年 月 日 	风暴潮组 	海浪组 	海浪组 	海浪组 	海冰组 	海冰组
            1 	NaN 	主班 	主班 	副班 	警报班 	主班 	主班
            '''
            read_data[:2]

            # 1.2获取第一列起始至结束；第0行起始至第一行的数据
            '''
             	1 	2 	3 	4 	5 	6
            0 	风暴潮组 	海浪组 	海浪组 	海浪组 	海冰组 	海冰组
            1 	主班 	主班 	副班 	警报班 	主班 	主班
            '''
            columns_names = read_data.iloc[0:2, 1:]

            # 1.3修改columns
            columns_names.columns = np.arange(columns_names.shape[1])

            # 1.4 在组名上面加入一行室名
            columns_department = pd.DataFrame(columns=columns_names.columns, index=[2])

            # 1.5 将columns_names与columns_department合并
            columns_newmerage = pd.merge(columns_names, columns_department, how='outer')

            # 1.6 更新索引，并重新排序
            columns_newmerage.index = [1, 2, 0]
            columns_newmerage = columns_newmerage.sort_index()

            # 1.7 将所有的nan值填充为默认值
            nan_name = derpartment_name
            columns_newmerage = columns_newmerage.fillna(nan_name)

            # 2 获取人员主体dataframe
            read_data[2:-1].head()

            # 重新设置第一列为索引
            convert_data = read_data[2:-1].set_index(0)

            # 3重新赋值columns并通过层次化的方式重新读取数据
            convert_data.columns = [columns_newmerage.loc[0].tolist(), columns_newmerage.loc[1].tolist(),
                                    columns_newmerage.loc[2].tolist()]

            # 返回df
            return convert_data
            # pass

    def merageDataFrame(self,df1,df2):
        '''
        合并两个dataframe
        :param df1:
        :param df2:
        :return:
        '''
        return pd.merge(df1, df2, left_index=True, right_index=True, how='outer')


    def checkTargetFileExist(self, path):
        '''
        ！！可改为装饰器模式
        :param path:
        :return:
        '''
        # 判断指定文件是否存在
        if os.path.exists(path):
            return True
        else:
            return False

    def getSavePath(self,now_date,persistence_type):
        '''
        获取要保存的文件路径
        :param now_date:当前时间
        :param persistence_type:持久化的数据类型（有：excel与Pickle两种）
        :return:
        '''
        # 最后持久化存储的目录（不含文件名）
        finial_dir=os.path.join(self.savedirpath,str(now_date.year))
        # 最终持久化保存的全路径
        finial_filename=None
        str_year=now_date.strftime('%y')
        str_month=now_date.strftime('%m')
        if persistence_type=='excel':
            finial_filename="%s%s%s.csv"%(settings.RESULT_FILE_NAME,str_year,str_month)
        elif persistence_type=='pickle':
            finial_filename = "%s%s%s.pk1" % (settings.RESULT_FILE_NAME, str_year, str_month)

        if finial_filename is not None:
            finial_fullname=os.path.join(finial_dir,finial_filename)
            # 判断指定路径是否存在，不存在则创建
            if os.path.exists(finial_dir)!=True:
                os.mkdir(finial_dir)
            # 判断指定文件是否存在若不存在则创建
            if os.path.isfile(finial_fullname)==False:
                fp = open(finial_fullname, 'w')
                fp.close()
        return finial_fullname
        # pass

    def getSavePath_Pickle(self,now_date):
        pass


    def getFinalPath(self,now_date):

        pass

    # def getLen(self):
    #     return self.__length


