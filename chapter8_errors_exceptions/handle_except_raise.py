#!/usr/bin/env python
# coding=utf-8

#实例化参数，在添加到异常中
try :
    raise Execption('spam','rggs')
except Execption as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x,y=inst.args
    print('x = ',x)
    print('y = ',y)
