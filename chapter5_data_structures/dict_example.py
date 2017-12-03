#!/usr/bin/env python
# coding=utf-8
'''
字典
'''
#字典与集合一样需要用花括号
tel = {'jack':4098,'sape':4139}
print(tel)
tel['guido'] = 4127 #通过关键字添加元素
print(tel)

del tel['sape'] #通过关键字删除元素
print(tel)

tel['irv'] = 4098 #添加键值与字典中键值相同的元素
print(tel)

a = list(tel.keys())#列出字典中的关键字
print(a)

b = sorted(tel.keys())#将字典按关键字排序
print(b)

#两个相同键值的元素，只能识别一个
c = 'jack' in tel
d = 'irc' in tel  
e = 'guido' in tel
print(c)
print(d)
print(e)

#用dict()函数构建字典
f = dict([('sape',4139),('guido',4127),('jack',4098)])
print(f)

#用于字典的生成式
g = {x: x**2 for x in (2,4,6)} #关键字为（2,4,6），键值为x**2 
print(g)

h = {x: x**2 for x in [2,4,6]} 
print(h)

#用关键字参数
i = dict(sape=4139,guido=4127,jack=4089)
print(i)
