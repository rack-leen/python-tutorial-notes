#!/usr/bin/env python
# coding=utf-8
'''
删除语句
'''
a = [-1,0,1,2,3,4,77,99,3444]
print(a)

del a[0]
print(a)

#切片删除
del a[2:4]
print(a)

#全部删除
del a[:]
print(a)

#删除全部变量
del a #输出错误，因为变量已经被删除

