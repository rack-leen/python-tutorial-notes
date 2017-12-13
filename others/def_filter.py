#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
filter函数与函数map类似，需要传入两个参数，传入函数依次作用在序列上
'''
#删掉偶数，只保留奇数
def is_odd(n):
    return n%2==1
a = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10]))
print(a)

#删除字符串中的空格
def not_empty(s):
    return s and s.strip() #删除空格用strip()
b = list(filter(not_empty,['A','B','C',None,'D']))
print(b)

#用filter求素数
def _odd_iter(): #私有函数
    n=1
    while True:
       n=n+2
       yield n
def _not_divisible(n): #筛选函数
    return lambda x: x%n>0
def primes():
    yield 2  #首先生成第一个素数２
    it=_odd_iter() #初始化序列
    while True:
        n = next(it)#返回序列第一个数
        yield n
        it = filter(_not_divisible(n),it)#构造新序列
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

