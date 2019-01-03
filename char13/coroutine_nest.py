# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 12:30

import asyncio
import time

#
# loop = asyncio.get_event_loop()

# run_forever 会一直运行
# run_until_complete 运行完成停止，其实run_until_complete也是使用run_forever,只是加了一个
# 回调函数.add_done_callback 运行完成之后将loop停止
# loop.run_forever()
# loop.run_until_complete()
# loop 会被放到future中
# 取消future(task)


# ctrl_c来关闭task
async def get_html(sleep_time):
    print("waitting")
    await asyncio.sleep(sleep_time)
    print("done {}s".format(sleep_time))

if __name__=="__main__":
    task1 = get_html(1)
    task2 = get_html(2)
    task3 = get_html(5)

    tasks=[task1,task2,task3]

    loop=asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:  # 相当于在外部按下了ctrl——c
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cancel task")
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()

# 协程里面调用子协程
