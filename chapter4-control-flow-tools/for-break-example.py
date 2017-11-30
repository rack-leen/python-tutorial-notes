#!/usr/bin/env python
# coding=utf-8
for n in range(2,10): #从2到10
    for x in range(2,n):#从2到n  双重循环
        if n % x == 0 :
            print(n,'equals',x,'*',n//x)
            break  #停止循环
        else:
            print(n,'is a prime number')

for num in range(2,10): 
    if(num % 2 == 0): #求余
        print("found an even number",num)
        continue #继续循环
    print("found a number",num)

