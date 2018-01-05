#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import unittest

import sys
from django.test import TestCase
import db.models as models

# 测试单元编写
reload(sys)
sys.setdefaultencoding("utf-8")


# Create your tests here.

# 测试类
class UserInfoTest(TestCase):
    # 跳过该方法不执行skip()里面内容可以随便填写
    @unittest.skip("skip")
    def test_findUserInfo(self):
        print '007'
        print models.UserInfo.objects.all()

    @unittest.skip("123")
    def test_insertUserInfo(self):
        userInfo = {
            'name': '占山',
            'age': 12,
            'email': '108377@qq.com',
            'desc': 'model'
        }
        models.UserInfo.objects.using('db_mysql').create(**userInfo)
        print 'mysql数据库内容：'
        print models.UserInfo.objects.using('db_mysql').all()[0]
        print '默认数据库sqlite内容：'
        print models.UserInfo.objects.all()
        print 123

# 测试单元入口
if __name__ == '__main__':
    unittest.main()
