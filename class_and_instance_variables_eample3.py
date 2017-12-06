#! /usr/bin/python3
#coding:utf-8

class Dog:
    def __init__(self,name):
        self.name = name
        self.tricks = [] #给实例的属性绑定一个空列表

    def add_trick(self,trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddly')

d.add_trick('roll ever')
e.add_trick('play dead')

print(d.tricks)
print(e.tricks) #有对象属性
#print(Dog.tricks)#Dog没有类属性tricks
