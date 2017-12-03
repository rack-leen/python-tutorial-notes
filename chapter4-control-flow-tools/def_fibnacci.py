#!/usr/bin/env python
# coding=utf-8
#example1
def fibnacci(n):
    a,b = 0,1
    while a<n :
        print(a,end=',')
        a,b = b , a+b
#输出需要在函数外面     
print(fibnacci(1000))

#example2
def fibnacci2(n):
    result = [] #result为输出结果
    a,b = 0 , 1 
    while a < n:
        result.append(a)#将a增加如result
        a,b = b , b+a
    return result #返回结果
print('实例输出：\n')
print(fibnacci2(100)) 
