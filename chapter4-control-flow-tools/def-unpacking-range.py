#!/usr/bin/env python
# coding=utf-8
'''
元组
'''
a = list(range(3,6))
print(a) #用list函数将range(3,6)中的参数解压

args = [3,7]
b = list(range(*args))
print(b) #用list函数将range中的可变参数解压
