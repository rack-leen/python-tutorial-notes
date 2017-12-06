#!/usr/bin/env python
# coding=utf-8

class MyClass:
    """
    A simple example clss.
    """
    i = 123456

    def f(self):#指代的是对象本身，代表当前对象地址，避免非限定调用造成的全局变量
        return 'hello world'

    #MyClass.i（返回整型）和MyClass.f（返回函数）都是有效的属性引用
    #__doc__也是一个有效的属性，返回属于类的docstring：'A simple example clss.'

        
                        
    #类实例化使用函数表示法，假设类对象是一个没有参数的函数，它将返回一个新实例
    #x = MyClass() #创建一个新实例，并将这个对象赋给局部变量x
    def __init__(self):#self指代类对象
        self.data = [] #这是类的实例化,将会创建一个空对象

# method objects
x = MyClass() #从MyClass类中返回一个对象，赋给x
xf = x.f      #x对象调用f方法，并赋给xf
while True :
    print(xf()) #xf现在就是x.f方法
