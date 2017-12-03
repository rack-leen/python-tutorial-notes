#!/usr/bin/env python
# coding=utf-8
words = ['cat','windows','linux','pig']
for x in words[:]:
    if len(x) > 5:
        words.insert(0,x) #将符合条件的数据增加到words[0]中
        print(words)
