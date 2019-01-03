# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 12:09

# wait 和 gather区别

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
    print(url)
    print("start")
    # 不能使用time.sleep,这个是同步编程。做数据库驱动、网络驱动一定要有一个异步库去完成异步功能。
    # 比如传统的request库不能做成异步
    await asyncio.sleep(2)
    print("end")
    return 'bobby'


if __name__=='__main__':
    # start_time=time.time()
    # loop = asyncio.get_event_loop()
    # tasks=[get_html(i) for i in range(10)]
    # # get_feature=asyncio.ensure_future(asyncio.wait(tasks))
    # get_feature = asyncio.ensure_future(asyncio.gather(*tasks))
    # loop.run_until_complete(get_feature)
    # gather 和 wait 的区别
    # gather更加高层，除了可以完成上面的功能，还可以分组

    # loop = asyncio.get_event_loop()
    # tasks1 = [get_html('www.baidu') for i in range(2)]
    # tasks2 = [get_html('www.muke') for i in range(3)]
    # get_feature = asyncio.ensure_future(asyncio.gather(*tasks1,*tasks2))
    # loop.run_until_complete(get_feature)


    loop = asyncio.get_event_loop()
    tasks1 = [get_html('www.baidu') for i in range(2)]
    tasks2 = [get_html('www.muke') for i in range(3)]
    group1 = asyncio.gather(*tasks1)
    group2 = asyncio.gather(*tasks2)
    get_feature = asyncio.ensure_future(asyncio.gather(group1, group2))
    loop.run_until_complete(get_feature)























