#! /usr/bin/python3
#-*-coding:utf-8-*-

'''
try...except...finally语句中使用else
'''

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero.")
    else:
        print("the result is ",result)
    finally:
        print("excuting finally clause.")

print(divide(2,1))
print(divide(2,0))
print(divide("2","1"))#不能输入字
