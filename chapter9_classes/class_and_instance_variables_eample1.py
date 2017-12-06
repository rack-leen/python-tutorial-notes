#! /usr/bin/python3
#-*-coding-*-

'''
类和实例变量
'''

class Dog:
    kind = 'canine'  #所有dog的种类，每一只dog共同拥有的属性
    def __init__(self,name): #dog name,每条dog有不同的name
        self.name = name    #为实例绑定属性


d = Dog('Fido')  #创建一个实例，d是一条叫Fido的dog
e = Dog('Buddly') #创建另一个实例，e是一条叫Buddly的dog

print('d is a ',d.kind)
print('e is a ',e.kind)

print('d is a ',d.name)
print('e is a ',e.name)

