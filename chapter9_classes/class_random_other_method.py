#!/usr/bin/env python
# -*-coding=utf-8-*-

class Bag:
    def __init__(self):
        self.data = []

    def add(self,x):
        self.data.append(x)

    def addtwice(self,x):
        self.add(x)
        self.add(x)

#实例
d = Bag()
d.add(7) #添加元素到列表
d.add(8)
print(d.data) #输出列表
