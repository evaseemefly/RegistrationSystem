import os
from core import FileInfo
from conf import  settings
from datetime import datetime
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
from conf import settings as st
from core import Persistence
from core import Scheduler


def main():

    '''
        2018-1-14 测试作业调度
    :return:
    '''

    '''
    1、读取并合并当月的所有部门的相关dataframe并生成合并后的dataframe并使用excel与pickle进行持久化保存
    2018-1-14 测试作业调度暂时注释掉（有用）
    ！！根据指定的时间手动处理该月的excel并合并成csv及pickle文件！！
    :return:
    '''
    # temp_date=datetime(2018,1,1)
    # # result_targetPath = os.path.join(settings.TARGET_DIR_PATH,
    # #                           "%s%s.csv" % (temp_date.year, temp_date.month))
    # ftpdir=st.FtpSourcePath
    # savedir=st.TARGET_DIR_PATH
    # full_name=None
    # excel_operate =FileInfo.ExcelOper(ftpdir,savedir)
    # result= excel_operate.build()


    '''
    2、定时从本地指定路径下读取excel（或pickle）文件，过滤某一日的一行数据
       加载至缓存中
    '''
    # excel_instance= Persistence.Excel_Persistence(result,full_name)
    #
    # # 测试可行
    # pickle_instance=Persistence.Pickle_Persistence(result,r'C:\Users\evase\Documents\git仓库\RegistrationSystem\result\pk1.pk1')
    # pickle_instance.to_persistence()
    # pickle_result=pickle_instance.read_persistence(r'C:\Users\evase\Documents\git仓库\RegistrationSystem\result\pk1.pk1')

    '''
    2018-1-15:
    改为作业调度的方式启动
    '''
    Scheduler.run()
    # pass
    # result.to_csv(result_targetPath)

    # excel_oper= FileInfo.ExcelOper()
    # derpartements=excel_oper.derpartments
    # length=excel_oper.getLen()
    # pass



if __name__=='__main__':
    main()