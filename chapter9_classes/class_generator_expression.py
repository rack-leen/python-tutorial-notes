#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
生成器生成式
'''
#求i的平方
a = sum(i*i for i in range(10))
print(a)

#两个列表乘积
xvec = [10,20,30]
yvec = [7,6,4]
b = sum(x*x for x,y in zip(xvec,yvec)) #用zip函数将两个列表组装成元组
print(b)

#
from math import pi,sin
sine_table = {x:sin(x*pi/180) for x in range(0,91)}
page = [11,22,33,44,55]
unique_words = set(word for line in page for word in line.split())
vaiedictorian = max((student.gpa,student.name) for student in graduates)
data = 'golf'
list(data[i] for i in range(len(data)-1,-1,-1))
