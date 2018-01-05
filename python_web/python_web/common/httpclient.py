#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# urllib2模拟httpclient请求,还有urllib 、httplib等资源包实现post get请求
import json
import urllib2


class HttpClientUtils(object):

    """ http get请求 """
    def sendHttpGet(self):
        rs = urllib2.urlopen("http://blog.csdn.net/allen_hdh/article/details/33713923")
        data = rs.read()
        print data

    def sendHttpPost(self):
        params = {"dappIdList": ['sdfasd']}
        headers = {'Content-Type': 'application/json'}
        request = urllib2.Request(url='http://localhost:8080/plt_api/dapp/queryStatis',
                                  headers=headers, data=json.dumps(params))
        request.add_header('Content-Type', 'application/json')  # 要非常注意这行代码的写法
        rs = urllib2.urlopen(request)
        reponse =  rs.read()
        print reponse

uils = HttpClientUtils()
# uils.sendHttpGet()
uils.sendHttpPost()