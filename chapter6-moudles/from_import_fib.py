#!/usr/bin/env python
# coding=utf-8
#用这个形式导入模块中的函数，不需要写模块前缀
from moudle_fibonacci import fib,fib2
print(fib(100)) #只需要用模块中的函数，与引用在一个文件的中函数一样
print(fib2(1000))

#导入模块中所有的函数，这种方法一般来说是不被使用的，只是可以用于交互式解释器
from moudle_fibonacci import *
print(fib(800))
print(fib2(1000))

