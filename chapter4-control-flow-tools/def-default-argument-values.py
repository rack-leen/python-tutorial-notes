#!/usr/bin/env python
# coding=utf-8
'''
默认参数值
'''
def ask_ok(prompt , retries=4 , reminder='please try again!'): #retries,reminder为默认参数
    while True :
        ok = input(prompt)
        if ok in ('y','ye','yes'):#输入其中的一个
            return True 
        if ok in ('n','no','nop','nope'):#如果第一个为真，这句将不执行
            return False
        retries = retries-1 #每执行一次，retries-1
        if retries < 0 : #当执行完次数，则报错
            raise ValueError('invalid user response')
        print(reminder) #打印结果，retries<0后重新运行程序
#这个函数参数两个参数为默认参数，默认参数如果不赋值，则默认输出
#如果赋值，则依照赋值的数据打印

    
#实例1
#print(ask_ok('Do you really want to quit?'))
#实例2
#print(ask_ok('OK to overwrite the file ?',2))#2为retries赋值
#实例3
print(ask_ok('OK to overwrite the file ?',2,'Come on , inly yes or no!'))
