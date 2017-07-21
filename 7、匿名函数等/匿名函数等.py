#内置函数补充

#1、enumerate  #返回一个枚举对象
li = ['a','b','c','d']
enumerate(li)
list(enumerate(li))
dict(enumerate(li))


#2 eval() #1取出字符串
#将字符串str当做有效的表达式  来求值  并返回结果
a = "{'a':1}"
b = '1+2+3'
eval(a)
eval(b)

#3 exec()  执行字符串或者compile方法编译过的字符串，没有字符串
s = '''
z = 10
su = x + y + z
print(su)
print('OK')
'''

x = 1
y = 2
exec(s)
exec(s,{'x':0,'y':1})
exec(s,{'x':0,'y':1},{'y':10,'z':30})  #以字符串为主  以最后的为主


#4、filter 过滤器

def test1(x):
    return x > 10
l1 = [10,2,20,13,15,5]
filter(test1,l1)
list(filter(test1,l1))  #返回大于10的元素

#5、map函数  将可迭代对象一次传给function
l2 = [1,2,3]
map(str,l2)
list(map(str,l2))

#zip 将对象逐一配对
l3 = [1,2,3]
t1 = ('a','b','c')
zip(t1,l3)
list(zip(t1,l3))


#匿名函数
def fun1(x):
    x = x + 1
    return x
def fun2(x):
    return x + 1

g = lambda x:x+1
g(3)

list(filter(lambda x:x>10,l1))


#内置函数作用域

def fun():  #外面不能访问函数里面的变量
    xx = 1
    return xx

x = 1
if x > 0:
    yyy = 1
else:
    print('no')

a = 12
def fun2():  #函数里面可以访问外面参数
    print(a)
    return a + 1

a = 12
def fun3():  #函数里面不能修改外面的变量 可以调用
    a = a + 1
    return a

a = 12
def fun4():  #内部调用利用global
    global a
    a = a + 1
    return a

a = 23
def fun5():
    global a
    a += 1
    global b  #函数里面的变量在外面可以访问的话  要用global
    b = 9
    print(a,b)

'''
在上面函数外面的变量的作用于就是全局  函数内部变量作用域就是局部
作用为全局的称谓全局变量  作用域为局部称谓局部变量
'''
#内嵌函数
def fun6():
    print('fun6在被调用')
    b = 10
    def fun6_2():
        nonlocal b  #nonlocal 用于在函数内可以修改外层的变量
        b = b +  1 # 作用到当前函数 不能修改相对外部变量
        print(b)
        print('内部被调用用')
    fun6_2()    #返回fun6_2的运行结果

def fun8():  #闭包
    print('fun9() is running')
    def fun10():
        print('fun10() is running')
    return fun10  #返回fun10()函数对象

#递归函数
def factorial(n):  #阶乘  n!  
    if n == 1:
        return 1
    return factorial(n-1)*n

#回调函数
'''
from tkinter import *
root = Tk()
root.geometry('400x400+300+100')

def clik():
    print('哈哈哈')

Button(root,text='push',command=clik,bg='red').pack(fill=X,expand=1)
root.mainloop()
'''
