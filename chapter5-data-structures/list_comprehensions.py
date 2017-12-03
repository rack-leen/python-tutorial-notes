#!/usr/bin/env python
# coding=utf-8
'''
列表生成式
'''
#example1
squares = [] #构建一个空队列
for x in range(10):
    squares.append(x**2)#将构建的列表中的元素用x解出再**运算
#实例
print(squares)

#example2
squares = list(map(lambda x:x*2,range(10))) #实际上结果和上面的一样
print(squares)

#example3
squares = [x**2 for x in range(10)]#第三种表达形式
print(squares)
