#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
私有变量
'''

class Mapping:
    def __init__(self,iterable):
        self.items_list = []  #相当于在函数中定义的变量
        self.__update(iterable) #调用方法

    def update(self,iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update #将update方法的副本复制给私有变量

class MappingSubclass(Mapping): #子类
    def update(self,keys,values):
        for item in zip(keys,values): #将keys,values组装返回一个元组
            self.items_list.append(item)

