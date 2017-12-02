#!/usr/bin/env python
# coding=utf-8
'''
嵌套列表生成式
'''
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],] #每个子集后面要加逗号
a = [[row[i] for row in matrix] for i in range(4)]
print(a)

#等价于
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

#等价于
transposed = [] #初始化
for i in range(4):
    transposed_row=[]  
    for row in matrix: #行初始化
        transposed_row.append(row[i])#往列表第row个元素的第i个位置增加元素
    transposed.append(transposed_row) #往列表的第i个位置增加元素
print(transposed)

#相似
e = list(zip(*matrix))
print(e)
