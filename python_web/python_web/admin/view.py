# coding:utf-8
import json
import logging

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import db.models as md
logger = logging.getLogger('demo1')
def hello(request):
    userInfo = {
        'name': '占山',
        'age': 12,
        'email': '108377@qq.com',
        'desc': 'model'
    }
    logging.info('新增用户：')
    logging.debug('debug新增用户：')
    logger.info('新增用户：')
    logger.error('新增用户：')
    md.UserInfo.objects.using('db_mysql').create(**userInfo)
    return HttpResponse("what is the fuck!")

# GET请求 request.GET post请求 request.POST
# http:ip:port/admin/get?a=123&b=123
def hello2(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse(str(a) + '  ' + str(b))

# POST请求
# post请求需要加上@csrf_exempt标签
@csrf_exempt
def fuck(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        print req['a']
        print req['b']
    else:
        req = 'NULL'
    return HttpResponse(req)

# 请求地址带参数
# 采用 /add/3/4/ 这样的网址的方式
def hello3(request,a,b):
    return HttpResponse(str(a) + '  ' + str(b))

