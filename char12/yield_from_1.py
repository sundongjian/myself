# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 15:31

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

def main():
    my_gen=gen('mon')
    my_gen.send(None)
    my_gen.send(1200)
    my_gen.send(1200)
    my_gen.send(1200)
    #  再次发送send(None)抛出异常，应该再处理(教程中说return会抛出异常，实际不return也会,只要send的次数大于（包扩send（None)
    #  就会抛出异常
    # yield from 帮我们完成了这个逻辑，不用做大量的try
    # my_gen.send(None)

    try:
        my_gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)

main()
