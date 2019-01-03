# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 13:00
from .app import celery_gg
import time

@celery_gg.task
def add():
    print('hhh')
    time.sleep(5)
    # return 'sunjian'

