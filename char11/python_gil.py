# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 12:24


# gil 使得同一个时刻只有一个线程在一个cpu上执行字节码.用java的话，可以将多个线程映射到多个cpu上
# 释放gil，gil会根据执行的字节码函数一级时间片释放gil。比如执行完1000行字节码后自动释放gil，这导致了如果两个线程同时修改一个
# 变量，那么会导致运算错误。如果遇到io操作也会释放

import dis

def add(a):
    a = a+1
    return a

print(dis.dis(add))



