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

def job_timerprint():
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
    ftpdir = settings.FtpSourcePath
    savedir = settings.TARGET_DIR_PATH
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

    pass

def run():
    # sched=BlockingScheduler()
    sched = apscheduler.schedulers.background.BackgroundScheduler()
    # 使用cron的方式实现以下两个时间的定时任务
    '''
        1、每月的第一天的01:00
        cron表达式：
        sched.add_job(my_job(), 'cron', day=1, hour=1, minute=00)
        2、每天的01:00执行
        cron表达式：
        sched.add_job(my_job(), 'cron', hour=1, minute=00)
    '''
    job1=sched.add_job(job_merageExcel,'cron',day=1, hour=1, minute=00)
    # # 经测试此种方式可行
    job2=sched.add_job(job_load2reids,'cron', hour=1, minute=00)
    sched.start()
    # sched.resume()

    # 获取作业列表
    job_list = sched.get_jobs()
    for temp_job in job_list:
        print("作业:id%s-name:%s已启动"%(temp_job.id,temp_job.name))


pass




