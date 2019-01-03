# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 12:41


# 对于io操作来说多线程和多进程性能差距不大
# 线程之间通信
# 共享变量 global 或者直接将变量写在参数
#
#
# 爬虫试验
# 1.共享列表
url_list = []
detail_list = []

import threading
import time
# 如果变量太多，将变量单独放在一个py文件中，非常简单，代码维护起来也简单。但是不要直接导入变量，因为导入变量线程对变量的修改是看不到的
# 线程安全list.pop是不安全的
from char11 import variables

def get_url():
    time.sleep(4)
    print("made get_url")
    for i in range(100):
        variables.url_list.append(i)
        time.sleep(3)


def get_html():
    time.sleep(2)
    print("made get_html")
    while True:
        if len(variables.url_list):
            print(variables.url_list.pop())


if __name__ == '__main__':
    # tmd千万不要忘记加逗号args里
    # get_url 速度大于get_html,可以多开几根get_html线程 用for循环
    # dqueue在线程码的级别上达到线程安全，双端队列
    start = time.time()
    thread1 = threading.Thread(target=get_url)
    thread2 = threading.Thread(target=get_html)
    thread1.start()
    thread2.start()
    print("spending_time {}".format(time.time() - start))


