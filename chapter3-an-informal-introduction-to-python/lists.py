#!/usr/bin/env python
# coding=utf-8
'''
列表
'''
squares = [1,4,8,16,25]
print(squares)  #输出列表数据
print(squares[0])
print(squares[-1])
print(squares[-3:]) #从倒数第三个数据到最后一个数据
print(squares[:])#相当于直接输出列表全部数据
print(squares + [36,64,81,100])#直接在列表后面增加数据

#替代列表中的数据
cubes = [1,8,65,125.78]
print(cubes)
cubes[3] = 64
print(cubes)

#用append()方法增加数据
cubes.append(216)
print(cubes)

cubes.append(7**2)#增加指数
print(cubes)

#列表中的字符串
letters = ['a','b','c','d','e','f','g']
print(letters)
#替代列表中的一串字符
letters[2:5] = ['C','D','E'] #从2到5的数据替换成另外三个数据
print(letters)
letters[2:5] = [] #将2到5的数据替换为空
print(letters)
letters[:] = [] #将整个列表数据替换为空

letters = ['a','b','c','d']
print(len(letters)) #打印字符串长度
#将列表字符与数字连接
a = ['a','b','c','d']
b = [1,2,3]
c = [a,b]   #将a和b做为c列表的子集
print(c) #输出整个列表
print(c[0])#输出列表的第一个子集a
print(c[0][1]) #输出列表的第一个子集的第二个数据



