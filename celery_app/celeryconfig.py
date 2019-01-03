# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 15:28
import datetime
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/1'
BACKEND_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_TIMEZONE='Asia/Shanghai'

CELERY_IMPORTS=(
    'celery_app.task1',
    'celery_app.task2',
)

CELERYBEAT_SCHEDULE={
    'task1':{
    'task':'celery_app.task2.add',
    'schedule':datetime.timedelta(seconds=5),
    'args':(2,8)},
    # 'task2':{
    # 'task':'celery_app.task2.add',
    # 'schedule':crontab(hour=16,minute=55),
    # 'args':(2,8)}
}
