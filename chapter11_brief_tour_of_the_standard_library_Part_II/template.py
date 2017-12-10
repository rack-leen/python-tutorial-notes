#!/usr/bin/env python
# -*-coding=utf-8-*-
from string import Template
#Template函数用来创建模板，'$'表示输出后面的字符,$$表示输出$
#t.substitute方法使用的字典模式,Template关键字，t.substitute提供键值
t = Template('${village}folk send $$10 to ${cause}')
print(t.substitute(village='NOttingham',cause='the dicth fund.'))

#如果输入的键值与模板中的关键字数量不匹配，会出现keyerror错误
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow') #用dict函数输入字典

print(t.safe_substitute(d)) #使用safe_substitute忽略错误


import time,os.path
photofiles = ['img_1974,jpg','img_1976.jpg','img_1977.jpg']
class BatchReneme(Template):
    delimiter = '%' #用%代替$分开
fmt = input('Enter reneme style (%d-date %n-seqnum %f-format):') #输入模板
t = BatchReneme(fmt) #将输入的模板复制到t
date = time.strftime('%d%b%y')#时间格式
for i , filename in enumerate(photofiles): #枚举photofiles
    base , ext = os.path.splitext(filename)# 切割photofiles中的文件名
    newname = t.substitute(d=date,n=i,f=ext) #d的键值就是date，n的键值为ｉ,f的键值n为ext
    print('{0} --> {1}'.format(filename,newname))#输出旧名称和新名称



