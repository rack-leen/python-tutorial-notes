#!/usr/bin/env python
# coding=utf-8
#example1
a = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y] 
print(a) #生成以元组为子集的列表

#example2

combs = [] #构建空列表

for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
           combs.append((x,y))

print(combs)

