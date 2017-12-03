#!/usr/bin/env python
# coding=utf-8

s = 'Hello world.'
print(str(s)) #字符串输出格式,用于将值转换为适用于人阅读的形式
print(repr(s)) #返回一个字符串，将值转换为适用于解释器的形式
print(str(1/7)) #将数值转换为字符串输出

x = 10*3.25
y = 200*200
s = 'the value of x is '+ repr(x) + ' ,and y is ' + repr(y) + '...'
print(s)

hello = 'Hello , world.\n'
print(hello) #print会将\n判断为换行符
hellos = repr(hello) #repr会将\n判断为一个字符
print(hellos)
print(repr((x,y,('spam','eggs')))) #repr的参可以是任何python对象

#输出平方和立方的两种方法
for i in  range(1,11):
    print(repr(i).rjust(2),repr(i*i).rjust(3),end=' ')#第一大列和第二大列所占空格分别为两个和三个（每一大列容纳酔大的空格数）
    print(repr(i*i*i).rjust(4)) #第三大列所占空格为四个

for x in range(1,11):
    print('{0:2d},{1:3d},{2:4d}'.format(x,x*x,x*x*x))#每列的空格由print()增加的
#repr.rjust()方法表
