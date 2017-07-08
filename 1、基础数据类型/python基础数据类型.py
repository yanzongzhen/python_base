#python 基础数据类型
a = 1 + 2
#print(1+2)

#编辑器里面返回值不会被打印，想打印要加print
#print 是什么？紫色--内置函数  橙色---关键字

dir(__builtins__)#列出内置函数方式

#整形
a = 1 + 2
type(a) #int代表整形  Python2 long

#浮点数
b = 3.3
type(b)# float代表浮点型  

#布尔型  bool
c = True  #真
type(c)
d = False #假
type(d)

#关键字
import keyword  #关键字模块
for i in keyword.kwlist:  #不要用关键字为变量名
    pass
    #print(i)

#变量命名规则
'''
字母、数字和下划线组成
只能为字母和下划线开头不能为数字开头
'''
'''
SyntaxError  语法错误  异常就是报错
'''
#复数 complex
e = 1 + 2j
type(e)

'''
数字类型
整形 int
浮点型 float
布尔  bool
复数 complex
'''
#type查看对象类型

#数字运算  加减乘除
# + - * /  //(整除)  %（取余） **（幂运算）
a + b
a - b
a * b
a / b #python2中  1/2 = 0   python3中  1/2 = 0.5
a//b  #向下整除

#3.0 < 3.3 < 4.0
#向下取整 3.0
#向上取整 4.0
'''
向上取整方式
import math
math.ceil(b/a)
int((b+a-1)/a)
'''
#取余
105%10
100%10
100/10
105/10

#**
3**2 








