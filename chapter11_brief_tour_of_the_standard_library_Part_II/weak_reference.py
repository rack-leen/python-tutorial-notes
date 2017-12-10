#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
弱引用
当对象不再需要，将会从弱引用表中移除
'''
import weakref , gc
class A:
    def __init__(self,value):
        self.value = value

    def __repr__(self): #用于解释器理解
        return str(self.value) #用字符串返回

a = A(10) #创建引用
d = weakref.WeakValueDictionary() #创建一个字典，对其中的值进行弱引用,对值没有更多的强引用时, 将丢弃该字典中的对应项。如果提供dict, 则将dict中的各项添加到返回的WeakValueDictionary。WeakValueDictionary的实例有两个返回弱值引用的方法：itervaluerefs()和valuerefs()。
d['primary'] = a #不创建引用
print(d['primary'])#如果引用还在，就取回对象
del a #移除引用
print(gc.collect()) #立即运行垃圾收集
print(d['primary']) #引用已经不存在，输出错误






