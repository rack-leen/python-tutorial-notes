# data structures //数据结构
## more on lists
+ using lists on stacks //列表用于栈
+ using lists on queues //列表用于队列
+ lists comprehensions //理解列表
## the del statement //删除语句
## tuples and sequeues //元组与顺序表
## sets
## dictionaries //字典
## looping techniques //循环技术
## more on conditions //其他状况 







## more on lists  //列表
+ functions on lists 
list.append(x) //向列表末尾添加元素,a【len(a):】=【x】
list.extend(itrable) //使用一个序列扩展另一个序列，序列中的元素将添加到列表尾部a【len(a):】=itrable
list.insert(i,x) //将x插入第i个位置
list.remove(x) //删除x
list.pop(【i】) //将第i个位置的数据退栈
list.clear() //del a【:】
list.index(x【,start盘【,end】】) //查找索引
list.count(x) //返回x在列表中所在位置
list.sort(key=none,reverse=false)//参数是用来自定义排序
list.reverse() //将列表中元素颠倒
list.copy() //复制列表
+ example

```
#!/usr/bin/env python
# coding=utf-8
fruits = ['orange','apple','pear','banana','kiwi','apple', 'banana']
#fruits.count('apple')
#fruits.count('tangerine')
#fruits.index('banana')
#fruits.index('banana',4) #从第4个位置开始查找banana
#fruits.pop() #显示退栈数据，退栈是从列表尾部开始

#实例
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana',4))
fruits.reverse() #颠倒顺序
print(fruits)
fruits.append('grape') #在列表末尾添加元素
print(fruits)
fruits.sort() #排序
print(fruits)
print(fruits.pop())
```
输出
```
2
0
3
6
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
pear
```

### using lists on stacks //用于栈
```
#!/usr/bin/env python
# coding=utf-8
'''
栈在列表中的应用
'''
stack = [3,4,5]
#在列表末尾插入元素
stack.append(6)
print(stack)
stack.append(7)
print(stack)
#显示弹出栈的元素
stack.pop()
stack.pop()
```
输出
```
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
```

## using lists as queues //列表用于队列
### queue
```
#!/usr/bin/env python
# coding=utf-8

from collections import deque   #被设计来从末尾更快速的append and pop元素
queue = deque(["Eric","Join","Michae"])
#从末尾增加元素
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)
#从队列左边退出队列
queue.popleft() 
print(queue)
queue.popleft()
print(queue)
```
输出
```
deque(['Eric', 'Join', 'Michae', 'Terry'])
deque(['Eric', 'Join', 'Michae', 'Terry', 'Graham'])
deque(['Join', 'Michae', 'Terry', 'Graham'])
deque(['Michae', 'Terry', 'Graham'])
```

## list comprehensions //列表推导式(列表生成式)

### list-comprehensions
```
#!/usr/bin/env python
# coding=utf-8
'''
列表生成式
'''
#example1
squares = [] #构建一个空队列
for x in range(10):
    squares.append(x**2)#将构建的列表中的元素用x解出再**运算
#实例
print(squares)

#example2
squares = list(map(lambda x:x*2,range(10))) #实际上结果和上面的一样
print(squares)

#example3
squares = [x**2 for x in range(10)]#第三种表达形式
print(squares)
```
输出
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### list-comprehensions1
```
#!/usr/bin/env python
# coding=utf-8
#example1
a = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y] 
print(a) #生成以元组为子集的列表

#example2

combs = [] #构建空列表

for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
           combs.append((x,y))

print(combs)
```
输出
```
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
### list-comprehensions2
```
#!/usr/bin/env python
# coding=utf-8
vec = [-4,-2,0,2,4]
#创建新的列表，值加倍递增
a = [x*2 for x in vec]
print(a)

#过滤列表中的负数
b = [x for x in vec if x >= 0]
print(b)

#对所有元素应用abs()函数
c = [abs(x) for x in vec]
print(c)

#在每个元素中调用方法
freshfruit = ['banana','loganberry','passion fruit']
d = [weapon.strip() for weapon in freshfruit]
print(d)
#创建一个有两个参数的二元组
e = [(x , x**2) for x in range(6)]
print(e)
#用两个for循环将双重列表转转为列表
vec = [[1,2,3],[4,5,6],[7,8,9]]
f = [num for elem in vec for num in elem] #用elem将vec列表中的各个子集提取出来，用num将各个子集中的元素提取出来
print(f)

#包含合成生成式和嵌套函数的列表生成式
from math import pi #求圆周率
g = [str(round(pi,i)) for i in range(1,6)] 
print(g) #得出来的pi为字符串
```
输出
```
[-8, -4, 0, 4, 8]
[0, 2, 4]
[4, 2, 0, 2, 4]
['banana', 'loganberry', 'passion fruit']
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### nexted list comprehensions //嵌套列表生成式
```
#!/usr/bin/env python
# coding=utf-8
'''
嵌套列表生成式
'''
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],] #每个子集后面要加逗号
a = [[row[i] for row in matrix] for i in range(4)]
print(a)

#等价于
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

#等价于
transposed = [] #初始化
for i in range(4):
    transposed_row=[]  
    for row in matrix: #行初始化
        transposed_row.append(row[i])#往列表第row个元素的第i个位置增加元素
    transposed.append(transposed_row) #往列表的第i个位置增加元素
print(transposed)

#相似
e = list(zip(*matrix))
print(e)
```
输出
```
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```
## the del statement //del语句
```
#!/usr/bin/env python
# coding=utf-8
'''
删除语句
'''
a = [-1,0,1,2,3,4,77,99,3444]
print(a)

del a[0]
print(a)

#切片删除
del a[2:4]
print(a)

#全部删除
del a[:]
print(a)

#删除全部变量
del a #输出错误，因为变量已经被删除
```
输出
```
[-1, 0, 1, 2, 3, 4, 77, 99, 3444]
[0, 1, 2, 3, 4, 77, 99, 3444]
[0, 1, 4, 77, 99, 3444]
[]
```

## tuples and sequences //元素与序列
```
#!/usr/bin/env python
# coding=utf-8
'''
元组与序列
'''
print("example")
t = 12345,54321,'hello' #元组可以只用逗号分开，不需要括号
print(t[0])
print(t)

#元组嵌套
u = t,(1,2,3,4,5)
print(u)#嵌套后的元组成为有两个子集元组的大元组

#元组值不可变,t[0]=9999(元组重置元素是不可行的，会报错)
#元组可以包含可变的参数,如列表
v = ([1,2,3],[3,2,1])
print(v)


print("example2")
empty = ()
sing = 'woow'
singleton = 'hello', #后面多加一个逗号表示元组
print(len(empty)) #显示empty长度
print(len(sing)) #显示sing长度
print(len(singleton))#显示singleton长度
print(empty)
print(sing)
print(singleton)

#在解释器中，如果，t = 1,2,3 ，可以颠倒，1,2,3=t
```
输出
```
example
12345
(12345, 54321, 'hello')
((12345, 54321, 'hello'), (1, 2, 3, 4, 5))
([1, 2, 3], [3, 2, 1])
example2
0
4
1
()
woow
('hello',)
```

## sets  //集合 
+ 用花括号或者set()函数创建sets（创建空的sets需要用set()函数）
```
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
```
输出
```
{'apple', 'pear', 'banana', 'orange'}
True
False
{'d', 'r', 'c', 'a', 'b'}
{'d', 'r', 'b'}
{'d', 'c', 'z', 'r', 'b', 'l', 'm', 'a'}
{'d', 'z', 'r', 'b', 'l', 'm'}
{'c', 'a'}
{'d', 'r'}
```

## dictionaries //字典
```
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
```
输出
```
{'jack': 4098, 'sape': 4139}
{'jack': 4098, 'guido': 4127, 'sape': 4139}
{'jack': 4098, 'guido': 4127}
{'jack': 4098, 'guido': 4127, 'irv': 4098}
['jack', 'guido', 'irv']
['guido', 'irv', 'jack']
True
False
True
{'jack': 4098, 'guido': 4127, 'sape': 4139}
{2: 4, 4: 16, 6: 36}
{2: 4, 4: 16, 6: 36}
{'jack': 4089, 'guido': 4127, 'sape': 4139}
```

## looping techniques //循环技术
+ looping through dictionaries //通过字典循环
+ looping through sequence     //通过序列循环

