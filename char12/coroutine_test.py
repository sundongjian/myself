# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 13:54

def gen_func():
    # 可以产出值  可以接收值（接收调用方产生的值)
    html= yield "www.baidu.com"
    print(html)
    yield 2
    yield 3

if __name__=="__main__":
    gen = gen_func()
    # 在调用send发送费none值之前必须先启动一次生成器
    # 启动生成器方式有两种，一种是调用next，一种是send。
    gen.send(None)
    # print(next(gen))
    # send 既可以传送值又可以接收值。接收的值是 = yield下面的一个yield值
    print(gen.send('aaaa'))
    print(next(gen))
