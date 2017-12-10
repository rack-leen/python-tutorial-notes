#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
这个例子显示了怎样在没有用zipfile模块的情况下在一个zip文件中通过循环头部信息
'''

with open('myfile.zip','rb') as f : #用open()用只读二进制格式打开,并将open命名为f
    data = f.read()  #读取数据，并赋值给data

start = 0  #初始时从０开始
for i in range(3): #显示前三个文件头信息
    start += 14  #由于H表示４字节的无符号数字,I表示２字节的无符号数字，IIIHH则有１４字节,需要每次增加１４字节
    fields = struct.unpack('<IIIHH',data[start:start+16]) #解压后的数据域增加2字节
    crc32,comp_size,uncomp_size,filename,extra_size = fields　#数据域包含的信息

    start += 16 　#解压后需要每次增加１６字节
    filename = data[start:start+filename]　#现在的数据域长度为filename
    start += filename　# 每次增加filename长度
    extra = data[start:start+extra_size] 
    print(filename,hex(crc32),comp_size,uncomp_size)

    start += extra_size + comp_size #跳过下一个头部
