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

