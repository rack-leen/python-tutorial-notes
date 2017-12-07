#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
迭代器，用for进行迭代
'''

for element in [1,2,3]: #list
    print(element)
for element in (1,2,3): #tuple
    print(element)
for key in {'one':1,'two':2}: #dictionary
    print(key)
for char in "123": #string
    print(char)
for line in open("myfile.txt"):
    print(line)

