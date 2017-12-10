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



