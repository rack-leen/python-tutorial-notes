#!/usr/bin/env python
# -*-coding=utf-8-*-
from collections import deque
d = deque(['task1','task2','task3']) #创建一个队列
d.append('task4') #增加队列元素
print('insert ',d)
print('Handing ',d.popleft()) #从队头删除
'''
starting_node = ['who','i','am','a','bou']
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
a = breadth_first_search(unsearched)
print(a)
'''

import bisect
scores = [(100,'perl'),(200,'tcl'),(400,'lua'),(500,'python')]
bisect.insort(scores,(300,'ruby')) #将加入的元组在scores中排序
print(scores)

#基于规则链表实现的堆功能
from heapq import heapify , heappop , heappush 
data = [1,3,5,7,9,2,4,6,8,0]
heapify(data) #将列表重新排列成堆排序
heappush(data,-5) #在data中插入元素
a = [heappop(data) for i in range(3)] #取三个最小项
print(a)
