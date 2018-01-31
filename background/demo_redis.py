'''
 作业调度框架
'''
import time
from datetime import datetime
import os
import logging
import pickle
import redis

def job_load2reids():
    '''
    每天执行一次读取excel并根据当前时间获取当日的数据，并加载至redis中
    :return:
    '''

    # 4.1 序列化
    data="测试测试"
    p1 = pickle.dumps(data)
    print("序列化成功")
    print(str(p1))

    # 4.2 将pickle存储至redis中 并设置过期时间
    r = redis.Redis('127.0.0.1', 6379)
    print("初始化redis成功")

    r.set('test', p1,8540)
    print("写入redis成功")


# def run():
    

def main():
    job_load2reids()

if __name__=='__main__':
    main()
    





