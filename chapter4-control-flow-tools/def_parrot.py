#!/usr/bin/env python
# coding=utf-8
def parrot(voltage,state = 'a stiff',action = 'voom',type = 'Norwegian Blue'):
    print('--this parrot wouldn\'t',action,end='') #用空格分开
    print("if you put",voltage,"volts though it.") 
    print("--lovely plumage , the ",type )
    print("it's",state , "!")

#实例1
print(parrot(1000)) #voltage值为1000，其他使用默认变量
#实例2
print(parrot(voltage=1000))
#实例3
print(parrot(voltage=10000000,action='VOOOOOM'))#输出输入的值
#实例4
print(parrot(action='VOOOOOM',voltage=100000))
#实例5
print(parrot('a million','bereft of left', 'jump'))#这三个数据填在parrot的前三个参数位
#实例6
parrot('a thousand', state='pushing up the daisies')#将数据一次填入参数位（指定参数除外）

