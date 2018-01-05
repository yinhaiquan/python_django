#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# redis单节点操作
#  具体操作介绍：http://www.cnblogs.com/melonjiang/p/5342505.html

import redis

# redis单例实现
class RedisModel(object):
    HOST = '127.0.0.1'
    PORT = 6379
    DBID = 0
    def __init__(self):
        if not hasattr(RedisModel, 'pool'):
            RedisModel._create_pool()
        self.conn = redis.Redis(connection_pool=RedisModel.pool)

    # python中，所有类的实例中的成员变量，都是公用一个内存地址，因此，及时实例化多个RedisCache类，内存中存在的pool也只有一个
    @staticmethod
    def _create_pool():
        RedisModel.pool = redis.ConnectionPool(
            host=RedisModel.HOST,
            port=RedisModel.PORT,
            db=RedisModel.DBID)

# 给对象动态添加属性
RedisModel.fk = 123
print RedisModel.fk
rt = RedisModel()
# 给对象的属性赋值，若属性不存在，先创建再赋值
setattr(rt,"fk",555)
print rt.fk
print RedisModel().conn.info()

# 获取普通redis连接
r = redis.Redis(host="localhost", port=6379, db=0)
# print r.info()

# 配置连接池，从中获取连接
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r2 = redis.Redis(connection_pool=pool)
# print r2.info()

"""
#在Redis中设置值，默认不存在则创建，存在则修改
r.set('name', 'zhangsan')
参数：
     set(name, value, ex=None, px=None, nx=False, xx=False)
     ex，过期时间（秒）
     px，过期时间（毫秒）
     nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
     xx，如果设置为True，则只有name存在时，当前set操作才执行
"""


def setString(key, value):
    r.set(key, value)


def getString(key):
    print r.get(key)


setString("fuck", "what is the fuck?")
getString("fuck")
