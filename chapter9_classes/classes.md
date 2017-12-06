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

### scopes and namespaces example
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
+ 类对象是可以直接使用类名字表示的对象，支持两种操作属性引用(也称为类方法)和实例化
属性引用：标准语法为obj.name;在类被创建后有效的属性名称在类的名称空间中。
类方法的使用：需要实例化一个对象，将对象名赋值给self使用
+ 类对象是一个模板，类实例是这个模板的具体体现
+ 实例化将会创建一个对象，对象将会具有特定的初始状态
```
#!/usr/bin/env python
# coding=utf-8

class MyClass:
    """
    A simple example clss.
    """
    i = 123456

    def f(self):#指代的是对象本身（类实例），代表当前对象地址，避免非限定调用造成的全局变量
        return 'hello world'

    #MyClass.i（返回整型）和MyClass.f（返回函数）都是有效的属性引用
    #__doc__也是一个有效的属性，返回属于类的docstring：'A simple example clss.'


    #类实例化使用函数表示法，假设类对象是一个没有参数的函数，它将返回一个新实例
    #x = MyClass() #创建一个新实例，并将这个对象赋给局部变量x
    def __init__(self):#self指代类对象
        self.data = [] #这是类的实例化,将会创建一个空对象
```
+ 类方法也可以有具有更大灵活性的参数，方法的参数将会被传递给类实例
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
#实际上这后面的参数是__init__方法中的参数，通过类实例传递给了Complex
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

method objects 方法对象

