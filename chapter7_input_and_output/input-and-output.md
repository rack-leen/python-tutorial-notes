# input and output  输入与输出
## fancier output formatting 更好看的输出格式
### old string
## reading and wrtiing
### methods of files objects
### saving structured data with json


## fancier output formatting 更好看的输出格式
+ 处理所有的字符串
用字符串的切割和连接操作创建自己需要的布局
+ 使用str(适用于人机交互)和repr(适用于解释器理解)输出
+ 格式化字符串或者使用str.format()方法

```
#!/usr/bin/env python
# coding=utf-8

s = 'Hello world.'
print(str(s)) #字符串输出格式,用于将值转换为适用于人阅读的形式
print(repr(s)) #返回一个字符串，将值转换为适用于解释器的形式
print(str(1/7)) #将数值转换为字符串输出

x = 10*3.25
y = 200*200
s = 'the value of x is '+ repr(x) + ' ,and y is ' + repr(y) + '...'
print(s)

hello = 'Hello , world.\n'
print(hello) #print会将\n判断为换行符
hellos = repr(hello) #repr会将\n判断为一个字符
print(hellos)
print(repr((x,y,('spam','eggs')))) #repr的参可以是任何python对象

#输出平方和立方的两种方法
for i in  range(1,11):
    print(repr(i).rjust(2),repr(i*i).rjust(3),end=' ')#第一大列和第二大列所占空格分别为两个和三个（每一大列容纳酔大的空格数）
    print(repr(i*i*i).rjust(4)) #第三大列所占空格为四个

for x in range(1,11):
    print('{0:2d},{1:3d},{2:4d}'.format(x,x*x,x*x*x))#每列的空格由print()增加的
#repr.rjust()方法表示向右对齐

#str.zfill()表示向左填充0，如下
a = '12'.zfill(5) #只有两位，不足5位，需要在前面填充0
print(a)
b = '-3.14'.zfill(7) #所有字符有5位，不足7位，需要在前面填充0
print(b)
c = '3.14159265359'.zfill(5)#由于字符串位数比给定的大，不需要填充
print(c)
d = '3.1416'.zfill(5)
print(d)
#当字符串中的字符数少于.zfill中的数字，则在前面填充0；当等于或大于时，正常输出字符串。

#.format()函数用法,format输出格式其实就是str.format()形式
print('we are the {},who say "{}"!'.format('knight','Ni'))
print('{0} and {1}.'.format('spam','eggs'))#{}中数字表示所在位置
print('{1} and {0}.'.format('spam','eggs'))#{0}表示.format中的第二个参数在输出参数中的第一个位置

#关键字参数用在format中
print('this {food} is {adjective}.'.format(food='spam',adjective='absolutely horrible'))#输出关键字参数对应的键值

#位置与关键字参数组合
print('the story is {0},{1} and {other}.'.format('Bill','Manfred',other='Georg'))

#!a(apply acsii),!r(apply repr),!s(apply str).就是将输入的转换为对应的格式
contents = 'eels'
print('my hovercraft is full of {}.'.format(contents))
print('my hovercraft is full of {!r}!'.format(contents))#转换为repr格式
print('my hovercraft is full of {!a}.'.format(contents))#转换为ascii格式
print('my hovercraft is full of {!s}.'.format(contents))#转换为str格式

#用‘':'，':'之后的整数表示字符所需要的最小范围
table = {'Sjoerd':4127,'Jack':4098,'Dcab':7679}
for name,phone in table.items(): #table.items表示关键字参数
    print('{0:10} ==> {1:10d}'.format(name,phone)) #第一个表示输出的是字符，第二个表示输出的是数字，通过位置表示键值

#通过关键字(用0[keyword]表示关键字参数)来表示键值(用d表示键值),只需要输出字典
table = {'Sjoerd':4127,'Jack':4098,'Dcab':6079493}
print('Jack:{0[Jack]:d};  Sjoerd:{0[Sjoerd]:d};''  Dcab:{0[Dcab]:d}'.format(table)) 
print('Jack:{0[Jack]:d};  Sjoerd:{0[Sjoerd]:d};'.format(table)) 

#用'**'表示关键字参数,与内建函数vars（返回一个包含本地变量的字典）联合使用
print('Jack:{Jack:d};  Sjoerd:{Sjoerd:d};''  Dcab:{Dcab:d}'.format(**table)) 

#老式的string格式
import math 
print('the value of PI is approximately %5.3f.'%math.pi)
```
输出
```
Hello world.
'Hello world.'
0.14285714285714285
the value of x is 32.5 ,and y is 40000...
Hello , world.

'Hello , world.\n'
(32.5, 40000, ('spam', 'eggs'))
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
 1,  1,   1
 2,  4,   8
 3,  9,  27
 4, 16,  64
 5, 25, 125
 6, 36, 216
 7, 49, 343
 8, 64, 512
 9, 81, 729
10,100,1000
00012
-003.14
3.14159265359
3.1416
we are the knight,who say "Ni"!
spam and eggs.
eggs and spam.
this spam is absolutely horrible.
the story is Bill,Manfred and Georg.
my hovercraft is full of eels.
my hovercraft is full of 'eels'!
my hovercraft is full of 'eels'.
my hovercraft is full of eels.
Jack       ==>       4098
Dcab       ==>       7679
Sjoerd     ==>       4127
Jack:4098;  Sjoerd:4127;  Dcab:6079493
Jack:4098;  Sjoerd:4127;
Jack:4098;  Sjoerd:4127;  Dcab:6079493
the value of PI is approximately 3.142.
```

## reading and wrtiing files 对文件进行读写操作
f.open(filename,mode) filename:文件名；mode:进行操作的方式，读操作（r）,写操作（w）,只能对文件增加数据（a）,进行读写操作（r+）

用with关键字进行文件操作,在完成任务后将会关闭文件,如果不用，需要使用f.close()函数关闭文件
```
#!/usr/bin/env python
# coding=utf-8

with open('workfile') as f:#为open()取别名
    read_data = f.read() #workfile中读取的数据放入read_data
print(read_data)
print(f.closed) #标记文件是否已经关闭，true表示正确关闭
#print(f.read()) #运行错误，表示文件确实被关闭
#f.close()
#print(f.read()) #文件
```
输出
```
this is the entire file.\n
asl;lfhdsgjkvnhbkgdsfghi

True
```
```
>>> with open('workfile') as f:
...     read_data = f.read()
>>> f.closed
True
```
```
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file
```

### methods of file objects 文件对象的方法
f.read() :读取文件
f.readline() :从文件中读取单行(用\n结尾)

