# errors and exceptions 错误和异常
## syntax errors 语法错误
## exceptions 异常
## handing exceptions 处理异常
## raising exceptions 引发异常
## user-defined exceptions 用户定义异常
## defining clean-up actions 定义清理行动
## predefined clean-up actions 预定义清理行动

## syntax errors 语法错误
+ 书写不当造成
一般显示 SyntaxError错误

## exceptions 异常
+ 执行过程中检测到的错误
+ 只是一些小问题，不影响程序运行的错误
```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero   #除以0的错误
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined #名称错误，名称没有被定义
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly #类型错误
```

## handing exceptions 处理异常
+ 用try...except语句来捕捉异常错误
try后面接需要运行的语句
except后面接需要捕捉的异常错误，用自己的语言来描述这个错误
+ 如果异常没有发生，则运行try后面的语句，如果异常发生，则运行except后面的语句
```
#!/usr/bin/env python
# coding=utf-8
'''
通过异常捕捉来捕捉错误
'''
#输入数字，则正确运行程序，若输入其他字符，则显示异常
while True:
    try:  #接需要运行的语句
       x = int(input("Please enter a number :")) 
       break
    except ValueError: #接收ValueError错误
        print("Oops! that was no Valid number . try again...")
```
输出
```
Please enter a number :qw
Oops! that was no Valid number . try again... #输入的不正确则显示自定义的异常语句
Please enter a number :qw
Oops! that was no Valid number . try again...
Please enter a number :12
```
+ 一个except 子句可以将多个异常命名为一个元组
```
except (NameError,TypeError,RuntimeError):
    pass
```
+ 如果有相同类或者基类，一个except子句是与一个异常想适配的
```
class B(Execption):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
#
#如过except子句被颠倒过来，首先B与第一个循环元素匹配，输出，发生异常。输出B,B,B
```
+ 捕获详细的异常信息
```
#!/usr/bin/env python
# coding=utf-8
import sys
try :
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err)) #OSError错误
except ValueError:
    print("Couldn't convert data to an integer.") #ValueError错误
except :
    print("Unexcepted error:",sys.exc_info()[0]) #捕获详细的异常信息
    raise #引发异常

#try...except语句用else关键字

#用else,避免意外捕获由try语句保护的代码引起的异常
for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except OSError:#出现异常
        print('cannot open',arg) #打印异常信息
    else:
        print(arg,'has',len(f.readlines()),'lines') #否则正常运行程序
        f.close() #关闭文件

```
+ 实例化参数
```
#实例化参数，在添加到异常中
try :
    raise Execption('spam','rggs')
except Execption as inst: 
    print(type(inst)) #异常实例化
    print(inst.args) #将参数储存在.args数组中
    print(inst) 

    x,y=inst.args
    print('x = ',x)
    print('y = ',y)
```
+ 发生在函数里面的异常也可以用try捕获
```
#!/usr/bin/env python
# coding=utf-8
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error',err)
```
输出
```
Handling run-time error division by zero
```

## raising exceptions 引发异常

+ raise 语句允许强制指定异常发生
```
#有参数
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere #强制指定NameError错误发生
#无参数
raise ValueError  # raise ValueError()的简称
```

+ 确定一个异常是否被引发，但不处理
```
>>> try:
...     raise NameError('HiThere') #引发异常
... except NameError:
...     print('An exception flew by!') #输出自定义描述
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
#不处理异常
```

## user-defined exceptions 用户自定义异常

+ 创建异常类来命名自己的异常

```
#!/usr/bin/env python
# coding=utf-8
class Error(Exception):
    """
    Base clase for Exceptions in this moudle.
    """
    pass

class InputError(Error):
    """
    Exception raised for errors in the input .
    Attributes:
        exception -- input expression in which the error occured
        message -- explanation of the error
    """
    def __init__(self,expression,message): #self是指向类的实例（根据类创建出的具象化对象）
        self.expression = expression #self实例的expression方法
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```

## defining clean-up actions 

+ 在所有情况下被定义的清理动作

```
>>> try:
...     raise KeyboardInterrupt
... finally: #不管异常发生没有，finally都会执行
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```
+ try...except...else...finally语句连用
```
#! /usr/bin/python3
#-*-coding:utf-8-*-

'''
try...except...finally语句中使用else
'''

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero.")
    else:
        print("the result is ",result)
    finally:
        print("excuting finally clause.")

print(divide(2,1))
print(divide(2,0))
print(divide("2","1"))#不能输入字符
```
输出
```
the result is  2.0
excuting finally clause.
None
division by zero.
excuting finally clause.
None
excuting finally clause.
Traceback (most recent call last):
  File "define_clean_up_action_else.py", line 20, in <module>
    print(divide("2","1"))#不能输入字
  File "define_clean_up_action_else.py", line 10, in divide
    result = x/y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
+ conclusion
try:后面接正确运行的语句，如果没有异常，则运行
except:后面接异常类型，自定义异常描述
finally:不论是否发生异常，都会运行
else:与其他语句中的用法相同，用在异常语句中，意味着异常不会发生
raise:异常引发语句

## predefined clean-up actions

+ with 语句处理异常
```
for line in open("myfile.txt"): 
  print(line, end="")

#这段代码将会打开一个文件，但是不会关闭，这将会产生一个异常
```
但是用了with语句
```
with open("myfile.txt") as f: 
   for line in f: 
       print(line, end="")
#这将会自动关闭打开的文件。
```
