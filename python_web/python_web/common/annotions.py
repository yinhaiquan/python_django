#!/usr/bin/env python
# coding:utf-8

# python @ 修饰符 类似java中的注解

import atexit


# *  ** 区别

def exit0(*args,**kw):
    print 'exit0'
    print args
    print kw
kw = {}
exit0(123,'sdfsd','sdf234',kw)
print '-----------------------'
exit0(123,('sdfsd','sdf234'),kw)
print '-----------------------'
exit0(123,*('sdfsd','sdf234'),**kw)

# 单例注解
import string
from numbers import Number

# ***********************************************分割线-单例修饰器**********************************************
def singleton(cls):
    instances = {}
    print cls
    print cls()
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

# 单例注解使用
@singleton
class MyClass:
    def main(self):
        print 123

# 测试方法
# t = MyClass();
# print t
# t2 = MyClass();
# print t2

# *******************************************分割线-日志修饰器***********************************************
'''
# 日志注解，不带参数修饰器
'''
def log(f):
    def fn(*args,**kw): # 内嵌函数，保证每个线程调用都是重新绑定函数
        print "【%s】入参：%s" % (f.func_name, str(args)+str(kw))
        res = f(*args,**kw) # 执行函数，并获取结果
        print "【%s】输出结果:%s" %(f.func_name,res)
        return res # 返回结果
    return fn #执行内嵌函数

@log
def decorator0(name,age):
    return str(age)+name

@log
def decorator2(*args,**kwargs):
    return str(kwargs)+str(args)

@log
def decorator1():
    print 123

# 测试方法
# print decorator0("sdf",123)
# print decorator2((1,2,3),{'name':"sdf",'sdf':"sdf",'234':"sdf"})
# print decorator2({'name':"sdf",'sdf':"sdf",'234':"sdf"})
# print decorator2((1,2,3))
# decorator1()

'''
# 日志注解，带参数修饰器
'''
def log2(desc):
    def log(f):
        def fn(*args,**kw): # 内嵌函数，保证每个线程都是调用各自的函数
            print "调用方法名称: %s" % desc
            print "【%s】入参：%s" % (f.func_name, str(args)+str(kw))
            res = f(*args,**kw) # 执行函数，并获取结果
            print "【%s】输出结果:%s" %(f.func_name,res)
            return res # 返回结果
        return fn #执行内嵌函数
    return log

@log2("测试带参数修饰器")
def decorator4():
    print 123

decorator4()