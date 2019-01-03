# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 10:50

#
import time
from concurrent.futures import ThreadPoolExecutor,as_completed,wait
from concurrent.futures import Future
# Future 未来对象，task的返回容器。task的执行结果执行状态都会放在Future里面。Future是异步编程的核心


#线程池：可控制的并发，自定义大小
# semaphore只能设置大小。需求：主线程中可以获取某一个任务的状态一级返回值，semaphore无法满足
# 当一个线程完成的时候，主线程能够立即直到状态及返回值
# future可以让多线程和多进程编码接口一致
def get_url(times):
    time.sleep(times)
    print("get_url  {}".format(times))


def get_html(times):
    time.sleep(times)
    print("get_html {}".format(times))
    return times

#
# executor = ThreadPoolExecutor(max_workers=1)
# # 通过submit函数提交执行的函数到线性值，submit是非阻塞的
# task1=executor.submit(get_html,(3))
# task2=executor.submit(ge
# t_html,(2))
# task3=executor.submit(get_html,(1))
# # 判断任务是否执行成功
# print(task1.done())
# # 如果任务在执行中或者已经执行完成无法取消.将线程池改为1就可以取消
# print(task3.cancel())
# time.sleep(4)
# print(task1.done())
# # 阻塞的方法，可以获取task的执行结果
# print(task1.result())



# 要获取已经成功的task
urls = [3,2,4]
executor = ThreadPoolExecutor(max_workers=3)
all_task =[executor.submit(get_html,(url)) for url in urls]
# 阻塞，等待某一任务完成后结束,可以设置时间，过时后无论有没有完成都不再阻塞
wait(all_task)
print('***')

# as_complete是生成器，用到yield
# 遍历已经成功的future
# for future in as_completed(all_task):
#     data = future.result()
#     print("get page {}".format(data))


# 用executor获得已经完成的task
# 和as_complate 区别：不是执行成功后立即打印结果，和urls里顺序一致
# for data in executor.map(get_html,urls):
#     print("get page {}".format(data))

