# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 14:11

import asyncio

def callback(sleep_times,loop):
    print("sleep {}s".format(sleep_times))
    print("loop_time {}".format(loop.time()))

def stoploop(loop):
    loop.stop()

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    now = loop.time()
    # call_soon 立即执行
    # call_soon会立即执行，call_later会根据时间顺序执行
    loop.call_at(now+1,callback, 1,loop)
    loop.call_at(now+3,callback, 3,loop)
    loop.call_at(now+6,callback, 6,loop)
    # run_until_complete在此处不适用
    # loop.call_soon(stoploop, loop)
    loop.run_forever()


