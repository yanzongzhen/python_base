# python基础
'''
1、迭代器和生成器
2、模块和包
'''
#迭代器iterator
li = [1,2]
dir(li)#查看__iter__方法  如果有就是可迭代对象
a = li.__iter__()  #调用这个方法返回一个迭代器
next(a)  #去迭代器的值  取完后返回 停止位异常

li = []
for i in range(10):
    li.append(i)

#列表推导  #列表解析
l2 = [i for i in range(10)]
l3 = [i for i in range(10) if i%3 == 0]

'''
列表推到是从外部存到列表中 迭代器是从容器取出值
'''
l2 = l2.__iter__() #得到一个迭代器
next(l2)  #迭代取值

l3 = iter(l2)
l3.__next__()

#生成器 generator
def fun(n):
    i = 0
    while i < n:
        print('start',i)
        yield i  #运行到此函数返回一下  生成器关键字
        i += 1
        print('end',i)
        
#b = fun(5)
#b.__next__() #利用list()显示全部
#函数里面放了yield之后函数就是生成器

#生成器作用
def fab(maxs):
    n,a,b = 0,0,1
    while n < maxs:
        print(b)
        a,b = b,a+b
        n = n + 1
#不用占用太大空间  需要就生成
def fab1(maxs):
    n,a,b = 0,0,1
    while n < maxs:
        yield b
        a,b = b,a+b
        n = n + 1

c = fab1(1000)
next(c)

#yield 只能依次去取不能从中间取  也不能回头
'''
在文件读取时候  利用生成器去读 就不会占用太大的内存空间
'''
f = open('test.txt','r',encoding='utf8')
def getfile():
    a = 'aa'
    while a != '':
        a = f.readline()
        yield a
f.close

#模块和包
import keyword
keyword.kwlist

'''
通过查看安装路径下的lib文件夹中的keyword.py文件  模块就是一个py文件  lib中为内置模块
'''
#导入模块
#import  #导入方法
from keyword import kwlist as kw
#从keyword模块中导入kwlist这个变量娶个别名kw

#这里这个模块和kw没有关系  相当于生命了一个变量kw，这个变量的值为这个列表

'''
from的作用
如果模块很大的话  可以节省时间
程序导入模块也是需要时间和空间 (导入可以在函数中导入  节省时间)
'''
#在同一个路径下
#import test
#test.test()

'''
python模快导入时会生产__pycache__文件夹  python2中出现 __init__.py
'''

#在不同的目录下面呢
import os,sys #内置模块
path = r'/Users/yanzongzhen/python_base'  #其他路径
sys.path.append(path)
import test2
#test2.test2()
  
#包管理
import xml
import xml.dom

#模块和包两则的导入类似的 只不过包时很多模块放在一起
import mod
import mod.packet as md
md.mod

#os  sys
os.getcwd()  #获得py文件的当前系统中的目录
#os.mkdir('work')  #创建新的目录
#os.rmdir('work')  #删除目录
os.listdir()  #列出当前目录下的文件   可加path

import shutil
#shutil.copyfile('work/test.txt','work1/test.txt')  #复制

def fun(z):
    print(z)
    
if __name__ == '__main__':
    print('开始')
    print(sys.argv)
#    fun(sys.argv[1])   #一定要记住这个东西 在测试终端的时候 

#cmd  python3 迭代生成模块包.py 20170107 20170730 --》['迭代生成模块包.py', '20170107', '20170730']

import time
time.time()
time.localtime()
time.asctime(time.localtime())
