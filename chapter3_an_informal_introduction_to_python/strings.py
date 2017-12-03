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

