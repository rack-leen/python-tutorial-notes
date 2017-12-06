#!/usr/bin/env python3
# coding=utf-8

def scope_test():
    def do_local():
        spam = "local spam" #局部名称

    def do_nonlocal():
        nonlocal spam 
        spam = "nonlocal spam" #nonlocal名称

    def do_global(): #nonlocal改变局部名称后，现在的局部名称为spam="nonlocal"
        global spam
        spam = "global spam" #局部名称

    spam = "test spam" #为全局名称
    
    do_local()
    print("After local assignment:",spam) #输出的是test spam，因为局部名称不能修改全局名称，所以输出的是全局名称的值
    do_nonlocal()
    print("After nonlocal assignment:" , spam) #输出的是nonlocal spam,因为nonlocal可以改变spam绑定的名称
    do_global()
    print("After global assignment:",spam)#输出的还是nonlocal，因为global绑定为全款名称，改变global定义的spam实际上为全局名称spam="test spam"

scope_test()
print("in global scope:",spam) #输出的是global，因为全局名称绑定被global改变了，改变为global所在函数的spam

