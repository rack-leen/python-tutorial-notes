#!/usr/bin/env python
# coding=utf-8

with open('workfile') as f:#为open()取别名
    read_data = f.read() #workfile中读取的数据放入read_data
print(read_data)
print(f.closed) #标记文件是否已经关闭，true表示正确关闭
#print(f.read()) #运行错误，表示文件确实被关闭
#f.close()
#print(f.read()) #文件


