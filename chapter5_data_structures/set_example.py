#!/usr/bin/env python
# coding=utf-8
'''
sets集合
'''

basket = {'apple','orange','apple','pear','orange','banana'} #用{}创建sets
print(basket)#不重复输出元素

#判断sets中的value是否在字典中
a = 'orange' in basket
print(a)
b = 'cranfg' in basket
print(b)

#对两个单词的操作
a = set('abracadabra')
b = set('alacazam')
print(a) #不重复输出a中的字母
c = a - b #相减
print(c)
d = a | b #或
print(d)
e= a ^ b #取反
print(e)
f = a & b #取并集
print(f)

#用列表生成式
g = {x for x in 'abracadabra' if x not in 'abc'} #输出不在abc范围中的字符串中的字母
print(g)
