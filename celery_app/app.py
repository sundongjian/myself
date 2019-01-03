# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 13:00

# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 12:43

import os
import sys
sys.path.append(os.path.abspath('.'))


from celery_app import task1
from celery_app import task2

task1.mult.delay(2,3)
task2.add.delay(3,4)
print('end......')
