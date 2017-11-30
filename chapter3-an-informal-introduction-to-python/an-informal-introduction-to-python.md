# using python as a calculator //将python做为计算器
## numbers  //整数
### numbers1.py 整数运算
```
#!/usr/bin/python3
# coding=utf-8
'''
这个程序是整数之间的运算
有- + * /等运算
'''
print ("请输入整数")
a = 2+2
b = 50 - 5*6
c = (50-5*6)/4
d = 8/5

print ('plus:',a)  #单变量输出
print ("minus:%d\nmultiplied:%.2f\nexcpept%.2f\n" %(b,c,d)) #格式化输出
```
输入输出
```
input:python3 numbers.py 
output:
请输入整数
plus: 4
minus:20
multiplied:5.00
excpept1.60   #python3现在能让/输出浮点数
```

### numbers2.py 运算符的运用和指数
```
'''
/ % // 运算符的运用和指数
'''
#!/usr/bin/env python
# coding=utf-8

print ("请输入：\n")
a = 17/3
b = 17//3
c = 17%3
d = 5*3+2
e = 5**2
f = 2**7
print("a = %f\nb = %f\nc = %d\nd = %d\ne = %d\nf = %d\n"%(a,b,c,d,e,f))
```
输出浮点数和指数
```
请输入：

a = 5.666667
b = 5.000000
c = 2
d = 17
e = 25
f = 128
```

### numbers3.py 变量运算
```
'''
变量运算
'''
#! /usr/bin/python3
# coding:utf-8
print("请输入变量：\n")
width = 20
height = 5*9
print("the add : %d\n"%(width*height))
```
输出 
```
请输入变量：

the add : 900
```

### numbers4.py 其他运算
``````
#!/usr/bin/python3
# coding=utf-8
'''
其他运算
'''
a = 4*3.75-1
tax = 12.5/100
price = 100.50
c = price*tax
#在python解释器下price+_  '_'表示继续上一个运算的结果，与price相加
print("a = %f\ntax = %f\nc = %f\n"%(a,tax,c))

a = 14.000000
tax = 0.125000
c = 12.562500
``````

## strings
``````
#!/usr/bin/env python
# coding=utf-8
print("spam eggs")
print("does\'t")
print("does't") #print('does't')不正确，''单引号不能
print('yes",he said.')
print("\"yes\",he said.") #用反斜杠
print('"isn\'t",she said.') #字符串加引号不用反斜杠需要将双引号改为单引号
#>>> '"isn\'t",she said'
#'"isn\'t",she said'  
#在解释器下与脚本下的显示不一样
s = 'first line.\nsecond line.'
print(s)
print('C:\some\name') #C:\some
                      #ame
print(r'C:\some\name') #C:\some\name
print("""
      Usage: thingy [OPTIONS]
      -h                 Display this Usage message
      -H hostname        hostname to connect to
      """) #打印帮助信息
print(3*'un'+'ium') #复制un三次
print('Py''thon') #连接多个字符串
text = ('put several strings within parenteses' 'to have them joined together.') #将两个字符串连接成一个字符串
print(text)
prefix = 'Py'
print(prefix + 'thon')

word = 'Python'
print(word[0])
print(word[5])#利用列表输出字符
print(word[-1])#从最后的字符开始取字符
print(word[-4])
print(word[2:4])#只选取2到4之间的字符
print(word[0:2]+word[2:4])#将两个选取的字符串连接
print(word[-2:]) #选取倒数第二个字符串到最后
print('J'+word[1:])#将J和选取的字符串连接
print(word[:2]+'Py')
s = 'supercaliasdfdgfdhgfj'
print(len(s))#字符串长度
``````
输出
``````
spam eggs
does't
does't
yes",he said.
"yes",he said.
"isn't",she said.
first line.
second line.
C:\some
ame
C:\some\name

      Usage: thingy [OPTIONS]
      -h                 Display this Usage message
      -H hostname        hostname to connect to
      
unununium
Python
put several strings within parentesesto have them joined together.
Python
P
n
n
t
th
Pyth
on
Jython
PyPy
21
``````
## list //列表
+ 列表是一个数据可变的结构，列表中的数据字符数字都可以
+ 列表的功能
1.增加数据append方法
2.切割列表【：】
3.连接两个列表
4.列表中的列表，列表可以包括子集列表
``````
#!/usr/bin/env python
# coding=utf-8
'''
列表
'''
squares = [1,4,8,16,25]
print(squares)  #输出列表数据
print(squares[0])
print(squares[-1])
print(squares[-3:]) #从倒数第三个数据到最后一个数据
print(squares[:])#相当于直接输出列表全部数据
print(squares + [36,64,81,100])#直接在列表后面增加数据

#替代列表中的数据
cubes = [1,8,65,125.78]
print(cubes)
cubes[3] = 64
print(cubes)

#用append()方法增加数据
cubes.append(216)
print(cubes)

cubes.append(7**2)#增加指数
print(cubes)

#列表中的字符串
letters = ['a','b','c','d','e','f','g']
print(letters)
#替代列表中的一串字符
letters[2:5] = ['C','D','E'] #从2到5的数据替换成另外三个数据
print(letters)
letters[2:5] = [] #将2到5的数据替换为空
print(letters)
letters[:] = [] #将整个列表数据替换为空

letters = ['a','b','c','d']
print(len(letters)) #打印字符串长度
#将列表字符与数字连接
a = ['a','b','c','d']
b = [1,2,3]
c = [a,b]   #将a和b做为c列表的子集
print(c) #输出整个列表
print(c[0])#输出列表的第一个子集a
print(c[0][1]) #输出列表的第一个子集的第二个数据

``````
输出列表
`````
[1, 4, 8, 16, 25]
1
25
[8, 16, 25]
[1, 4, 8, 16, 25]
[1, 4, 8, 16, 25, 36, 64, 81, 100]
[1, 8, 65, 125.78]
[1, 8, 65, 64]
[1, 8, 65, 64, 216]
[1, 8, 65, 64, 216, 49]
['a', 'b', 'c', 'd', 'e', 'f', 'g']
['a', 'b', 'C', 'D', 'E', 'f', 'g']
['a', 'b', 'f', 'g']
4
[['a', 'b', 'c', 'd'], [1, 2, 3]]
['a', 'b', 'c', 'd']
b
`````
## first steps towards programming //首次编程
### fibonacci //斐波拉契数
``````
'''
#!/usr/bin/env python
# coding=utf-8
'''
fibonacci数
'''
a,b = 0,1
while b < 10 :
    print(b) #先输出b
    a,b = b,a+b #可以分解为a = b b = a+b
``````
输出fibonacci
 `````
1
1
2
3
5
8
`````
### 格式化输出
```
#!/usr/bin/python3
#coding:utf-8

i = 258*258
print('the value of i is',i)
```
输出
```
the value of i is 66564
```
### 变种fibonacci表示
```
#!/usr/bin/env python
# coding=utf-8

#!/usr/bin/env python
# coding=utf-8
'''
fibonacci数
'''
a,b = 0,1
while b < 1000 :
    print(b,end=',') #用，来分割输出数据
    a,b = b,a+b #可以分解为a = b b = a+b
```
输出fibonacci1
```
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```

