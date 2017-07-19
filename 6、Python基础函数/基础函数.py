#while 循环  和 for循环
'''
a = 0
while a < 5:
    print('aaa',a)
    a += 1
    b = 0
    while b < 5:
        #print('bbb',b)
        b += 1
        if b == 2:
            #break  #结束本次循环  只影响当前层循环
            continue   #跳过本次循环后面不运行 跳回while
        print('bbb',b)
'''
'''
#for
for i in range(5):
    print('iii',i)
    for j in range(5):
        if j == 2:
            #break   #for和while相同之作用所在层
            continue  #同while
        print('kkk',j) 
'''

#函数的优点
#x + y = 3
x = ['a','b','a',1,2,2,3]
y = ['a','3']

for i in y:
    while i in x:
        x.remove(i)

a = [1,2,3,4,4]
b = [1,2,4]
for i in b:
    while i in a:
        a.remove(i)

def fun(x,y):
    for i in y:
        while i in x:
            x.remove(i)
    return x,y

#把重复的代码放到函数中 下次要用时直接调用这个函数

#函数定义形式
'''
def function_name(param):
    block
    return 表达式/value   #表达式不能有赋值语句  += /= *=
'''

#必备参数  没有默认值  调用必须要传的参数 不然会报错
def func(x,y):
    print(x)
    print(y)
    return x  #默认不谢return返回none

#默认参数  有默认值，不传参数是返回默认值  传了则返回传入值
def func2(x,y,z=3):
    print('x->',x)
    print('y->',y)
    print('z->',z)
    return x+1
#要想改顺序必须全改  利用 参数重新赋值  或者从前往后

#不定长参数
def func3(x,y=1,*args):
    print('xx',x)
    print('yy',y)
    print(args)

#func3(1,2,a)  把a当做参数
#func3(1,2,*a)  把a当做元祖

def func4(**kwargs):  #键值对传入
    print('kwargs',kwargs)

#func4(a=1,b=2)
#a = {'a':1,'b':3}
#func4(**a)

#常见的内置函数
import keyword
keyword.kwlist

dir(__builtins__)

li = [2,8,5]
la = ['a','z','q']  #ascii码比较

len(li)  #长度
min(li)  #最小
max(li)  #最大

sorted(la)#sorted  不改变原来的  li.sort()会改变
sorted(li)

reversed(li)
reversed(la)

sum(li)  #求和
sum(li,2)  #自己写一个

#进制转换
bin(12)  #转成二进制
hex(15)  #转成16进制
oct(9)   #转成8进制

'{0:o}'.format(12)  #转8进制  x -> 16  b -> 2进制

ord('a')  #转成ASCII吗
chr(97)  #ascii 转成字符






