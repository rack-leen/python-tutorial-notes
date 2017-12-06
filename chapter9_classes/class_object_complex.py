#!/usr/bin/env python
# coding=utf-8

class Complex:
    def __init__(self,realpant , imagpart):
        self.r = realpant   #参数传给类实例，self.r是一个类实例
        self.i = imagpart #self.i是一个类实例

x = Complex(3.0,-4.5) #这两个参数就是self.r,self.i这两个类实例 
#实际上这后面的参数是__init__方法中的参数，通过类实例传递给了Complex
print(x.r,x.i)


#对象实例化
x.counter = 1  #对象实例的初始状态
while x.counter < 10: #属性引用也可以称为方法，这是属于对象的方法
    x.counter = x.counter * 2
print(x.counter)
del x.counter #删除
