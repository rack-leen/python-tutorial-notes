#! /usr/bin/python3
#coding:utf-8

class Dog:
    tricks = [] 
    def __init__(self,name):
        self.name = name
    def add_trick(self,trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddly')
d.add_trick('roll ever')
e.add_trick('play dead')#e使用方法，增加trick到tricks

print(d.tricks)#tricks是一个类变量，被所有实例共享,所以每个实例向tricks增加内容都会被所有实例共享

print(Dog.tricks)
#在这里Dog.tricks(所有对象共享的属性)与d.tricks(对象的属性)显示相同.
