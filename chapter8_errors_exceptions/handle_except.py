#!/usr/bin/env python
# coding=utf-8
'''
通过异常捕捉来捕捉错误
'''
#输入数字，则正确运行程序，若输入其他字符，则显示异常
while True:
    try:  #接需要运行的语句
       x = int(input("Please enter a number :")) 
       break
    except ValueError: #接收ValueError错误
        print("Oops! that was no Valid number . try again...")
