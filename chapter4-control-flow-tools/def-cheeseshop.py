#!/usr/bin/env python
# coding=utf-8
'''
命名关键字参数
'''
def cheeseshop(kind , *argument , **keywords):
    print("--Do you have any ",kind , "?")
