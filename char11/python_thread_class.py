# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 12:41


# 对于io操作来说多线程和多进程性能差距不大


import threading
import time

class GetUrl(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        time.sleep(4)
        print("get_url {}".format(self.name))

class GetHtml(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    # run可以覆盖父类方法
    def run(self):
        time.sleep(2)
        print("get_html")
        print("get_html {}".format(self.name))


if __name__ =='__main__':
    # tmd千万不要忘记加逗号args里
    start = time.time()
    thread1 = GetUrl('baidu')
    thread2 = GetHtml('google')
    thread1.start()
    thread2.start()
    print("spending_time {}".format(time.time()-start))


