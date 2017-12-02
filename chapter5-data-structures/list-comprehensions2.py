#!/usr/bin/env python
# coding=utf-8
vec = [-4,-2,0,2,4]
#创建新的列表，值加倍递增
a = [x*2 for x in vec]
print(a)

#过滤列表中的负数
b = [x for x in vec if x >= 0]
print(b)

#对所有元素应用abs()函数
c = [abs(x) for x in vec]
print(c)

#在每个元素中调用方法
freshfruit = ['banana','loganberry','passion fruit']
d = [weapon.strip() for weapon in freshfruit]
print(d)
#创建一个有两个参数的二元组
e = [(x , x**2) for x in range(6)]
print(e)
#用两个for循环将双重列表转转为列表
vec = [[1,2,3],[4,5,6],[7,8,9]]
f = [num for elem in vec for num in elem] #用elem将vec列表中的各个子集提取出来，用num将各个子集中的元素提取出来
print(f)

#包含合成生成式和嵌套函数的列表生成式
from math import pi #求圆周率
g = [str(round(pi,i)) for i in range(1,6)]
print(g)
