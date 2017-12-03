#!/usr/bin/env python
# coding=utf-8

#!/usr/bin/env python
# coding=utf-8
'''
fibonacci数
'''
a,b = 0,1
while b < 1000 :
    print(b,end=',') #用，来分割输出数据
    a,b = b,a+b #可以分解为a = b b = a+b
