#!/usr/bin/env python3
# coding=utf-8
def concat(*args,sep="/"):#可变参数和默认参数
    return sep.join(args)
#实例
print(concat("earth","mars","venus"))#只为可变参数赋值
print(concat("earth","mars","venus",sep=".")) #可变参数和默认参数
