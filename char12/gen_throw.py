# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 14:33

# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 13:54

def gen_func():
    # 可以产出值  可以接收值（接收调用方产生的值)
    try:
        yield "www.baidu.com"
    except Exception as e:
        # pass
        pass
    yield "www.baidu.com"
    yield 2
    yield 3
    return "bobby"


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception,'download_url_error')
    print(next(gen))
    # 在yield 2 的地方抛出异常 Exception: download_url_error
    gen.throw(Exception, 'download_url_error')
    '''
    中断Generator是一个非常灵活的技巧，可以通过throw抛出一个GeneratorExit异常来终止Generator。Close()方法作用是一样的，
    其实内部它是调用了throw(GeneratorExit)的。
    throw 和close的不同是可以将异常抛到被调用方里面
    close 
    '''








