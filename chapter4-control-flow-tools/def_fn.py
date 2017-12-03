#!/usr/bin/env python
# coding=utf-8
'''
函数注释
'''
def fn(ham:str,eggs:str='eggs')->str:
    print("annotations: ",fn.__annotations__)#函数注释所在的隐藏属性
    print("arguments: ",ham,eggs) #函数参数输出
    return ham+"and"+eggs
#实例
print(fn('spam')) 
