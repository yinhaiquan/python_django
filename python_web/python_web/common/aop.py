#!/usr/bin/env python
# coding:utf-8

'''
python实现aop

利用contextlib实现AOP
'''
from contextlib import contextmanager


@contextmanager
def AOPfunc(name):
    print ("before:")
    yield
    print ("after:")


def process_1():
    print ("process_1")

def process_2():
    print ("process_2")

def process_3():
    print ("process_3")

def Main():
    with AOPfunc("aop"):
        process_1()
        process_2()

    with AOPfunc("aop2"):
        process_3()

if __name__ == '__main__':
    Main()
