#!/usr/bin/env python
# coding=utf-8
'''
元组与序列
'''
print("example")
t = 12345,54321,'hello' #元组可以只用逗号分开，不需要括号
print(t[0])
print(t)

#元组嵌套
u = t,(1,2,3,4,5)
print(u)#嵌套后的元组成为有两个子集元组的大元组

#元组值不可变,t[0]=9999(元组重置元素是不可行的，会报错)
#元组可以包含可变的参数,如列表
v = ([1,2,3],[3,2,1])
print(v)


print("example2")
empty = ()
sing = 'woow'
singleton = 'hello', #后面多加一个逗号表示元组
print(len(empty)) #显示empty长度
print(len(sing)) #显示sing长度
print(len(singleton))#显示singleton长度
print(empty)
print(sing)
print(singleton)

#在解释器中，如果，t = 1,2,3 ，可以颠倒，1,2,3=t
