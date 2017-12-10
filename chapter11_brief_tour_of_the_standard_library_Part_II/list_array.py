#!/usr/bin/env python
# -*-coding=utf-8-*-
from array import array 
a = array('H',[4000,10,700,22222]) #‘'H'为类型代码，表示二进制数，后面为生成的是二进制数组
b = sum(a) #将数组中数据相加
print(b)
c = a[1:2] 
print(c)
