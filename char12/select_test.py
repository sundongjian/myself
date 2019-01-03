# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 17:30

import socket
from urllib.parse import urlparse
import time

def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host,80))
    except BlockingIOError:
        pass

    while True:
        try:
            client.send(
                "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))  # 相对路径
            print("send异常")
            break
        except:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1023)
        except BlockingIOError as e:
            continue
        if d:
            data+=d
        else:
            break


if __name__=='__main__':
    now=time.time()
    for i in range(20):
        get_url('http://www.baidu.com')
    print(time.time()-now)









