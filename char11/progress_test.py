# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 12:17

# 耗cpu的操作因为线程有一把gil锁的存在
# 对于io操作来说，瓶颈不再cpu，使用多线程
# 进程切换的代价高于线程
# 显卡gpu速度高于cpu

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
 #接口将Thread换成Process就行

import os
import time

print("fuck")
pid=os.fork()
print('boddy')
if pid ==0:
    print("子进程{} 父进程{}".format(os.getpid(),os.getppid()))
else:
    print("我是父进程 {}".format(pid))

# time.sleep(2)


'''
结果：
boddy
我是父进程 15302
boddy
子进程15302 父进程15301

多进程和多线程完全不同，多进程会完全拷贝运行文件的数据，这份数据是独立出来的
进程数据完全隔离，每个进程是隔离的
子进程从fork处开始执行
'''
