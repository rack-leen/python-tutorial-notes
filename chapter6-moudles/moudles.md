# moudles 模块
## more on moudles 
+ excuting moudles as scripts 将模块用作脚本执行
+ the moudles search path     模块搜索路径
+ complied python files       编译python文件
## standard moudles 标准模块
## the dir()function dir()函数
## packages 包
+ importing from a package 
+ intra-package references
+ packages in multiple directories

# moudles
_做为全局变量名 _name_的值时，模块是可用的
+ fibonacci函数
```
#!/usr/bin/env python
# coding=utf-8
'''
fibonacci函数
'''
def fib(n):
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a,b=b,a+b

#用result返回
def fib2(n):
    result = []
    a,b=0,1
    while b < n:
        result.append(b)
        a,b=b,a+b
    return result
        
```
输出
```
1 1 2 3 5 8 13 21 34 55 89 None
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
1 1 2 3 5 8 13 21 34 55 89 None
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
```
## more on moudles 
+ 一个moudle中能导入其他moudle
+ 可以导入模块中选定的函数
example

### excuting moudles as scripts 用作脚本

