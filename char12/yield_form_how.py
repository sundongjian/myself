
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 17:19

# yield from 需要处理的异常
# 子生成器可能只是一个迭代器，并不是一个作为协程的生成器，说哟它不支持close和throw方法
# 如果有throw和close方法，那但在生成器内部，也会抛异常
# 调用方让子生成器自己抛异常
# 当调用方使用next()或者send（None）时，都要在子生成器next（）函数，当调用send发送费none值时，才调用子生成器的send方法
import types

finual_result={}

# 加上装饰器又可以快乐的用装饰器了
@types.coroutine
def gen(pro_name):
    total=0
    num=[]
    while True:
        x = yield
        print("{}+销量{}".format(pro_name,x))
        if not x:
            break
        total += x
        num.append(x)
    return total,num


async def middle(key):
    while True:
        finual_result[key] = await gen(key)
        print("统计{}".format(key))

def main():
    data = {
        'mon':[100,200,300],
        'the':[100,200,400],
        'wed':[100,200,500],
    }
    for key,values in data.items():
        print('start {}'.format(key))
        m=middle(key)
        m.send(None)
        for value in values:
            m.send(value)
        m.send(None)
    print('finual_result {}',finual_result)


main()