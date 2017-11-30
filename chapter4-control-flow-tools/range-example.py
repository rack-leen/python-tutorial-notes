#!/usr/bin/env python
# coding=utf-8

for i in range(10): #表示输出从0到10的整数
    print('please output i: %d\t'%i)  
print('\n')

for x in range(5,10): #输出从5到10的数
    print('please output x: %d\t'%x)  
print('\n')

for b in range(0,10,3):#输出从0到10的数（每个数之间相隔3）
    print('please output b: %d\t'%b)  

print('\n')
for c in range(-10,-100,-30):#输出从-10到-100的数（每个数之间隔-30）
    print('please output c: %d\t'%c)  

#range()函数与len()函数连用
a = ['mary','had','a','little','lamb']
print('\n')
for e in range(len(a)): #用a的长度做为i的范围
    print(e,a[e])#输出第i个a[i]

#直接输出range
print(range(0,10))

#用列表输出
d = list(range(5))
print(d)

