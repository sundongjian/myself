# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 15:30
import os
import sys
sys.path.append(os.path.abspath('.'))
from celery_app import app
import time

@app.task
def add(x,y):
    time.sleep(5)
    return x*y
