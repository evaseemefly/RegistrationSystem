from django.shortcuts import render
from rsdb import models
from django.core.serializers import serialize
from django.http import HttpResponse,HttpResponseRedirect
import json
from Common import MyJsonEncoder
from datetime import datetime


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
    for p in range(1,5):
        person_list.append(models.Person("预报员%s"%str(p),"预警室","风暴潮","主班"))
    # dict_json = dict(person_list)
    # test_data=serialize("json",test_list)
    # 此种方式对于集合不可用
    # test_json=json.dumps(person_list,cls=MyJsonEncoder)
    '''
        使用
    '''
    data=json.dumps(person_list,default=lambda obj:obj.__dict__,ensure_ascii=False)
    # test_json=json.dumps(test_list)
    # data=json.dumps(dict_json)
    # data=serialize("json",person_list)
    dict_data={"now_date":datetime.now().strftime('%y-%m-%d'),"persons":person_list}
    test_json=json.dumps(dict_data,default=lambda obj:obj.__dict__,ensure_ascii=False)
    return HttpResponse(data,content_type="application/json")

