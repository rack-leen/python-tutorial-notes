#!/usr/bin/env python
# -*-coding=utf-8-*-


#计算税率
from decimal import * #十进制浮点运算
print(round(Decimal('0.70')*Decimal('1.05'),2)) #计算后进行约数，再保留２位小数点
print(round(.70*1.05,2)) #计算后直接保留２位小数，不进行任何运算
print(Decimal('1.00')%Decimal('.10'))
print(1.00%0.10)
print(sum([Decimal('0.1')]*10)==Decimal('1.0')) #判断结果是否相等
print(sum([0.1]*10)==1.0)
getcontext().prec=36 #后面小数点数
print(Decimal(1)/Decimal(7)) 
