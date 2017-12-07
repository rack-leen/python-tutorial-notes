#!/usr/bin/env python
# -*-coding=utf-8-*-
from datetime import date
now = date.today()
print(now)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.") #输出日期格式

birthday = date(1964,7,31)
age = now - birthday
print(age.days) #输出年龄，以秒输出
