#!/usr/bin/env python
# coding=utf-8
'''
fibonacci函数
'''
def fib(n):
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a,b=b,a+b

#用result返回
def fib2(n):
    result = []
    a,b=0,1
    while b < n:
        result.append(b)
        a,b=b,a+b
    return result
        
