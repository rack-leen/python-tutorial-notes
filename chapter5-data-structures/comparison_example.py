#!/usr/bin/env python
# coding=utf-8
'''
将比较的结果分配给变量
'''
string1,string2,string3='','Trondheim','Hammer Dance' #三个变量分别赋值
non_null = string1 or string2 or string3 #比较三个变量中的数据，并赋值给另一个变量
print(non_null) 
