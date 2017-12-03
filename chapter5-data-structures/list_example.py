#!/usr/bin/env python
# coding=utf-8
fruits = ['orange','apple','pear','banana','kiwi','apple', 'banana']
#fruits.count('apple')
#fruits.count('tangerine')
#fruits.index('banana')
#fruits.index('banana',4) #从第4个位置开始查找banana
#fruits.pop() #显示退栈数据，退栈是从列表尾部开始

#实例
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana',4))
fruits.reverse() #颠倒顺序
print(fruits)
fruits.append('grape') #在列表末尾添加元素
print(fruits)
fruits.sort() #排序
print(fruits)
print(fruits.pop())
