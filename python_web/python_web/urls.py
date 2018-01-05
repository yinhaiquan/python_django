# coding:utf-8
"""python_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from python_web.admin import view as admin
from python_web.admin import view2 as admin2
from db import views as skip
from . import view

# '''
# name 作用 相当于此链接别名，在视图层内部重定向跳转时，可直接使用别名
# '''
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^admin2[/]?$', admin.hello),
    url(r'^admin/get$', admin.hello2),
    url(r'^admin/(\d+)/(\d+)[/]?$', admin.hello3),
    url(r'^test$', admin2.hello2, name="test"),
    url(r'^test2$',admin2.hello3),
    url(r'^test3$',admin2.hello4),
    url(r'^fuck$',admin.fuck),
    url(r'^skip$',skip.skip)
]
