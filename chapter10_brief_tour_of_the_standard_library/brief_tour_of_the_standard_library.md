# brief tour 0f the standard library 标准库的简单介绍
## operation system interface 操作系统接口
## file wildcards 文件通配符
## command line argument 命令行参数
## error output redirection and program temination 错误输出重定向和程序终止
## string pattern matching 字符串模式匹配
## mathematics 数学运算
## internet access 互联网接入
## dates and times 日期和时间
## data compression 数据压缩
## performance measurement 性能测量
## quality control 质量控制
## batteries included 



## operation system interface 操作系统接口
```
#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
操作系统接口
'''
import os

print(os.getcwd()) #返回现在的工作目录
#指定工作目录，在工作目录下创建文件夹
print(os.chdir('/home/rack/')) #改变现在的工作目录
print(os.system('mkdir day')) #在操作系统shell中运行命令

print(dir(os)) #显示os下的属性和方法
print(help(os)) #返回os的帮助页面

#shutil模块
import shutil
shutil.copyfile('1','archive') #将1文件复制为archive文件
shutil.move('/home/rack/moo/','installer') #将moo移动到installer(相当于重命名)
```

## file wildcards 文件通配符
+ glob模块提供了从目录通配符中搜索中制作文件列表的功能
```
import glob
glob.glob("*.py")
```
## command line argument 命令行参数
+ 命令行参数存储在sys的argv属性的列表中
```
import sys
print(sys.argv)
```

## error output redirection and program temination
+ 打印输出错误提示
```
import sys
sys.stderr.write("warning,log file not found!") 
```
+ sys.exit()提供程序中断功能

## string pattern matching 字符串模式匹配
```
import re
re.findall(r'\bf[a-z]*','which foot or hand fell fastest') #用f匹配foot与hand， '*'为匹配[a-z]中所有字符 'r'表示字符串,'\b'表示退格
re.sub(r'(\b[a-z]*) \l',r'\l','cat in the hat') #
'tea for too'.replase('too','two') #用two代替too
```

## mathematics 数学运算
```
import math
math.cos(math.pi/4) 
math.log(1024,2) 

import random
random.choice(['apple','pear','banana']) #在其中随机选择
random.sample(range(100),10) #不重复抽样
random.random() #随机浮点数
random.randrange(6) #在range(6)中随机选择整数

import statistics #计算数字数据中的基本统计属性(mean(平均值)，median(中位数),vanriance(方差))
statistics.mean(data) #平均值
statistics.median(data) #中位数
statistics.variance(data) #方差
```

## internet access 互联网接入

+ urilib.repuest(从url中检索数据),smtplib(发送邮件)

```
#!/usr/bin/env python
# -*-coding=utf-8-*-

from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response: #将url命名为response
    for line in response:#在response中检索数据
        line = line.decode('utf-8') #将二进制文件解码为文本
        if 'EST' in line or 'EDT' in line: #寻找西方时间
            print(line) #打印时间


import smtplib #发送邮件
server = smtplib.SMTP('localhost') #SMTP是邮件协议
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
     From: soothsayer@example.org

    Beware the Ides of March.
 """) #从第一个地址到第二个地址
server.quit() #退出
```

## dates and times 日期和时间
```
#! /usr/bin/python3
# -*-coding=utf-8-*-
from datetime import date
now = date.today()
print(now)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.") #输出日期格式

birthday = date(1964,7,31)
age = now - birthday
print(age.days) #输出年龄，以秒输出
```
输出
```
2017-12-07
19487
```

## data compression 数据压缩

```
#!/usr/bin/env python
# -*-coding=utf-8-*-
import zlib
s = b'witch which has which witches wrist watch' #字节文件
len(s) #查看字节长度
t = zlib.compress(s) #将s压缩
len(t) #再次查看长度
zlib.decompress(t) #将压缩文件解压
zlib.crc32(s) #校验文件

```

## performance measurement 性能测量

```
from timeit import Timer
Timer('t=a;a=b;b=t','a=1;b=2').timeit()
Timer('a,b=b,a','a=1;b=2').timeit()
#检测两个语句的消耗时间
```

## quality control 质量控制

+ 质量测试 doctest
```
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)
import doctest 
doctest.testmod() $自动验证嵌入测试
```
+ unittest 允许在单独文件中维护更全面的测试
```
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all TestStatisticalFunctions
```

## batteries included

Python has a “batteries included” philosophy. This is best seen through the sophisticated and robust capabilities of its larger packages. For example:

    The xmlrpc.client and xmlrpc.server modules make implementing remote procedure calls into an almost trivial task. Despite the modules names, no direct knowledge or handling of XML is needed.
    The email package is a library for managing email messages, including MIME and other RFC 2822-based message documents. Unlike smtplib and poplib which actually send and receive messages, the email package has a complete toolset for building or decoding complex message structures (including attachments) and for implementing internet encoding and header protocols.
    The json package provides robust support for parsing this popular data interchange format. The csv module supports direct reading and writing of files in Comma-Separated Value format, commonly supported by databases and spreadsheets. XML processing is supported by the xml.etree.ElementTree, xml.dom and xml.sax packages. Together, these modules and packages greatly simplify data interchange between Python applications and other tools.
    The sqlite3 module is a wrapper for the SQLite database library, providing a persistent database that can be updated and accessed using slightly nonstandard SQL syntax.
    Internationalization is supported by a number of modules including gettext, locale, and the codecs package.
