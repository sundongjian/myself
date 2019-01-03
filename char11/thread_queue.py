# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 12:41


# 对于io操作来说多线程和多进程性能差距不大
# 线程之间通信
# 共享变量 global 或者直接将变量写在参数
#
#
# 爬虫试验
# 1.共享列表
url_list=[]
detail_list = []

import threading
import time

def get_url(url_list):
    time.sleep(4)
    print("made get_url")
    for i in range(100):
        url_list.append(i)
        time.sleep(3)



def get_html(url_list):
    time.sleep(2)
    print("made get_html")
    while True:
        if len(url_list):
            print(url_list.pop())



if __name__ =='__main__':
    # tmd千万不要忘记加逗号args里
    # get_url 速度大于get_html,可以多开几根get_html线程 用for循环
    start = time.time()
    thread1 = threading.Thread(target=get_url,args=(url_list,))
    thread2 = threading.Thread(target=get_html,args=(url_list,))
    thread1.start()
    thread2.start()
    print("spending_time {}".format(time.time()-start))


