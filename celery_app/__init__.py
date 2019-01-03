# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 15:27

import time

from celery import Celery

app=Celery('demo')
app.config_from_object('celery_app.celeryconfig')

