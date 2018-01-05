'''
    主要用来获取指定路径下的当月的上传的excel文件
'''


import os
import conf.settings

class ExcelOper:
    def __init__(self):
        # ftp根目录
        self.ftpdirpath=conf.settings.FtpSourcePath
        self.__derpartement_dirs=[]
        # self.__length=22
        pass

    @property
    def derpartments(self):
        '''
        获取ftp根目录下的第一级目录，实际就是部门的名称
        :return:
        '''
        # 若没有初始化，需要从指定路径下获取该路径下的全部文件夹名称
        if len(self.__derpartement_dirs)==0:
            self.__derpartement_dirs=os.listdir(self.ftpdirpath)
            return self.__derpartement_dirs

    class DerpartmentData:
        def __init__(self,name,path):
            #ftp根目录
            self.root_dir = path
            #部门名称
            self.name=name
            # self.now_date=now_date

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

        def

        def checkTargetFileExist(self,path):
            '''
            ！！可改为装饰器模式
            :param path:
            :return:
            '''
            # 判断指定文件是否存在
            if os.path.exists(path):
                return True
            else :
                return False


    def getFinalPath(self,now_date):

        pass

    # def getLen(self):
    #     return self.__length


