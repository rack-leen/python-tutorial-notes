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

