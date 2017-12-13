# control flow tools  控制流工具
## if statements
## for statements
## range function
## break , contiune ,else
## pass statements
## function argument 
### position argument  位置参数，普通的参数
### default argument  默认参数
### keyword argument  关键字参数，字典形式
### arbitrary argument lists 

## if statements  if语句
```
#!/usr/bin/env python
# coding=utf-8
x = input("please enter an data: ") #说明语句和输入变量,这里的x是str类型
print(x) #输出
b = int(input("please enter an integer: "))#只能输入整型数据，输入其他报错,b是int类型
print(b)

#if语句

if b < 0 :
    b = 0
    print('negative changed to zero') #输出字符串
elif b == 0:
    print('zero')
elif b == 1:
    print('single')
else:
    print('more')
```
输出
```
please enter an data: 21
21
please enter an integer: 1
1
single

```

## for statements  for 语句
###for-example
```
#!/usr/bin/env python
# coding=utf-8
'''
用for输出列表中的字符串
'''
words = ['cat','windows','linux','strings']

#for语句
for x in words: #x为words中的子集word[0...3],word[0]=cat
    print(x,len(x)) #输出x和len
```
输出
```
cat 3
windows 7
linux 5
strings 7
```
###for-example1
```
#!/usr/bin/env python
# coding=utf-8
words = ['cat','windows','linux','pig']
for x in words[:]:
    if len(x) > 5:
        words.insert(0,x) #将符合条件的数据增加到words[0]中
        print(words)
```
输出
```
['windows', 'cat', 'windows', 'linux', 'pig']
```

##the range() function  range()函数
```
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
```
输出格式
```
please output i: 0	
please output i: 1	
please output i: 2	
please output i: 3	
please output i: 4	
please output i: 5	
please output i: 6	
please output i: 7	
please output i: 8	
please output i: 9	


please output x: 5	
please output x: 6	
please output x: 7	
please output x: 8	
please output x: 9	


please output b: 0	
please output b: 3	
please output b: 6	
please output b: 9	


please output c: -10	
please output c: -40	
please output c: -70	


0 mary
1 had
2 a
3 little
4 lamb
range(0, 10)
[0, 1, 2, 3, 4]
```

## break and contiune statements, and else clauses on loops  循环中的break,contiune,else子句
```
#!/usr/bin/env python
# coding=utf-8
for n in range(2,10): #从2到10
    for x in range(2,n):#从2到n  双重循环
        if n % x == 0 :
            print(n,'equals',x,'*',n//x)
            break  #停止循环
        else:
            print(n,'is a prime number')

for num in range(2,10): 
    if(num % 2 == 0): #求余
        print("found an even number",num)
        continue #继续循环
    print("found a number",num)
```
输出格式
```
3 is a prime number
4 equals 2 * 2
5 is a prime number
5 is a prime number
5 is a prime number
6 equals 2 * 3
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 equals 2 * 4
9 is a prime number
9 equals 3 * 3
found an even number 2
found a number 3
found an even number 4
found a number 5
found an even number 6
found a number 7
found an even number 8
found a number 9
```

## pass statements pass语句
### 遇到pass语句,两种情况
+ 语句中，会使程序等待在那里，需要强制断开（ctrl+c）
+ 类中，构造一个空类，适合以后想到东西可以直接在这里补充
### example
```
#!/usr/bin/env python
# coding=utf-8
while True:
    pass
#不能输出，程序等待，一直运行
```
### class
```
#!/usr/bin/env python
# coding=utf-8
class MyEmptyClass:
    pass
#这个空类可以以后用
```
### def
```
#!/usr/bin/env python
# coding=utf-8
def initlog(*args):
    pass
```

## defining function 定义函数
### fibnacci
```
#!/usr/bin/env python
# coding=utf-8
#example1
def fibnacci(n):
    a,b = 0,1
    while a<n :
        print(a,end=',')
        a,b = b , a+b
#输出需要在函数外面     
print(fibnacci(1000))

#example2
def fibnacci2(n):
    result = [] #result为输出结果
    a,b = 0 , 1 
    while a < n:
        result.append(a)#将a增加如result
        a,b = b , b+a
    return result #返回结果
print('实例输出：\n')
print(fibnacci2(100)) 
```
输出
```
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,None
实例输出：

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

## more on defining function  更多的定义函数
### default argument values  默认参数值,只能指向不变对象
```
#!/usr/bin/env python
# coding=utf-8
'''
默认参数值
'''
def ask_ok(prompt , retries=4 , reminder='please try again!'): #retries,reminder为默认参数
    while True :
        ok = input(prompt)
        if ok in ('y','ye','yes'):#输入其中的一个
            return True 
        if ok in ('n','no','nop','nope'):#如果第一个为真，这句将不执行
            return False
        retries = retries-1 #每执行一次，retries-1
        if retries < 0 : #当执行完次数，则报错
            raise ValueError('invalid user response')
        print(reminder) #打印结果，retries<0后重新运行程序
#这个函数参数两个参数为默认参数，默认参数如果不赋值，则默认输出
#如果赋值，则依照赋值的数据打印

    
#实例1
print(ask_ok('Do you really want to quit?'))
#实例2
print(ask_ok('OK to overwrite the file ?',2))#2为retries赋值
#实例3
print(ask_ok('OK to overwrite the file ?',2,'Come on , inly yes or no!'))
```

实例1
```
Do you really want to quit?
please try again!
Do you really want to quit?
please try again!
Do you really want to quit?
please try again!
Do you really want to quit?
please try again!
Do you really want to quit?
Traceback (most recent call last):
  File "def-default-argument-values.py", line 22, in <module>
    print(ask_ok('Do you really want to quit?'))
  File "def-default-argument-values.py", line 15, in ask_ok
    raise ValueError('invalid user response')
ValueError: invalid user response

```
实例2
```
OK to overwrite the file ?
please try again!
OK to overwrite the file ?
please try again!
OK to overwrite the file ?
Traceback (most recent call last):
  File "def-default-argument-values.py", line 24, in <module>
    print(ask_ok('OK to overwrite the file ?',2))#2为retries赋值
  File "def-default-argument-values.py", line 15, in ask_ok
    raise ValueError('invalid user response')
ValueError: invalid user response
```
实例3
```
OK to overwrite the file ?
Come on , inly yes or no!
OK to overwrite the file ?
Come on , inly yes or no!
OK to overwrite the file ?
Traceback (most recent call last):
  File "def-default-argument-values.py", line 26, in <module>
    print(ask_ok('OK to overwrite the file ?',2,'Come on , inly yes or no!'))
  File "def-default-argument-values.py", line 15, in ask_ok
    raise ValueError('invalid user response')
ValueError: invalid user response

```

##arg  默认参数
```
#!/usr/bin/env python
# coding=utf-8
i = 5 
def f(arg = i):
    print(arg)
i = 6
f()

#实例
print(f())
```
输出
```
5
5
None
```
##f   默认参数
```
#!/usr/bin/env python
# coding=utf-8
def f(a , L = []): 
    L.append(a) #将变量a增加入L
    return L
#实例1
print(f(1))
print(f(2))
print(f(3))
print(f(4,[1,2,3,4]))
print(f(4,[1,2,3,4]))
print(f(1))
print(f(2))
print(f(3))
```
输出
```
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4, 4]
[1, 2, 3, 4, 4]
[1, 2, 3, 1]  #当为默认参数重新赋值，此后的默认参数将会改变
[1, 2, 3, 1, 2]
[1, 2, 3, 1, 2, 3]
```
### f_example  默认参数
```
#!/usr/bin/env python
# coding=utf-8
def f_example(L=[]):
    L.append('END')
    return L
print(f_example())
print(f_example([1,2,3]))
print(f_example())

```
输出
```
['END'] 
[1, 2, 3, 'END']  #现在默认参数为END
['END', 'END']  #第一个为默认参数，后面一个是增加的
```
## varied argument  可变参数
## def-varied
```
#!/usr/bin/env python
# coding=utf-8
'''
可变参数
'''
def varied(*numbers): #可变参数,可以传入多个参数,*numbers相当于一个元组tuple
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(varied(1,3,4,5))
```
输出
```
51  #可变参数能同时输入多个参数，组合成元组，进行运算
```

## keyword arguments  关键字参数,需要关键字和关键字值形式keyword=value
### parrot
```
#!/usr/bin/env python
# coding=utf-8
def parrot(voltage,state = 'a stiff',action = 'voom',type = 'Norwegian Blue'):
    print('--this parrot wouldn\'t',action,end='') #用空格分开
    print("if you put",voltage,"volts though it.") 
    print("--lovely plumage , the ",type )
    print("it's",state , "!")

#实例1
#print(parrot(1000)) #voltage值为1000，其他使用默认变量 位置参数
#实例2
#print(parrot(voltage=1000))  #关键字参数
#实例3
#print(parrot(voltage=10000000,action='VOOOOOM'))#输出输入的值 1个位置参数，1个关键字参数
#实例4
#print(parrot(action='VOOOOOM',voltage=100000))#两个关键字参数
#实例5
print(parrot('a million','bereft of left', 'jump'))#这三个数据填在parrot的前三个参数位，三个位置参数
#实例6
parrot('a thousand', state='pushing up the daisies')#将数据一次填入参数位（指定参数除外），1个位置参数，1个关键字参数
```
输出
```
--this parrot wouldn't voomif you put 1000 volts though it.
--lovely plumage , the  Norwegian Blue
it's a stiff !
None
--this parrot wouldn't voomif you put 1000 volts though it.
--lovely plumage , the  Norwegian Blue
it's a stiff !
None
--this parrot wouldn't VOOOOOMif you put 10000000 volts though it.
--lovely plumage , the  Norwegian Blue
it's a stiff !
None
--this parrot wouldn't VOOOOOMif you put 100000 volts though it.
--lovely plumage , the  Norwegian Blue
it's a stiff !
None
--this parrot wouldn't jumpif you put a million volts though it.
--lovely plumage , the  Norwegian Blue
it's bereft of left !
None
--this parrot wouldn't voomif you put a thousand volts though it.
--lovely plumage , the  Norwegian Blue
it's pushing up the daisies !
```

无效的输入
```
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```
## named keyword parameters  命名关键字参数，传入的关键字参数不受限制
### cheeseshop
```
#!/usr/bin/env python
# coding=utf-8
'''
命名关键字参数
'''
def cheeseshop(kind , *arguments , **keywords):#命名关键字参数使得关键字参数传入不受限制
    print("--Do you have any ",kind , "?")
    print("--i'm  sorry , we're all out of ",kind)
    for arg in arguments : #*arguments为可变参数,可以输入多个参数
        print(arg) #arg将多个参数分别提取出来
    print("-"*40)
    for kw in keywords: # **keywords为关键字参数，需要keyword=value组合   
        print(kw , ":",keywords[kw]) #kw为关键字，keywords[]为值

print(cheeseshop("Limburger","it's very runny,sir","it's really very , very runny ,sir",shopkeeper = "michael Palin",client = "John Cleese",shetch = "Cheese Shop shetch"))
```
输出
```
--Do you have any  Limburger ?
--i'm  sorry , we're all out of  Limburger
it's very runny,sir
it's really very , very runny ,sir
----------------------------------------
shetch : Cheese Shop shetch
client : John Cleese
shopkeeper : michael Palin
None
```

## arbitrary argument lists  可变参数

### varied
```
#!/usr/bin/env python
# coding=utf-8
'''
可变参数
'''
def varied(*numbers): #可变参数,可以传入多个参数,*numbers相当于一个元组tuple
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(varied(1,3,4,5))
```
输出
```
51  #可变参数能同时输入多个参数，组合成元组，进行运算
```

### concat
```
#!/usr/bin/env python3
# coding=utf-8
def concat(*args,sep="/"):#可变参数和默认参数
    return sep.join(args)
#实例
print(concat("earth","mars","venus"))#只为可变参数赋值
print(concat("earth","mars","venus",sep=".")) #可变参数和默认参数
```
输出
```
earth/mars/venus
earth.mars.venus
```

## unpacking argument lists  解出参数列表
```
#!/usr/bin/env python
# coding=utf-8
'''
元组
'''
a = list(range(3,6))
print(a) #用list函数将range(3,6)中的参数解压

args = [3,7]
b = list(range(*args))
print(b) #用list函数将range中的可变参数解压
```
输出
```
[3, 4, 5]
[3, 4, 5, 6]
```

### parrot
```
#!/usr/bin/env python
# coding=utf-8
'''
参数解压
'''

def parrot(voltage,state='a stiff',action='voom'):
    print("-- this parrot wouldn't",action,end=' ')
    print("if you put ",voltage,"volts though it.",end=' ')
    print("E's ",state,"!")
d = {"voltage":"four million","state":"bleedin' demised","action":"VOOM"}
print(parrot(**d)) #传递命名关键字参数，字典
```
输出
```
-- this parrot wouldn't VOOM if you put  four million volts though it. E's  bleedin' demised !
None
```

## lambda expressions  lambda匿名函数
```
#!/usr/bin/env python
# coding=utf-8
'''
匿名函数
'''
def make(n):
    return lambda x: x+n #匿名函数设置一个简单的参数，在式中进行简单计算
#实例
f=make(42) #这里的43为n值

print(f(39)) #这里的39是x值
#lambda 用作函数
#>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
#>>> pairs.sort(key=lambda pair: pair[1])
#>>> pairs
#[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```
输出
```
81
```

## documentation strings  文档字符串，用作说明文档
### my_function
```
#!/usr/bin/env python3
# coding=utf-8
'''
文档字符串，用作说明文档
'''
def my_function():
    """Do nothing , but document it.

    No really , it doesn't do anything
    """
    pass 

#实例
print(my_function.__doc__) #"__"需要两个杠
```
输出
```
Do nothing , but document it.

    No really , it doesn't do anything
```

## function annotations  函数注释
### fn
```
#!/usr/bin/env python
# coding=utf-8
'''
函数注释
'''
def fn(ham:str,eggs:str='eggs')->str:
    print("annotations: ",fn.__annotations__)#函数注释所在的隐藏属性
    print("arguments: ",ham,eggs) #函数参数输出
    return ham+"and"+eggs
#实例
print(fn('spam')) 
```
输出
```
annotations:  {'return': <class 'str'>, 'ham': <class 'str'>, 'eggs': <class 'str'>}
arguments:  spam eggs
spamandeggs
```
