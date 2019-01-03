# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 12:43

import os,time
from celery import Celery

broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'

app= Celery('mytask',broker=broker,backend=backend)

@app.task
def add(x,y):
    print('hhh')
    time.sleep(5)
    return x+y



if __name__=='__main__':
    print('aaa')
    add.delay(2,3)
    print('bbb')
