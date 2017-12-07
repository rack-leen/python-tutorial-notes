#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
生成器，用yield返回
'''

def reverse(data):
    for index in range(len(data)-1,-1,-1): #从后面开始循环到开始
        yield data[index]   #由于是列表，从0开始，需要-1

for char in reverse('golf'):
    print(char)
