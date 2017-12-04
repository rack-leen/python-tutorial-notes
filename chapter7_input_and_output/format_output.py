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
#repr.rjust()方法表示向右对齐

#str.zfill()表示向左填充0，如下
a = '12'.zfill(5) #只有两位，不足5位，需要在前面填充0
print(a)
b = '-3.14'.zfill(7) #所有字符有5位，不足7位，需要在前面填充0
print(b)
c = '3.14159265359'.zfill(5)#由于字符串位数比给定的大，不需要填充
print(c)
d = '3.1416'.zfill(5)
print(d)
#当字符串中的字符数少于.zfill中的数字，则在前面填充0；当等于或大于时，正常输出字符串。

#.format()函数用法,format输出格式其实就是str.format()形式
print('we are the {},who say "{}"!'.format('knight','Ni'))
print('{0} and {1}.'.format('spam','eggs'))#{}中数字表示所在位置
print('{1} and {0}.'.format('spam','eggs'))#{0}表示.format中的第二个参数在输出参数中的第一个位置

#关键字参数用在format中
print('this {food} is {adjective}.'.format(food='spam',adjective='absolutely horrible'))#输出关键字参数对应的键值

#位置与关键字参数组合
print('the story is {0},{1} and {other}.'.format('Bill','Manfred',other='Georg'))

#!a(apply acsii),!r(apply repr),!s(apply str).就是将输入的转换为对应的格式
con
