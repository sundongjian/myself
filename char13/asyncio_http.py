# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 15:05

# asyncio 没有提供http协议
# 可以用来aiohttp使用

import asyncio
from urllib.parse import urlparse
import time

async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'
    # asyncio.open_connection 里有register，和多路复用一样，只是封装好了
    reader,writer = await asyncio.open_connection(host,80)
    # write 依然调用了send方法
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
    # async for 直接将for循环异步化
    all_line=[]
    async for raw_line in reader:
        data = raw_line.decode('utf8')
        all_line.append(data)
    html = "\n".join(all_line)
    return html

# 协程一旦完成马上返回结果
async def main():
    tasks = []
    for i in range(20):
        url = 'https://www.baidu.com/'
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in tasks:
        result = await task
        print(result)


if __name__ =="__main__":
    start_time=time.time()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(time.time() - start_time)
