#! /usr/bin/python3
# -*-coding:utf-8-*-

try:
    raise KeyboardInterrupt #引发异常
finally: #不管引发异常没有，都会触发
    print('googlebye,world!') 
