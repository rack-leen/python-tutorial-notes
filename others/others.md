# 官方教程未使用的python内容

## map()和reduce()函数
+ map()函数
第一个参数是定义的运算规则，后面的序列是需要计算的元素
```
#!/usr/bin/env python
# -*-coding=utf-8-*-

def f(x):
    return x*x

r = map(f , [1,2,3,4,5,6,7,8]) #第一个参数是定义的运算规则，后面的序列是需要计算的元素
print(list(r))
```
输出
```
[1, 4, 9, 16, 25, 36, 49, 64]
```

+ reduce()函数
reduce把一个函数作用在一个序列上，这个函数必须接收两个参数，把结果继续和序列的下一个元素做累积计算
```
#!/usr/bin/env python
# -*-coding=utf-8-*-

'''
reduce()函数作用在一个序列上，必需接收两个参数，把结果继续和序列的下一个元素进行计算。
reduce(f,(x1,x2,x3,x4)) 效果相当于f(f(f(x1,x2),x3),x4)
'''

from functools import reduce

#求和运算
def add(x,y):
    return x+y
a = reduce(add,[1,3,5,7,9])
print('sum is : ',a)

#复杂的运算
def fn(x,y):
    return x*10+y
b = reduce(fn,[1,3,5,7,9])
print('sum2 is : ',b)

#字符串
def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
c = reduce(fn,map(char2num,'13579')) #map将字典中的关键字与输入的匹配，输出键值，并将键值用自定的函数规则运算
print('char is : ',c)

#用lambda匿名函数进行简化
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2int(s):
    return reduce(lambda x,y: x*10+y,map(char2num,s))
print('str is : ',str2int('123456'))
```
输出
```
sum is :  25
sum2 is :  13579
char is :  13579
str is :  123456
```

## filter
+ filter函数用于过滤序列
与map类似,filter也接收一个函数和一个序列，但是把传入的函数依次作用于每个元素,根据返回true/false判断保留或者丢弃该元素

```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
filter函数与函数map类似，需要传入两个参数，传入函数依次作用在序列上
'''
#删掉偶数，只保留奇数
def is_odd(n):
    return n%2==1
a = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10]))
print(a)

#删除字符串中的空格
def not_empty(s):
    return s and s.strip() #删除空格用strip()
b = list(filter(not_empty,['A','B','C',None,'D']))
print(b)

#用filter求素数
def _odd_iter(): #私有函数
    n=1
    while True:
       n=n+2
       yield n
def _not_divisible(n): #筛选函数
    return lambda x: x%n>0
def primes():
    yield 2  #首先生成第一个素数２
    it=_odd_iter() #初始化序列
    while True:
        n = next(it)　#返回序列第一个数
        yield n
        it = filter(_not_divisible(n),it)#构造新序列
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

+ sorted 排序算法

