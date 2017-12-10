#!/usr/bin/env python
# -*-coding=utf-8-*-
'''
多线程,显示高级线程模块在后台运行，而主程序继续运行
'''

import threading , zipfile

class AsyncZip(threading.Thread): #继承threading模块的Thread方法
    def __init__(self,infile,outfile):
        threading.Thread.__init__(self) #调用threading模块Thread类的__init__()方法
        self.infile = infile #需要写进zip包的文件
        self.outfile = outfile　#文件需要输出的zip压缩包

    def run(self):
        f = zipfile.ZipFile(self.outfile,'w',zipfile.ZIP_DEFLATED)  #将zip包设置为可写状态，以便写进文件,ZIP_DEFLATED应该是压缩比吧，这是一个默认值
        f.write(self.infile) #将文件写进zip包
        f.close()　#关闭文件
        print('Finished background zip of:',self.infile) #后台程序完成

background = AsyncZip('nydata.txt','myarchive.zip')#将mydata.txt写入myarchive.zip压缩包，创建一个对象
background.start() #threading.Thread中的方法，用来开起线程
print('The main program continues to run in foreground.')

background.join() #等待后台程序完成,threading.Thread中的方法，用来加入线程
print('Main program waited until background was done.')
