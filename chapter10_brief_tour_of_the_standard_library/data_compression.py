#!/usr/bin/env python
# -*-coding=utf-8-*-
import zlib
s = b'witch which has which witches wrist watch' #字节文件
len(s) #查看字节长度
t = zlib.compress(s) #将s压缩
len(t) #再次查看长度
zlib.decompress(t) #将压缩文件解压
zlib.crc32(s) #校验文件


