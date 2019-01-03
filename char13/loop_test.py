# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 19:26
# 1.事件循环 + 回调（驱动生成器）+  epoll（io多路复用）
# asyncio是python自带的
# tornado（实现了web服务器） gevent twisted（scrapy django channels）uwsgi gunicorn uginx
# tornado可以直接部署，nginx+tornado

import asyncio
import time

async def get_html(url):
    print("start")
    # 不能使用time.sleep,这个是同步编程。做数据库驱动、网络驱动一定要有一个异步库去完成异步功能。
    # 比如传统的request库不能做成异步
    await asyncio.sleep(2)
    print("end")
    return 'bobby'

def callback(future):
    print("send_email_to_baddy")

if __name__=='__main__':
    start_time=time.time()
    loop = asyncio.get_event_loop()

    # loop.create_task() 是loop自带的返回功能，与上相同
    # tasks=[get_html(i) for i in range(10)]
    # get_feature=asyncio.ensure_future(asyncio.wait(tasks))
    # loop.run_until_complete(get_feature)
    # print(time.time()-start_time)
    # print(get_feature.result())

    # ensuer_future如何和loop产生关系的？在ensure_future中，先要get_event_loop,一个线程中只有一个loop，就是当前的loop
    get_feature = asyncio.ensure_future(get_html('wewerwerwerwer'))
    loop.run_until_complete(get_feature)
    print(get_feature.result())

    # get_feature = loop.create_task(get_html('wewerwerwerwer'))
    # loop.run_until_complete(get_feature)
    # print(get_feature.result())







