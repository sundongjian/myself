# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 15:15

#线程同步

# 对锁来说，获得和释放都需要时间，影响性能
# 锁会引起死锁
# 死锁的情况：A线程先后需要ab两个变量，B线程先后需要ba两个变量，A线程获得a变量后释放锁，B线程得到锁，B线程得到b变量后释放锁，
# A线程得到b变量，这时候出问题了，b变量已经被B线程获得并修改了，已经不是之前的b变量了
# 还有一种死锁的情况，一个加锁的线程函数调用另一个加锁的函数（在同一个线程里），会两次acquire锁，然后形成死锁 解决方法：
# 使用 RLock 注意acquire 和 release 次数相等

import threading

# lock = threading.Lock()
lock = threading.RLock()
total = 0

def add():
    global total
    global lock
    for i in range(1000):
        lock.acquire()
        total+=1
        lock.release()

def desc():
    global total
    global lock
    for i in range(1000):
        lock.acquire()
        total -= 1
        lock.release()

t1 = threading.Thread( target=add)
t2 = threading.Thread( target=desc)
t1.start()
t2.start()
t1.join()
t2.join()
print(total)