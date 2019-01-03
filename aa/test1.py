# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 13:09
from app import add
import time


if __name__=='__main__':
    print('aaa')
    result=add.delay(10,20)
    print('bbb')
    time.sleep(8)
    if result.ready():
        print(result.get())
    else:
        time.sleep(5)
        print(result.get())


