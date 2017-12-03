#!/usr/bin/env python
# coding=utf-8
'''
可变参数
'''
def varied(*numbers): #可变参数,可以传入多个参数,*numbers相当于一个元组tuple
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(varied(1,3,4,5))


