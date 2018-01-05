# coding:utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

# 跳转至页面
def hello2(request):
    return render(request, "test.html")

# 带返回参数至页面
def hello3(request):
    list = {1, 2, 3, 4, 5, 6}
    return render(request, "test/test2.html",{'list':list})

# 重定向
# 带参数 reverse('test',arg(a,b))
def hello4(request):
    return HttpResponseRedirect((reverse('test')))
