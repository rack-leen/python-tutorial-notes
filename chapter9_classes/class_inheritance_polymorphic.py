#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
继承的多态
'''

class Animal(object):
    def run(self):
        print('Animal is running......')

class Dog(Animal):
    def run(self):
        print('Dog is runing......')
    def eat(self):
        print('Dog eating meat......')

class Cat(Animal):
    def run(self):
        print('Cat running......')

#现在输出的是子类定义的函数输出，也就是父类同名函数被覆盖了
dog = Dog()
cat = Cat()

dog.run()
dog.eat()
cat.run()
