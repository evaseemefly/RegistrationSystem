'''
 作业调度框架
'''

import time
from apscheduler.schedulers.blocking import BlockingScheduler

def timerprint_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time()))))

sched=BlockingScheduler()


# 使用cron的方式实现以下两个时间的定时任务
'''
    1、每月的第一天的01:00
    cron表达式：
    sched.add_job(my_job(), 'cron', day=1, hour=1, minute=00)
    2、每天的01:00执行
    cron表达式：
    sched.add_job(my_job(), 'cron', hour=1, minute=00)
'''
# sched.add_job(timerprint_job,'interval',seconds=2)
# 经测试此种方式可行
sched.add_job(timerprint_job,'cron',hour=16, minute=24)
sched.start()