# virtual environments and packages 虚拟环境和包

## introduction 介绍
## creating virtual environments 创建虚拟环境
## managing packages with pip 用pip包管理器


## introduction 介绍

python程序经常使用没有包含在标准库中的包和模块,程序有时需要特定版本的库，因此有些程序需要的版本不同，这将会产生版本冲突。
解决办法：创建一个虚拟环境，一个自己的目录树容器，包含一个python程序安装需要的详细的python版本以及附加的包.
不同的程序需要用不同的虚拟环境，用来解决冲突。


## creating virtual environments 创建虚拟环境
venv模块是用来创建和管理虚拟环境的，通常将会安装大多数你需要的最近的python版本。如果在你的系统有许多python版本，你能选择一个特定的你想要运行的python版本。
创建一个虚拟环境，选择自己要放置的目录，并且用带有目录路径的脚本运行venv模块：
```
python3 -m venv tutorial-env #如果目录不存在，将会创建一个tutorial-env，也能在其中创建目录，其中包含python解释器的副本，标准库和各种支持文件。
```
创建好有个虚拟环境后，需要激活它。
在windows上，运行：
```
tutorial-env\Scripts\active.bat
```
在linux/Unix上，运行：
```
source tutorial-env/bin/active
```
改变虚拟环境:
```
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
```

## managing packages with pip 用pip包管理器

```
pip search astronomy #搜索python包
pip install packages #安装包
pip install requests=2.6.0 #安装指定版本包
pip install --upgrade requests #更新包版本
pip show requests  #显示包信息
pip list #显示所有的安装在虚拟环境中的包
pip freeze > requests.txt 　#将会产生一个被安装包的列表，但是使用pip期望的格式输出
pip install -r requests.txt requests.txt将会提交到版本控制，并作为程序的一部分，用户能够用-r安装所有需要的包
```
