# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 15:31

from itertools import chain

# mylist=[1,2,3]
# my_dict = {
#     "boddy":"http://ssss",
#     "boddp":"http://ssss"
# }
# for value in chain(mylist,my_dict):
#     print(value)
#
# def my_chain(*args,**kwargs):
#     for my_iterable in args:
#         # for value in my_iterable:
#         #     yield value
#         # 将值一个个迭代出来
#         yield from my_iterable
#
#
# for value in chain(mylist, my_dict):
#     print(value)
#
# def g1(iterable):
#     yield iterable
#
# def g2(iterable):
#     yield from iterable
#
# # yield是传进什么出来什么
# for value in g1(range(10)):
#     print(value)
#
# #yield from直接迭代
# # 相当于 for value in range(10):
# #            yield value
# for value in g2(range(10)):
#     print(value)

finual_result={}

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


def middle(key):
    while True:
        finual_result[key] = yield from gen(key)
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
# main是调用方，g1是委托生成器，gen是子生成器
# yield form会在调用方与子生成器之间建立一个双向通道，委托生成器是调用方和子生成器的通道。
# 为什么不直接去掉中间函数？