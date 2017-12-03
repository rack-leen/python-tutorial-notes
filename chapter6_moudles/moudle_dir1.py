#!/usr/bin/env python
# coding=utf-8
a = [1,2,3,4,5] #a做为一个全局变量加入了dir搜索中
import moudle_fibonacci
fib = moudle_fibonacci.fib
print(dir())
#列出的所有类型名有变量，模块，函数

#dir列出内置函数和变量的名称
import builtins
print(dir(builtins))
