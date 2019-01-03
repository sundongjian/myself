# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 15:42

# 条件变量，用于复杂的线程间同步
# 锁的竞争使得获得锁没有固定顺序
# 其实Condition用的还是lock

from threading import Condition
from threading import Thread
from threading import Lock


class XiaoAi(Thread):
    def __init__(self,cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self):
        # 释放锁
        with self.cond:
            # 等到通知
            self.cond.wait()
            print("在")
            self.cond.notify()
            self.cond.wait()
            print("呵呵")
            self.cond.notify()


class TianMao(Thread):
    def __init__(self, cond):
        super().__init__(name='天猫')
        self.cond = cond

    def run(self):
        # 释放锁
        with self.cond:
            # 也可以self.cond.acquire() 代替with
            # 但是记得最后release
            print("小爱同学")
            # 通知小爱释放锁
            self.cond.notify()
            self.cond.wait()
            print("雷布斯")
            self.cond.notify()


if __name__=="__main__":
    cond = Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)
    # 注意这个地方的启动顺序，需要小爱先启动。wait方法只有notify才能把它唤醒，如果先启动天猫，天猫将notify先发出去了，但是
    # 这时候小爱还没有start起来，启动后由于没收到nofity信号一直阻塞
    xiaoai.start()
    tianmao.start()
    # xiaoai.start()
