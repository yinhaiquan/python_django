#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 多线程


import threading

import time
from multiprocessing.dummy import Pool as ThreadPool

# 线程锁
lock = threading.RLock()

# 方式一 ： 通过继承threading.Thread新建线程
class TestThread(threading.Thread):
    __args = None
    def run(self):
        lock.acquire(); # 获得锁
        time.sleep(1)
        print self.__args
        lock.release(); # 释放锁

    def __init__(self, args):
        self.__args = args
        super(TestThread, self).__init__()

# for index in xrange(10):
#     t = TestThread(index)
#     t.start()

# 方式二 ： 定义方法
def testRun(arg):
    lock.acquire();  # 获得锁
    time.sleep(1)
    print arg
    lock.release();  # 释放锁

# for index in xrange(5):
#     t = threading.Thread(target=testRun,args=(index,))
#     t.start()

# 线程池使用
pool = ThreadPool(6)
for i in xrange(8):
    msg = 'hello %d' %(i)
    pool.apply_async(func=testRun,args=(msg,))
pool.close()
pool.join()