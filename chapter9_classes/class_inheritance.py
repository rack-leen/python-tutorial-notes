#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
类继承
'''
#父类动物
class Animal(object):
    def run(self):
        print('Animal is running......')


#子类
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()
cat = Cat()
cat.run()
