#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
定义一个__iter__()方法，用__next__()方法返回一个对象
'''

class Reverse:
    def __init__(self,data):
        self.data = data 
        self.index = len(data) #返回data长度
    def __iter_(self):
        return self        #
    def __next__(self):
        if self.index == 0: #数据长度为0则停止迭代
            raise StopIteration #将引发异常
        self.index = self.index - 1 #数据长度-1
        return self.data[self.index] #返回第i个数据

rev = Reverse("spam")
for char in rev:
    print(char)

