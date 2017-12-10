#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
repr输出格式
'''

import reprlib 

a = reprlib.repr(set('aDsupercalifragilisticexpialidocious'))
print(a) #以ascii表顺序输出不重复字母（字符串中出现的）

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
print(pprint.pprint(t,width=30)) #t以每行３０个字符的方式输出

import textwrap #格式化文本段落，以适应屏幕宽度
doc = """he wrap() method is just like fill() except that it returns,a list of strings instead of one big string with newlines to separate,the wrapped lines.""" 
print(textwrap.fill(doc,width=40)) #只能用文本方式

#多语言模块
import locale
locale.setlocale(locale.LC_ALL,'English_United States.1252') #设置语言
conv = locale.localeconv() #获取约定的映射
x = 1234567.8
locale.format("%d",x,grouping=True) #格式化x为整型
locale.format_string("%s.%f",(conv['currency_symbol'],conv['frac_digits'],x),grouping=True) #格式化为字符串(使用组分隔符格式化数字) currency_symbol意思为使用$开头的和发标识为站位符

