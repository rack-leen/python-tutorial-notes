#!/usr/bin/env python
# -*-coding=utf-8-*-

'''
reduce()函数作用在一个序列上，必需接收两个参数，把结果继续和序列的下一个元素进行计算。
reduce(f,(x1,x2,x3,x4)) 效果相当于f(f(f(x1,x2),x3),x4)
'''

from functools import reduce

#求和运算
def add(x,y):
    return x+y
a = reduce(add,[1,3,5,7,9])
print('sum is : ',a)

#复杂的运算
def fn(x,y):
    return x*10+y
b = reduce(fn,[1,3,5,7,9])
print('sum2 is : ',b)

#字符串
def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
c = reduce(fn,map(char2num,'13579')) #map将字典中的关键字与输入的匹配，输出键值，并将键值用自定的函数规则运算
print('char is : ',c)

#用lambda匿名函数进行简化
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2int(s):
    return reduce(lambda x,y: x*10+y,map(char2num,s))
print('str is : ',str2int('123456'))

