#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
将类当做struct数据类型
'''
class Emptyclass:
    pass

join = Emptyclass()

join.name = 'john Doe'
join.dept = 'computer lab'
join.salary = '1000'

#实例

print(join.name,"\n",join.dept,"\n",join.salary)

