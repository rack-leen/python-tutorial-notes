#!/usr/bin/env python
# -*-coding=utf-8-*-

def f(x):
    return x*x

r = map(f , [1,2,3,4,5,6,7,8]) #第一个参数是定义的运算规则，后面的序列是需要计算的元素
print(list(r))
