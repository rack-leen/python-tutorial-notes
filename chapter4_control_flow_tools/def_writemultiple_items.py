#!/usr/bin/env python3
# coding=utf-8
'''
任意形式参数列表
'''
def write_multiple_items(file,separator, *args):
    file.write(separator.join(args))

print()
