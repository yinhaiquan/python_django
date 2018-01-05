# coding:utf-8

from django.middleware.common import CommonMiddleware


class FilterMiddleware(CommonMiddleware):

    def process_request(self, request):
        print "过滤"
        return None

    def process_response(self, request, response):
        return response