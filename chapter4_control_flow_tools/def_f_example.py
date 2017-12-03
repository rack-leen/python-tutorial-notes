#!/usr/bin/env python
# coding=utf-8
def f_example(L=[]):
    L.append('END')
    return L
print(f_example())
print(f_example([1,2,3]))
print(f_example())
