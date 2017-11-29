#using python as a calculator //将python做为计算器
##numbers  //整数
###numbers1.py 整数运算
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

###numbers2.py 运算符的运用和指数
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

###numbers3.py 变量运算
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

###numbers4.py 其他运算
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

##strings
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

