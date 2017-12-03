#!/usr/bin/env python
# coding=utf-8
x = input("please enter an data: ") #说明语句和输入变量,这里的x是str类型
print(x) #输出
b = int(input("please enter an integer: "))#只能输入整型数据，输入其他报错,b是int类型
print(b)

#if语句
if b < 0 :
    b = 0
    print('negative changed to zero') #输出字符串
elif b == 0:
    print('zero')
elif b == 1:
    print('single')
else:
    print('more')
