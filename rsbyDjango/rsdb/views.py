from django.shortcuts import render
from rsdb import models
from django.core.serializers import serialize
from django.http import HttpResponse,HttpResponseRedirect
import json
from Common import MyJsonEncoder
from datetime import datetime
import redis
import pickle
from rsbyDjango import settings
from data import model
import math

# Create your views here.

def home(request):
    return render(request, 'rsdb/index.html')


def getPersonList(request):
    '''
    根据传入的时间获取当日的人员列表
    :param request:
    :return:
    '''
    person_list=[]
    test_list=["stre",1,"444"]
    '''
        此处改为从redis中读取数据，并反序列化
    '''
    # 获取当前页以及页容积
    '''
        eg:page_index=1
            page_count=8
            len_list=15
            page_next=1
            
    '''
    page_index=1
    # 当前页面的页容积
    page_count=int(request.GET.get('pagecount'))
    # 当前页面的编号
    # 1
    page_index=int(request.GET.get('pageindex'))
    page_next=page_index+1
    r = redis.Redis(settings.REDIS_IP, settings.REDIS_PORT)

    data_redis=r.get(settings.NAME_DaySavedInRedis)

    # 反序列化
    person_list=pickle.loads(data_redis)

    # 对list进行分页
    # 1、获取长度
    len_list=len(person_list)
    # 判断前台传过来的page_index+1是否大于总页数
    '''
    len_list=12
    page_count=6
    len_list/page_count=2
    
    page_index+1=2
    
    此处判断为：
        当前的页码不是未超过页码的最大值    
    '''

    person_skiplist=[]

    if page_index< math.ceil(len_list/page_count):
        # 下一页不是最终页
        if page_next != math.ceil(len_list / page_count):
            # page_index += 1
            # page_next=page_index
            # 2、跳过部分
            '''
                (page_index)*page_count  =2*6=12
                (page_index-1)*page_count=(2-1)*6=6
            '''
            person_skiplist = person_list[(page_next - 1) * page_count:page_count]
        # 若是最终页，切片选取时，只能使用[num1:]的方式
        else:
            person_skiplist=person_list[(page_next - 1) * page_count:]
    # 若当前页码时最后一页，则下一页改为第一页
    elif page_index==math.ceil(len_list/page_count):
        page_next=1
        person_skiplist = person_list[(page_next - 1) * page_count:page_count]
    # page_next=page_index
    # 测试用，已注释
    # for p in range(1,5):
    #     person_list.append(models.Person("预报员%s"%str(p),"预警室","风暴潮","主班"))

    # dict_json = dict(person_list)
    # test_data=serialize("json",test_list)
    # 此种方式对于集合不可用
    # test_json=json.dumps(person_list,cls=MyJsonEncoder)
    '''
        使用
        
    '''
    data=json.dumps(person_skiplist,default=lambda obj:obj.__dict__,ensure_ascii=False)
    # test_json=json.dumps(test_list)
    # data=json.dumps(dict_json)
    # data=serialize("json",person_list)
    dict_data={"now_date":datetime.now().strftime('%y-%m-%d'),"persons":person_skiplist,"pageindex":page_next,"listcount":len_list}
    test_json=json.dumps(dict_data,default=lambda obj:obj.__dict__,ensure_ascii=False)
    return HttpResponse(test_json,content_type="application/json")

