# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 12:41


# 对于io操作来说多线程和多进程性能差距不大


import threading
import time

def get_url(url):
    print(url)
    time.sleep(4)
    print("get_url")


def get_html(url):
    print(url)
    time.sleep(2)
    print("get_html")


if __name__ =='__main__':
    # tmd千万不要忘记加逗号args里
    start = time.time()
    thread1 = threading.Thread(target=get_url,args=("www.baidu.com",))
    thread2 = threading.Thread(target=get_html,args=("www.gg.com",))
    # setDaemon守护线程，当主线程退出时，义无反顾将子线程退出
    # setDaemon 当多个线程，只有设置了setDaemon的线程是守护线程（主线程关闭马上关闭）
    thread1.setDaemon(True)
    # thread2.setDaemon(True)
    thread1.start()
    thread2.start()
    # join 阻塞主线程
    # thread1.join()
    # thread2.join()
    print("spending_time {}".format(time.time()-start))


