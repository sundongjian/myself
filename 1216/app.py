# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 13:00

# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 12:43

import os,time
from celery import Celery

broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'

celery_gg= Celery('app',broker=broker,backend=backend)


# @celery_gg.task
# def add():
#     print('hhh')
#     time.sleep(5)