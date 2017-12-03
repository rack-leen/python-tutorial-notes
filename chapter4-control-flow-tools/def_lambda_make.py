#!/usr/bin/env python
# coding=utf-8
'''
匿名函数
'''
def make(n):
    return lambda x: x+n #匿名函数设置一个简单的参数，在式中进行简单计算
#实例
f=make(42) #这里的43为n值

print(f(39)) #这里的39是x值
#lambda 用作函数
#>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
#>>> pairs.sort(key=lambda pair: pair[1])
#>>> pairs
#[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
