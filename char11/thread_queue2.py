# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 12:41


# 通过queue的方式进行通信
from queue import Queue
import threading
import time

def get_url(url_list):
    time.sleep(4)
    print("made get_url")
    for i in range(100):
        # put_nowait 和 get_nowait都是调用了put方法，只不过加了一个参数block=false
        # 加了参数后变成非阻塞的，当队列已满时候，不插入，直接抛出queue.Full的异常后继续运行
        # 也可以设置time_out 当阻塞时间超过时候报queue.Full错
        url_list.put(i)
        time.sleep(3)

        # url_list.put_nowait(i)
        # time.sleep

        # url_list.put(i,timeout=1)
        # time.sleep(1)


def get_html(url_list):

    print("made get_html")
    while 1:
        # get方法是阻塞的方法，如果队列为空会一直阻塞，符合我们期望
        time.sleep(2)
        # get_nowait
        url = url_list.get()
        print(url)
        if url>4:
            url_list.task_done()
            print("task_done")


if __name__ =='__main__':
    # tmd千万不要忘记加逗号args里
    # get_url 速度大于get_html,可以多开几根get_html线程 用for循环
    start = time.time()
    # 设置一个最大值，否则对内存造成过度占用
    url_list = Queue(maxsize=100)
    thread1 = threading.Thread(target=get_url,args=(url_list,))
    thread2 = threading.Thread(target=get_html,args=(url_list,))
    thread1.start()
    thread2.start()


    # join 会一直阻塞，如果要取消阻塞，需要再某个地方加上task_done,比如爬满100个url   http://www.vuln.cn/8610
    # url_list.join()

    print("spending_time {}".format(time.time()-start))


