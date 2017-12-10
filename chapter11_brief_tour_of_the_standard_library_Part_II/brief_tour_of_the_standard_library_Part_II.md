# Brief Tour of the Standard Library — Part II 标准库 第二部分
## 输出格式
## 模板
## 使用二进制数据记录布局
## 多线程
## 记录
## 弱引用
## 使用列表工作的工具
## 十进制浮点运算

## 输出格式
+ reprlib模块提供一个定制的repr版本,它是大型的或者深度嵌套容器的缩写
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
repr输出格式
'''

import reprlib 

a = reprlib.repr(set('aDsupercalifragilisticexpialidocious'))
print(a) #以ascii表顺序输出不重复字母（字符串中出现的）

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
print(pprint.pprint(t,width=30)) #t以每行３０个字符的方式输出

import textwrap #格式化文本段落，以适应屏幕宽度
doc = """he wrap() method is just like fill() except that it returns,a list of strings instead of one big string with newlines to separate,the wrapped lines.""" 
print(textwrap.fill(doc,width=40)) #只能用文本方式

#多语言模块
import locale
locale.setlocale(locale.LC_ALL,'English_United States.1252') #设置语言
conv = locale.localeconv() #获取约定的映射
x = 1234567.8
locale.format("%d",x,grouping=True) #格式化x为整型
locale.format_string("%s.%f",(conv['currency_symbol'],conv['frac_digits'],x),grouping=True) #格式化为字符串(使用组分隔符格式化数字) currency_symbol意思为使用$开头的和发标识为站位符
```

## 模板

+ string模块包含了template类，template类就是模板
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
from string import Template
#Template函数用来创建模板，'$'表示输出后面的字符,$$表示输出$
#t.substitute方法使用的字典模式,Template关键字，t.substitute提供键值
t = Template('${village}folk send $$10 to ${cause}')
print(t.substitute(village='NOttingham',cause='the dicth fund.'))

#如果输入的键值与模板中的关键字数量不匹配，会出现keyerror错误
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow') #用dict函数输入字典

print(t.safe_substitute(d)) #使用safe_substitute忽略错误


import time,os.path
photofiles = ['img_1974,jpg','img_1976.jpg','img_1977.jpg']
class BatchReneme(Template):
    delimiter = '%' #用%代替$分开
fmt = input('Enter reneme style (%d-date %n-seqnum %f-format):') #输入模板
t = BatchReneme(fmt) #将输入的模板复制到t
date = time.strftime('%d%b%y')#时间格式
for i , filename in enumerate(photofiles): #枚举photofiles
    base , ext = os.path.splitext(filename)# 切割photofiles中的文件名
    newname = t.substitute(d=date,n=i,f=ext) #d的键值就是date，n的键值为ｉ,f的键值n为ext
    print('{0} --> {1}'.format(filename,newname))#输出旧名称和新名称

```
输出
```
NOttinghamfolk send $10 to the dicth fund.
Return the unladen swallow to $owner.
Enter reneme style (%d-date %n-seqnum %f-format):Axsle_%n%f
img_1974,jpg --> Axsle_0
img_1976.jpg --> Axsle_1.jpg
img_1977.jpg --> Axsle_2.jpg
```

## 使用二进制数据记录布局
+ struct模块提供pack()和unpack()方法用来处理可变长度二进制记录格式。
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
#暂时不懂
'''
这个例子显示了怎样在没有用zipfile模块的情况下在一个zip文件中通过循环头部信息
'''

with open('myfile.zip','rb') as f : #用open()用只读二进制格式打开,并将open命名为f
    data = f.read()  #读取数据，并赋值给data

start = 0  #初始时从０开始
for i in range(3): #显示前三个文件头信息
    start += 14  #由于H表示４字节的无符号数字,I表示２字节的无符号数字，IIIHH则有１４字节,需要每次增加１４字节
    fields = struct.unpack('<IIIHH',data[start:start+16]) #解压后的数据域增加2字节
    crc32,comp_size,uncomp_size,filename,extra_size = fields　#数据域包含的信息

    start += 16 　#解压后需要每次增加１６字节
    filename = data[start:start+filename]　#现在的数据域长度为filename
    start += filename　# 每次增加filename长度
    extra = data[start:start+extra_size] 
    print(filename,hex(crc32),comp_size,uncomp_size)

    start += extra_size + comp_size #跳过下一个头部
```

## 多线程

+ 多线程是一种分离任务的技术，将单一进程的任务分给多个线程完成，不需要依赖。
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
多线程,显示高级线程模块在后台运行，而主程序继续运行
'''

import threading , zipfile

class AsyncZip(threading.Thread): #继承threading模块的Thread方法
    def __init__(self,infile,outfile):
        threading.Thread.__init__(self) #调用threading模块Thread类的__init__()方法
        self.infile = infile #需要写进zip包的文件
        self.outfile = outfile　#文件需要输出的zip压缩包

    def run(self):
        f = zipfile.ZipFile(self.outfile,'w',zipfile.ZIP_DEFLATED)  #将zip包设置为可写状态，以便写进文件,ZIP_DEFLATED应该是压缩比吧，这是一个默认值
        f.write(self.infile) #将文件写进zip包
        f.close()　#关闭文件
        print('Finished background zip of:',self.infile) #后台程序完成

background = AsyncZip('nydata.txt','myarchive.zip')#将mydata.txt写入myarchive.zip压缩包，创建一个对象
background.start() #threading.Thread中的方法，用来开起线程
print('The main program continues to run in foreground.')

background.join() #等待后台程序完成,threading.Thread中的方法，用来加入线程
print('Main program waited until background was done.')
```

## 日志

+ logging模块提供完整的特性和灵活的日志记录系统,日志信息将会发送到一个文件或者sys.stderr
+ 错误
１、我在写完这个程序后，命名logging.py　用python3 logging.py运行，出现错误如下
```
Traceback (most recent call last):
  File "logging.py", line 3, in <module>
    import logging 
  File "/home/rack/python-tutorial-notes/chapter11_brief_tour_of_the_standard_library_Part_II/logging.py", line 9, in <module>
    logging.debug('Debugging imformation')#调试信息
AttributeError: 'module' object has no attribute 'debug'

```
解决方法：重命名文件名，因为在系统中已经有一个logging.py文件，python查询时查询出错。

２、再次运行python3 logging\_example.py程序，出现错误如下
```
Traceback (most recent call last):
  File "logging_example.py", line 3, in <module>
    import logging 
ImportError: bad magic number in 'logging': b'\x03\xf3\r\n'
```
解决方法：
```
ls -a 
会发现一个.pyc文件，删除该文件重新运行
```
+ logging
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
import logging 
#a = logging.basicConfig(level=logging.DEBUG,  
#                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
#                    datefmt='%a, %d %b %Y %H:%M:%S',  
#                    filename='/tmp/test.log',  
#                    filemode='w') 
b = logging.debug('Debugging imformation')#调试信息
c = logging.info('imformational message') #信息消息
d = logging.warning('Warning:config %s not found','server.conf') #警告信息
e = logging.error('Error occurred') #错误信息
f = logging.critical('Critical error -- shutting down') #关键性误差

#print(a)
print(b,c,d,e,f)
```
输出
```
WARNING:root:Warning:config server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

## 弱引用

+ 弱引用模块提供了用于跟踪对象，而不用创建引用。
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
弱引用
当对象不再需要，将会从弱引用表中移除
'''
import weakref , gc
class A:
    def __init__(self,value):
        self.value = value

    def __repr__(self): #用于解释器理解
        return str(self.value) #用字符串返回

a = A(10) #创建引用
d = weakref.WeakValueDictionary() #创建一个字典，对其中的值进行弱引用,对值没有更多的强引用时, 将丢弃该字典中的对应项。如果提供dict, 则将dict中的各项添加到返回的WeakValueDictionary。WeakValueDictionary的实例有两个返回弱值引用的方法：itervaluerefs()和valuerefs()。
d['primary'] = a #不创建引用
print(d['primary'])#如果引用还在，就取回对象
del a #移除引用
print(gc.collect()) #立即运行垃圾收集
print(d['primary']) #引用已经不存在，输出错误
```
输出
```
10
39
Traceback (most recent call last):
  File "weak_reference.py", line 21, in <module>
    print(d['primary']) #引用已经不存在，输出错误
  File "/usr/lib/python3.5/weakref.py", line 131, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

##使用列表工作的工具

+ array模块提供array()对象
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
from array import array 
a = array('H',[4000,10,700,22222]) #‘'H'为类型代码，表示二进制数，后面为生成的是二进制数组
b = sum(a) #将数组中数据相加
print(b)
c = a[1:2] 
print(c)
```
输出
```
26932
array('H', [10])
```
+ collections模块提供deque()对象
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
from collections import deque
d = deque(['task1','task2','task3']) #创建一个队列
d.append('task4') #增加队列元素
print('insert ',d)
print('Handing ',d.popleft()) #从队头删除
'''
starting_node = ['who','i','am','a','bou']
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
a = breadth_first_search(unsearched)
print(a)

import bisect
scores = [(100,'perl'),(200,'tcl'),(400,'lua'),(500,'python')]
bisect.insort(scores,(300,'ruby')) #将加入的元组在scores中排序
print(scores)

#基于规则链表实现的堆功能
from heapq import heapify , heappop , heappush 
data = [1,3,5,7,9,2,4,6,8,0]
heapify(data) #将列表重新排列成堆排序
heappush(data,-5) #在data中插入元素
a = [heappop(data) for i in range(3)] #取三个最小项
print(a)

'''
```
输出
```
insert  deque(['task1', 'task2', 'task3', 'task4'])
Handing  task1
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
[-5, 0, 1]
```

### 十进制浮点运算

+ 主要是金融和其他需要精确十进制表示的应用
例子，对７０%的电话收取5%的税率，在小数点和二进制浮点数上有不同结果
```
#!/usr/bin/env python
# -*-coding=utf-8-*-


#计算税率
from decimal import * #十进制浮点运算
print(round(Decimal('0.70')*Decimal('1.05'),2)) #计算后进行约数，再保留２位小数点
print(round(.70*1.05,2)) #计算后直接保留２位小数，不进行任何运算
print(Decimal('1.00')%Decimal('.10'))
print(1.00%0.10)
print(sum([Decimal('0.1')]*10)==Decimal('1.0')) #判断结果是否相等
print(sum([0.1]*10)==1.0)
getcontext().prec=36 #后面小数点数
print(Decimal(1)/Decimal(7)) 
```
输出
```
0.74
0.73
0.00
0.09999999999999995
True
False
0.142857142857142857142857142857142857
```

