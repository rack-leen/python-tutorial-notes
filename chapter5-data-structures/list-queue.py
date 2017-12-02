#!/usr/bin/env python
# coding=utf-8

from collections import deque   #被设计来从末尾更快速的append and pop元素
queue = deque(["Eric","Join","Michae"])
#从末尾增加元素
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)
#从队列左边退出队列
queue.popleft() 
print(queue)
queue.popleft()
print(queue)
