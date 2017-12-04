#!/usr/bin/env python
# coding=utf-8
import sys
try :
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err)) #OSError错误
except ValueError:
    print("Couldn't convert data to an integer.") #ValueError错误
except :
    print("Unexcepted error:",sys.exc_info()[0]) #其他异常
    raise #引发异常

#用else,避免意外捕获由try语句保护的代码引起的异常
for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except OSError:#出现异常
        print('cannot open',arg) #打印异常信息
    else:
        print(arg,'has',len(f.readlines()),'lines') #否则正常运行程序
        f.close() #关闭文件

