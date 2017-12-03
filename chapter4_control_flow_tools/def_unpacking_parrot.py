#!/usr/bin/env python
# coding=utf-8
'''
参数解压
'''

def parrot(voltage,state='a stiff',action='voom'):
    print("-- this parrot wouldn't",action,end=' ')
    print("if you put ",voltage,"volts though it.",end=' ')
    print("E's ",state,"!")
d = {"voltage":"four million","state":"bleedin' demised","action":"VOOM"}
print(parrot(**d)) #传递命名关键字参数，字典

