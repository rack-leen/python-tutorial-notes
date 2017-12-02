#!/usr/bin/env python
# coding=utf-8
def f(a , L = []): 
    L.append(a) #将变量a增加入L
    return L

#实例1
print(f(1))
print(f(2))
print(f(3))
print(f(4,[1,2,3,4]))
print(f(4,[1,2,3,4]))
print(f(1))
print(f(2))
print(f(3))
