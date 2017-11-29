#2.1 invoking the interpreter //调用解释器
python -c command arg ... 
python -m module arg .. 
##Argument Passing  //参数传递
##interactive mode  //交互模式


#2.2 the interpreter and its environment //解释器和它的环境
##source code encoding //源代码的编码
所有的python源文件编写都需要声明编码方式（linux/unix系统下）
```
#! /usr/bin/python #源文件需要的编译环境
#-*-coding:utf-8-*-#编码方式，在这里编码为utf-8
the_word_is_beautiful = TRUE
if the_word_is_beautiful:   //if语句
  print "that's right!"
```
input : python the_word_is_beautiful.py
output :that's right!





