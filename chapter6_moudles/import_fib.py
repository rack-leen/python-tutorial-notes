#!/usr/bin/env python3
# coding=utf-8
#用这个方式导入模块，需要写模块前缀名
import moudle_fibonacci

print(moudle_fibonacci.fib(100))
print(moudle_fibonacci.fib2(1000))
#别名
fib = moudle_fibonacci.fib
fib2 = moudle_fibonacci.fib2
print(fib(100))
print(fib2(1000))
