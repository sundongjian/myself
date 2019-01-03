# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 14:40

# 使用多线程：在协程里面不要调用阻塞方式，如果需要拿到线程池中
import asyncio
import time
import socket
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import requests

def get_url(url):
   result = requests.get(url)


if __name__=='__main__':
    now = time.time()
    loop=asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    tasks = []
    for i in range(10):
        task = loop.run_in_executor(executor,get_url,'https://www.baidu.com/')
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print("时间 {}".format(time.time()-now))



