# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 18:37

# python 为了将语义变得更加明确，将async和await关键词用于定义原生协程
# 为了将协程和生成器分开，async下不能用yield只能用await
# await 调用的方法也是async，如果不是async开头的def，并且里面有yield，可以加上types.coroutine的装饰器

async def downlaod():
    pass