# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 16:29

# semaphore 使用控制进入数量的锁
#　文件的读写，写一般只能用一个线程来写，读可以允许多个

import threading
import time
class HtmlSpider(threading.Thread):
    def __init__(self,url,sem):
        super().__init__()
        self.url = url
        self.sem = sem


    def run(self):
        time.sleep(2)
        print('get html text')
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self):
        # 防止20个同时进入，3个一组
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider("www.baidu.com",self.sem)
            html_thread.start()

if __name__ == "__main__":
    # SEMaphore 是使用condition完成的
    sem = threading.Semaphore(3)
    url_produce = UrlProducer(sem)
    url_produce.start()
