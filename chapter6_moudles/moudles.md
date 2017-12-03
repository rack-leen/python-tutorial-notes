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
+ 在交互式回话中，如果模块被改变，需要restart解释器
+ 也可以用importlib.reload(moudlename)重新加载模块
example
```
#!/usr/bin/env python
# coding=utf-8
#用这个形式导入模块中的函数，不需要写模块前缀
from moudle_fibonacci import fib,fib2
print(fib(100)) #只需要用模块中的函数，与引用在一个文件的中函数一样
print(fib2(1000))

#导入模块中所有的函数，这种方法一般来说是不被使用的，只是可以用于交互式解释器
from moudle_fibonacci import *
print(fib(800))
print(fib2(1000))
```
输出
```
1 1 2 3 5 8 13 21 34 55 89 None
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 None
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
```
### excuting moudles as scripts 用作脚本
+ 需要在模块文件最后加上_name_语句
+ if _name_="_main_" 表示用作脚本
+ if _name_="name.py" 表示用作模块导入
example
```
#!/usr/bin/env python
# coding=utf-8
'''
fibonacci函数,用作脚本，不能被导入
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
 
#用name语句,使得模块用作脚本，不能被导入
if __name__ == "__main__":
    import sys  
    fib(int(sys.argv[1])) #python3 moudle_fibonacci_script.py arguments
```
#python3 moudle_fibonacci_script.py 100
```
1 1 2 3 5 8 13 21 34 55 89 
```

### the moudle search path
+ 模块搜索路径
搜索模块名
搜索模块所在文件名
使用sys.path搜索
1.程序主目录
2.PYTHONPATH环境变量配置目录
3.标准库目录
4..pth文件目录

### compiled python files
+ 编译后的python文件
pyc文件： .pyc 是一种二进制文件，是由 .py 文件经过编译后，生成一种byte code文件。 .py 文件变成 .pyc 文件后，加载的速度有所提高，而且 .pyc 是一种跨平台的字节码，是由python的虚拟机来执行的，这个类似于JAVA或者.NET的虚拟机的概念。 .pyc 的内容是跟python的版本相关的，不同版本编译后的 .pyc 文件是不同的，2.5编译的 .pyc 文件对于2.4版本的python是无法执行的。
pyo文件： .pyo 是优化编译后的程序  python -O 源文件 即可将源程序编译为 .pyo 文件。
pyd文件： .pyd 是python的动态链接库。

## standard moudles 标准库模块
+ sys模块
+ 在交互模式中这两个才定义 sys.ps1 sys.ps2
+ sys.path 文件路径
```
#!/usr/bin/env python
# coding=utf-8
import sys
sys.path.append('/usr/bin/vim.basic')

print(sys.path) #将输入的路径加入sys.path搜索的路径
```
输出
```
['/home/rac/python-tutorial-notes/chapter6-moudles', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/dist-packages', '/usr/local/lib/python3.5/dist-packages/bypy-1.0.3-py3.5.egg', '/usr/lib/python3/dist-packages', '/usr/bin/vim.basic']
```

## the dir()function
+ dir()函数，用来查询python模块中的函数
example
```
#!/usr/bin/env python
# coding=utf-8
import moudle_fibonacci , sys #导入两个模块

print("please output moudle_fibonacci functions:\n")
print(dir(moudle_fibonacci))
print("\n\n\n")
print("please output sys fuctions:\n")
print(dir(sys))
```
输出
```
please output moudle_fibonacci functions:
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']

please output sys fuctions:

['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe', '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']
```

example1
```
#!/usr/bin/env python
# coding=utf-8
a = [1,2,3,4,5] #a做为一个全局变量加入了dir搜索中
import moudle_fibonacci
fib = moudle_fibonacci.fib
print(dir())
#列出的所有类型名有变量，模块，函数

#dir列出内置函数和变量的名称
import builtins
print(dir(builtins))
```
输出
```
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'fib', 'moudle_fibonacci']
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

## packages 包
+ 包必须有\_\_init\_\_.py文件，它用来确定文件目录为包,避免包名被认为是一个字符串.
+ 例如,有一个包（有\_\_init\_\_.py文件），包下面有三个子目录（都有\_\_init\_\_.py文件，是sound包的子包）
```
sound/                          Top-level package(主包)
      __init__.py               Initialize the sound package(确定sound目录是python包) 
      formats/                  Subpackage for file format conversions(sound包的子包)
              __init__.py           确定formats是包
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
```
### 导入方法
+ import sound.effects.echo   隐式导入（导入sound包中的effects子包中的echo模块） 

sound.effects.echo.function() 加载子模块需要引用全名

+ from sound.effects import echo 绝对导入（从包中导入模块）

echo.function()              只需要引用模块名，不需要引用全名

+ from sound.effects.echo import function  绝对导入（从包中模块导入函数）

function()                只需要引用函数名



## importing * from a package 从一个包中导入所有模块
+ \_\_init\_\_.py中的\_\_all\_\_函数决定应该导入的模块

example,引用sound包，其中的sound/effects/\_\_init\_\_.py文件
```
__init__.py

if __name__ ='__main__'

all =["echo","surround","reverse"]  

from sound,effects import *           只导入__ all__ 中的三个模块,__all__ 只影响这种导入模式
```
### intra-package references 
+ relative import 显示导入

from . import moudlename    显示导入（导入同一目录下的模块）

from .. import moudlename

from ..package import moudlename

+ 用于python程序的主模块的模块必须用绝对导入（主模块中有“"\_\_main\_\_"）

### packages in multiple directories
+ 使用不同目录下的包，需要使用sys.path添加包目录到当前路径
```
import sys
sys.path.append("引用模块的地址")
from moudlename import fucntion or import moudlename
```


# conclusion

## 模块导入方法
+ 显示导入

from . import moudlename

+ 隐式导入

import moudlename

+ 绝对导入

from moudlename/package path import moudlename/function
