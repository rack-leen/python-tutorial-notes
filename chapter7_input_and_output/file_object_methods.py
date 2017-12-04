#!/usr/bin/env python
# coding=utf-8

f = open('workfile') #打开文件
print(f.read()) #读取文件
print(f.read()) #由于已经读取过了，再读取为空

f = open('workfile1') #打开文件
print(f.readline()) #只读取一行，不能与f.read一起用
print(f.readline()) #再读取只能读取下一行,读取了的不能再读取

#用循环将文件中的文本取出
for line in f:
    print(line,end=' ')
f = open('workfile1', 'w') #打开文件,并支持写入
print(f.write('this is a text\n')) #向文件写入文本，返回写入文本的长度

#将其他类型转换为字符串
f = open('workfile1', 'w') #打开文件,并支持写入
value = ('answer',42) #元组
s = str(value) #将元组转换为字符串
f.write(s) #将s写入f文件中，需要有w权限
