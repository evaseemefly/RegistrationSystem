'''
 作业调度框架
'''

import time
from apscheduler.schedulers.blocking import BlockingScheduler
import apscheduler.schedulers.background
from datetime import datetime
import os
from core import FileInfo
from conf import settings
from core import Common
from core import Persistence
from data import model
import logging
import pickle
import redis

ftpdir = settings.FtpSourcePath
savedir = settings.TARGET_DIR_PATH

def job_timerprint():
    '''
    循环任务
    :return:
    '''
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time()))))



def job_merageExcel():
    '''
    每个月执行一次合并excel
    之前写在main.py中
    :return:
    '''

    temp_date = datetime.now()
    result_targetPath = os.path.join(settings.TARGET_DIR_PATH,
                                     "%s%s.csv" % (temp_date.year, temp_date.month))
    full_name = None
    excel_operate = FileInfo.ExcelOper(ftpdir, savedir)
    result = excel_operate.build()
    str_log="生成文件%s"%result_targetPath
    print(str_log)
    pass

def job_load2reids():
    '''
    每天执行一次读取excel并根据当前时间获取当日的数据，并加载至redis中
    :return:
    '''
    '''
    1:读取指定的pickle文件
    
    '''
    fileinfo= FileInfo.ExcelOper(ftpdir, savedir)

    # 获取当前时间
    now_date =datetime(datetime.now().year,datetime.now().month,datetime.now().day)

    # D:\git仓库\RegistrationSystem\background\result\2017
    file_path=fileinfo.getSavePath(now_date,'pickle')
    factory=Persistence.Persistence_Environment(Persistence.Pickle_Persistence(file_path))
    day_data=factory.read_persistence()
    # # 获取要读取的picklle文件的所在路径
    # targetpickle_name=settings.RESULT_FILE_NAME+"%s%s"%(now_date.strftime('%Y'),now_date.strftime('%m'))+settings.RESULT_FILE_EXT
    # # xxxx/2018/MERAGE_1801
    # targetpickle_path=os.path.join(settings.TARGET_DIR_PATH,now_date.strftime('%Y'),targetpickle_name)
    '''
    2:读取某一日的数据（series）
    '''
    # 需要加入day_data是否为空的判断
    targetday_data = day_data.loc[now_date]

    '''
    3:遍历series每一行的index以及value
    '''
    # targetday_data[0]
    list_person = []
    index = 0
    for temp in targetday_data:
        temp_person = model.Person(temp, targetday_data.index[index][0], targetday_data.index[index][1],
                             targetday_data.index[index][2])
        list_person.append(temp_person)
        print(targetday_data.index[index])
        print(temp)
        print(index)
        index += 1
        print("-----")

    '''
    4:使用pickle进行序列化，并使用redis进行持久化保存
        
    '''
    # 4.1 序列化

    p1 = pickle.dumps(list_person)
    print("序列化成功")
    print(str(p1))

    # 4.2 将pickle存储至redis中 并设置过期时间
    r = redis.Redis(settings.REDIS_IP, settings.REDIS_PORT)
    print("初始化redis成功")

    r.set(settings.NAME_DaySavedInRedis, p1,ex=settings.REDIS_EX)
    print("写入redis成功")


def run():
    sched=BlockingScheduler()
    # 注意使用background.BackgroundScheduler()启动之后只会执行一次就会停止？
    # sched = apscheduler.schedulers.background.BackgroundScheduler()
    # 使用cron的方式实现以下两个时间的定时任务
    '''
        1、每月的第一天的01:00
        cron表达式：
        sched.add_job(my_job(), 'cron', day=1, hour=1, minute=00)
        2、每天的01:00执行
        cron表达式：
        sched.add_job(my_job(), 'cron', hour=1, minute=00)
    '''
    # job1=sched.add_job(job_merageExcel,'cron',day=31, hour=9, minute=5)
    # job1 = sched.add_job(job_merageExcel, 'cron', hour=9, minute=7)
    job_merageExcel()
    # # 经测试此种方式可行
    # job2=sched.add_job(job_load2reids,'cron', hour=9, minute=55)
    # 循坏任务
    # job3=sched.add_job(job_timerprint,trigger='interval', minute=10)
    sched._logger=Common.My_Log(logging.DEBUG,os.path.join(settings.LOG_DIR,'scheduler.log'))
    sched.start()
    # sched.resume()

    # 获取作业列表
    # job_list = sched.get_jobs()
    # for temp_job in job_list:
    #     print("作业:id%s-name:%s已启动"%(temp_job.id,temp_job.name))





