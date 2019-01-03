# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 19:26
# 1.事件循环 + 回调（驱动生成器）+  epoll（io多路复用）
# asyncio是python自带的
# tornado（实现了web服务器） gevent twisted（scrapy django channels）uwsgi gunicorn uginx
# tornado可以直接部署，nginx+tornado

import asyncio
import time
# partial偏函数
from functools import partial

async def get_html(url):
    print("start")
    # 不能使用time.sleep,这个是同步编程。做数据库驱动、网络驱动一定要有一个异步库去完成异步功能。
    # 比如传统的request库不能做成异步
    await asyncio.sleep(2)
    print("end")
    return 'bobby'

# 如果有参数，必须放在future必须放在最后
def callback(content,future):
    print(content)
    print("send_email_to_baddy")

if __name__=='__main__':
    start_time=time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html('wewerwerwerwer'))
    # 执行完成之后直接执行callback
    task.add_done_callback(partial(callback,'have end ......'))
    loop.run_until_complete(task)
    print(task.result())







