# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 17:30

import socket
from urllib.parse import urlparse
import time
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import select

selector = DefaultSelector()


class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode(
                'utf8'))  # 相对路径
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        data = b""
        # 12-4 三分钟左右，这一段没弄懂
        # 当变得readable的时候并不代表我们可以不停从内核空间拷贝数据到内核空间，因为变得readable并不代表数据全部接受完成了，再次调用的
        # 时候内存空间不一定准备好，再次调用就会BlockingIOError。去掉循环，因为只要刻度就会继续调用io循环
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data=data.split("\r\n\r\n")[1]

            self.client.close()



    def get_url(self, url):
        self.url = urlparse(url)
        self.host = self.url.netloc
        self.path = self.url.path
        self.data = b""
        if self.path == "":
            self.path = '/'
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # select本身不支持register模式，selector是对select进行封装了，所以可以完成register
    # socket 状态变化的回调是程序完成的
    # 事件循环，不停请求socket的状态邠调用对应的回调
    while True:
        # 当没有任务的时候在windows上会报错，linux会一直阻塞。因为在linux上使用的是epoll,windows使用的是select
        try:
            ready = selector.select()
            for key,mask in ready:
                call_back = key.data
                call_back(key)
        except:
            print('结束')
            break


if __name__ == '__main__':
    # tornado  gevent等都用了io复用，select
    now = time.time()
    for i in range(0,20):
        fetcher = Fetcher()
        fetcher.get_url('http://www.baidu.com')
    loop()
    print('运行时间：{}'.format(time.time()-now))
