# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 14:11

import asyncio

def callback(sleep_times):
    print("sleep {}s".format(sleep_times))

def stoploop(loop):
    loop.stop()

if __name__=='__main__':
    # loop=asyncio.get_event_loop()
    # # call_soon 立即执行
    # loop.call_soon(callback,2)
    # # run_until_complete在此处不适用
    # loop.call_soon(stoploop,loop)
    # loop.run_forever()

    loop = asyncio.get_event_loop()
    # call_soon 立即执行
    # call_soon会立即执行，call_later会根据时间顺序执行
    loop.call_later(1,callback, 1)
    loop.call_later(3,callback, 3)
    loop.call_later(6,callback, 6)
    # run_until_complete在此处不适用
    # loop.call_soon(stoploop, loop)
    loop.run_forever()

