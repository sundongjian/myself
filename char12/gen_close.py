# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 14:33

# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 13:54

def gen_func():
    # 可以产出值  可以接收值（接收调用方产生的值)
    try:
        yield "www.baidu.com"
    # 注意GeneratorExit的基类是BaseException
    except GeneratorExit:
        # pass
        raise StopIteration
    yield 2
    yield 3
    return "bobby"

if __name__=="__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    next(gen)
    # close之后再调用next(gen)会抛出异常stopiteration
    # 尝试在第一个yield添加except忽略异常，如果注释掉下面的yield，不会抛异常，如果注释，就会在close（）处抛出异常
    # 如果不忽略而是rasie，那么即使不注释掉下面的yield，只要不再使用next调用，也不会抛出异常
    # 如果使用rasie后继续使用next，那么会在next处抛出异常StopIteration
    # 注意异常都是向上抛的，抛到调用方为止







