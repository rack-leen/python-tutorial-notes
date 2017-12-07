# classes 类

## a word about names and objects 名称和对象
+ 对象是私有的，多个名称能被绑定到相同的对象中

这些名称也被称为别名，避免命名与关键字冲突
这些类中的名称只能在类中使用，不能用在类外。
名称能够忽视不变的基类型（strings,numbers,tuples）
但是，用在可变化的对象中（lists,dictionaries,and most other types）会有一些语义冲突。
名称的作用有时与指针有一些方面相似.

## python scopes and namespaces python作用域和名字空间

+ 名称空间是名称到对象的映射

+ 名称空间的例子
内建名称（包含函数和内建异常名称），在模块中的全局名称，函数调用的中本地名称，一个对象的属性集也可以看做名称空间

+ 在不同名称空间中的名称是没有关联的
例如，两个模块定义了相同的名称，但是两个模块中的名称作用域不同，是不相关联的。

+ attribute(属性)
具体表现是做为点（'.'）
z.real   real是对象z的属性
moudlename.function moudlename是模块对象，function是模块对象的属性
模块属性与模块中定义的全局变量都共享同样的名称空间
属性可以是只读或者可写。可写的属性可以写入，也可以被删除（moudlename.function=42,del moudlename.function）

+ 名称空间生存期
python解释器开启时会创建包含内建名称的名字空间，并且永远不会被删除。
模块中的全局名称空间在模块定义被读入时被创建，模块名字空间会持续存在，直到解释器退出
由解释器的顶层调用执行的语句，无论是从脚本读入，还是交互式，都被认为是模块中\_\_main\_\_的一部分，它们有自己的全局名称空间（内建名称也是在模块中，被称为builtins）

+ 作用域
作用域是一个名称空间可以直接访问的文本区域

+ 正在执行的程序，至少有三个嵌套的作用域，他们的名称空间是可以直接访问的。
最内部的作用域（包含本地变量，第一个被搜索）
从最近的封闭作用域开始搜索的任何封闭函数的作用域，包含非本地也包含非全局名称。
下一个包含现在模块的全局名称的持续作用域
最外围的作用域是是包含内建名称的名称空间

如果一个名称被声明为全局的，那么所有的引用和赋值都会直接进入包含模块全局名称的中间范围。
为了重新绑定在最内层范围之外发现的变量，可以使用nonlocal语句:如果不声明nonlocal，则这些变量是只读的(对这样一个变量进行写入的尝试只会在最内层的范围内创建一个新的局部变量，从而保持不变的外部变量不变)。

global可以用来表示特定的变量在全局范围内，并且应该在那里进行重新绑定;
nonlocal语句表示特定的变量存在于一个封闭的范围内并且应该在那里进行重新绑定

### scopes and namespaces example 作用域和名字空间例子
```
#!/usr/bin/env python3
# coding=utf-8

def scope_test():
    def do_local():
        spam = "local spam" #局部名称

    def do_nonlocal():
        nonlocal spam 
        spam = "nonlocal spam" #nonlocal名称

    def do_global(): #nonlocal改变局部名称后，现在的局部名称为spam="nonlocal"
        global spam
        spam = "global spam" #局部名称

    spam = "test spam" #为全局名称
    
    do_local()
    print("After local assignment:",spam) #输出的是test spam，因为局部名称不能修改全局名称，所以输出的是全局名称的值
    do_nonlocal()
    print("After nonlocal assignment:" , spam) #输出的是nonlocal spam,因为nonlocal可以改变spam绑定的名称
    do_global()
    print("After global assignment:",spam)#输出的还是nonlocal，因为global绑定为全款名称，改变global定义的spam实际上为全局名称spam="test spam"

scope_test()
print("in global scope:",spam) #输出的是global，因为全局名称绑定被global改变了，改变为global所在函数的spam
```
输出

```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
in global scope: global spam
```

## a first look at classes

### 类的形式
```
class ClassName:
    <statement-1>
    ...
    ...
    ...
    <statement-n>
```

### 类对象
+ 类是一个属性和方法的集合

例如，students是一个类，指的是学生这个集合

+ 对象，也称为实例，是一个类的具体实现。类对象就是可以用类名直接表示的对象,支持两种操作属性引用(也称为类方法)和实例化

例如，student是Student这个类的具体实现，一个群体中具体的某一个人。
首先，定义一个类
```
class Student:
	pass

bart = Student() #这是一个实例，将Student看做一个函数。在其中有很多对象，它将返回一个对象，并赋值给bart，bart成为了一个实例，也就是对象。
```

#### 实例的属性和方法

实例的属性也就是对象的变量，与c++需要中的prviate中的变量差不多，能被方法调用。
实例的方法，实例绑定的函数，也称为公有接口，与c++中public中的公共接口类似。实例能够通过公共接口调用实例变量。但是不能直接修改实例变量。	

+ 属性引用
标准语法为obj.name;在类被创建后有效的属性名称在类的名称空间中。

+ 实例绑定属性

bart是指向实例的，它就代表了实例本身，bart通过运算符'.'来引用属性。
```
class Student(object):
	def __init__(self,name,score):
		self.name = name    #为实例对象绑定属性
		self.score = score #self是代指对象本身，和上面的bart差不多。
```
+ 实例方法的使用

需要实例化一个对象，将对象名赋值给self使用

+ 类对象是一个模板，类实例是这个模板的具体体现，实例化将会创建一个对象，对象将会具有特定的初始状态
```
#!/usr/bin/env python
# coding=utf-8

class MyClass:
    """
    A simple example clss.
    """
    i = 123456 #为类的属性

    def f(self):#指代的是对象本身（类实例），代表当前对象地址，避免非限定调用造成的全局变量
        return 'hello world'

    #MyClass.i（返回整型）和MyClass.f（返回函数）都是有效的属性引用
    #__doc__也是一个有效的属性，返回属于类的docstring：'A simple example clss.'


    #类实例化使用函数表示法，假设类对象是一个没有参数的函数，它将返回一个新实例
    #x = MyClass() #创建一个新实例，并将这个对象赋给局部变量x
    def __init__(self):#self指代类对象
        self.data = [] #这是类的实例化,将会创建一个空对象
```
+ 方法也可以有具有更大灵活性的参数，方法的参数将会被传递给类实例
类当做函数时，类后面的参数则是类实例
```
#! /usr/bin/python3
# coding=utf-8
class Complex:#类对象
    def __init__(self,realpant , imagpart):
        self.r = realpant   #绑定属性
        self.i = imagpart #绑定属性
#x为新的类实例
x = Complex(3.0,-4.5) #这两个参数就是self.r,self.i这两个类实例，x为实例对象 
#实际上这后面的参数是__init__方法中的参数，通过类实例传递给了x
print(x.r,x.i)
```
输出
```
3.0 -4.5
```

### 实例对象

+ 类能实例化，对象也可以实例化，对象的实例化就是对象的属性引用
```
#接上面的类
#对象实例化
x.counter = 1  #对象实例的初始状态
while x.counter < 10: #属性引用也可以称为方法，这是属于对象的方法
    x.counter = x.counter * 2
print(x.counter)
del x.counter #删除
```
输出
```
3.0 -4.5
16
```

### method objects 方法对象
```
#接上MyClass类
x = MyClass() #从MyClass类中返回一个对象，赋给x,这里的x.f()其实是等效于Myclass.f
xf = x.f      #x对象调用f方法，并赋给xf
while True :
    print(xf()) #xf现在就是x.f方法
```

### class and instance variables 类和实例的变量
+ 类变量
是所有对象共享的变量
```
#! /usr/bin/python3
#-*-coding-*-

'''
类和实例变量
'''

class Dog:
    kind = 'canine'  #所有dog的种类，每一只dog共同拥有的属性
    def __init__(self,name): #dog name,每条dog有不同的name
        self.name = name    #为实例绑定属性


d = Dog('Fido')  #创建一个实例，d是一条叫Fido的dog
e = Dog('Buddly') #创建另一个实例，e是一条叫Buddly的dog

print('d is a ',d.kind) #调用的是类变量
print('e is a ',e.kind)

print('d is a ',d.name) #调用的是本实例的变量
print('e is a ',e.name)
```
输出
```
d is a  canine
e is a  canine
d is a  Fido
e is a  Buddly
```
+ 将数据添加到类变量
这会使数据在所有对象实例中共享
```
#! /usr/bin/python3
#coding:utf-8

class Dog:
    tricks = [] 
    def __init__(self,name):
        self.name = name
    def add_trick(self,trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddly')
d.add_trick('roll ever')
e.add_trick('play dead')#e使用方法，增加trick到tricks

print(d.tricks)#tricks是一个类变量，被所有实例共享,所以每个实例向tricks增加内容都会被所有实例共享

print(Dog.tricks)
#在这里Dog.tricks(所有对象共享的属性)与d.tricks(对象的属性)显示相同.
```
输出
```
['roll ever', 'play dead']
['roll ever', 'play dead']
```

+ 实例变量
各个对象实例所独有的变量，只能被所属实例调用

```
#! /usr/bin/python3
#coding:utf-8

class Dog:
    def __init__(self,name):
        self.name = name
        self.tricks = [] #给实例的属性绑定一个空列表

    def add_trick(self,trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddly')

d.add_trick('roll ever')
e.add_trick('play dead')

print(d.tricks)
print(e.tricks) #有对象属性
#print(Dog.tricks)#Dog没有类属性tricks
```
输出
```
['roll ever']
['play dead']
```

## random remarks

+ 函数定义在类外面,在类定义中，函数包含在类中是不必要的
```
#!/usr/bin/env python
# -*-coding=utf-8-*-

#函数定义在类外面

def fi(self,x,y):
    return min(x,x+y)
class C:
    f = fi

    def g(self):
        return 'hello world'
    h = g 
```

+ self参数也可以放在类的其他方法中
```
#!/usr/bin/env python
# -*-coding=utf-8-*-

class Bag:
    def __init__(self):
        self.data = []

    def add(self,x):
        self.data.append(x)

    def addtwice(self,x):
        self.add(x)
        self.add(x)

#实例
d = Bag()
d.add(7) #添加元素到列表
d.add(8)
print(d.data) #输出列表
```
输出
```
[7, 8]
```

## inheritance 继承
继承是子类继承父类的属性和方法
+ 继承的形式
```
class DeriveClassName(BaseCalssNmae): #括号中的为父类
    <statement-1>
    ...
    ...
    ...
    <statement-n>
#父类定义在其他模块
class DeriveClassName(moudlename.BaseClassNmae):
```
+ 继承的例子
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
类继承
'''
#父类动物
class Animal(object):
    def run(self):
        print('Animal is running......')


#子类
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()   #dog类继承了Animal类,可以直接使用Animal的属性和方法
cat = Cat()
cat.run()
```
输出
```
Animal is running......
Animal is running......
```
+ 多态
对继承的延伸，子类可以定义与父类相同的方法，子类的方法输出将会覆盖父类的方法输出
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
继承的多态
'''

class Animal(object):
    def run(self):
        print('Animal is running......')

class Dog(Animal):
    def run(self):
        print('Dog is runing......')
    def eat(self):
        print('Dog eating meat......')

class Cat(Animal):
    def run(self):
        print('Cat running......')

#现在输出的是子类定义的函数输出，也就是父类同名函数被覆盖了
dog = Dog()
cat = Cat()

dog.run()
dog.eat()
cat.run()
```
输出
```
Dog is runing......
Cat running......
```
+ 检查对象继承和判断实例类型

isinstance(obj,int):检查实例的类型
issubclass(bool,int):检查类继承,返回true false

### multiple inheritance 多重继承
+ 多重继承形式
```
class DeriveClassName(Base1,Base2,Base3):
    <statement-1>
    ...
    ...
    ...
    <statement-n>
```

+ 多重继承定义
多重继承是动态语言的特色，一个子类能够同时继承多个父类的属性和方法

## private variables 私有变量

+ 私有变量与访问限制
私有变量是只有内部可以访问，外部不能访问。
+ 私有变量形式
在普通变量之前加上两个下划线，如self.\_\_name，这就是私有变量
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
私有变量
'''

class Mapping:
    def __init__(self,iterable):
        self.items_list = []  #相当于在函数中定义的变量
        self.__update(iterable) #调用方法

    def update(self,iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update #将update方法的副本复制给私有变量

class MappingSubclass(Mapping): #子类
    def update(self,keys,values):
        for item in zip(keys,values): #将keys,values组装返回一个元组
            self.items_list.append(item)
```

## 其他
+ 类也有c语言中struct数据类型的作用
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
将类当做struct数据类型
'''
class Emptyclass:
    pass

join = Emptyclass()

join.name = 'john Doe'
join.dept = 'computer lab'
join.salary = '1000'

#实例

print(join.name,"\n",join.dept,"\n",join.salary)
```
输出
```
john Doe 
 computer lab 
 1000
```
## 迭代器
+ for语句用于迭代
```
+ 用for循环进行迭代
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
迭代器，用for进行迭代
'''

for element in [1,2,3]: #list
    print(element)
for element in (1,2,3): #tuple
    print(element)
for key in {'one':1,'two':2}: #dictionary
    print(key)
for char in "123": #string
    print(char)
for line in open("myfile.txt"):
    print(line)
```
输出
```
1
2
3
1
2
3
one
two
1
2
3
this is a txt .
```
+  for 语句调用iter()进行迭代
```
#!/usr/bin/env python
# -*-coding=utf-8-*-

s = 'abc'
it = iter(s) #用于迭代的内建函数

print(it)
print(next(it)) #next函数表示显示下一个迭代的值
print(next(it))
print(next(it))
print(next(it))
```
输出
```
<str_iterator object at 0x7ffbce6ae9e8>
a
b
c
Traceback (most recent call last):
  File "class_iterator_next.py", line 11, in <module>
    print(next(it))
StopIteration       #当迭代对象为空时，则返回错误,停止迭代
```

+ 定义一个iter()方法，返回\_\_next\_\_()方法

```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
定义一个__iter__()方法，用__next__()方法返回一个对象
'''

class Reverse:
    def __init__(self,data):
        self.data = data 
        self.index = len(data) #返回data长度
    def __iter_(self):
        return self        #
    def __next__(self):
        if self.index == 0: #数据长度为0则停止迭代
            raise StopIteration #将引发异常
        self.index = self.index - 1 #数据长度-1
        return self.data[self.index] #返回第i个数据

rev = Reverse("spam")
for char in rev:
    print(char)
#不知为什么，不能迭代，输出错误
```

## generators 生成器

+ 生成器是一个简单的用来创建迭代器的工具.与普通函数差不多，但是用yield返回.
生成器自动创建\_\_iter()\_\_和\_\_next()\_\_方法，生成器实现的函数也可以用迭代器实现。
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
生成器，用yield返回
'''

def reverse(data):
    for index in range(len(data)-1,-1,-1): #从后面开始循环到开始
        yield data[index]   #由于是列表，从0开始，需要-1

for char in reverse('golf'):
    print(char)
```
输出
```
f
l
o
g
```
## generator expressions 生成器表达式

+ 是一些简单的生成器被编码为表达式，它使用像列表生成式的语法，但是‘"\[\]"换为"()"
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
生成器生成式
'''
#求i的平方
a = sum(i*i for i in range(10))
print(a)

#两个列表乘积
xvec = [10,20,30]
yvec = [7,6,4]
b = sum(x*x for x,y in zip(xvec,yvec)) #用zip函数将两个列表组装成元组
print(b)

#
from math import pi,sin
sine_table = {x:sin(x*pi/180) for x in range(0,91)}
unique_words = set(word for line in page for word in line.split())
vaiedictorian = max((student.gpa,student.name) for student in graduates)
data = 'golf'
list(data[i] for i in range(len(data)-1,-1,-1))
```
输出
```
285
1400
Traceback (most recent call last):
  File "class_generator_expression.py", line 19, in <module>
    unique_words = set(word for line in page for word in line.split())
NameError: name 'page' is not defined

```
