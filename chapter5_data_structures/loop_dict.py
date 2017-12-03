#!/usr/bin/env python
# coding=utf-8
'''
用字典循环
'''
#looping through dictionaries 
print("looping through dictionaries:\n")
knights = {'gallahad':'the pure','robin':'the brave'}
for k,v in knights.items(): #items()用作显示字典键值
    print(k,v)

#looping through sequence
print("looping through sequence:\n")
for i,n in enumerate(['tic','tac','toe']): #enumerate()函数在字典上是枚举、列举的意思
    print(i,n)

#loop over more sequence
print("loop over more sequence:\n")
questions = ['name','quest','favorite color']
answers = ['lancelot','the holy grail','blue']
for q,a in zip(questions,answers): #zip函数接受任意多个序列做为参数，返回一个元组列表
    print('what is your{0}? it is {1}.'.format(q,a))#format格式化函数用{},:代替传统%

#loop over a sequence in reverse
print("to loop over a sequence in reverse:\n")
for i in reversed(range(1,10,2)):#颠倒顺序
    print(i)

#loop over a sequence in sorted order
print("loop over a sequence in sorted order\n")
basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):#按照集合排序(用字母顺序排序),set输出不能重复
    print(f)

#loop create a list
print("loop create a list :\n")
import math  #导入数学公式
raw_data = [56.2,float('NaN'),51.7,55.3,52.5,float('NaN'),47.8]
filtered_data = [] #创建一个空列表
for value in raw_data:
    if not math.isnan(value): #nan is not a number，这一句表示输出是number的
        filtered_data.append(value)
print(filtered_data)
