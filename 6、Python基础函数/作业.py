#作业 13-燕宗振-Py201706062

#第一题  课堂代码自己敲一遍

#第二题
Q2 = '''
二题：找到1-100内的质数，用while和for来做，结束之后打印“搜索结束”
'''
'''
print(Q2)

#for
print('for循环')
for i in range(2,101):
    fg = 0
    for j in range(2,i-1):
        if i%j == 0:
            fg = 1
            break
    if fg == 0:
        print (i,end = ' ')
else:
    print('\n搜索结束')
    

#while
print('while循环')
a = 2
while a <= 100:
    n = 0
    b = 2
    while b <= a-1:
        if a % b == 0:
            n = 1
            break
        b += 1
    if n == 0:
        print(a,end = ' ')
    a += 1
else:
    print("\n搜索结束")


'''
'''
题目三
Q3 = '''
##题目三：定义包含各种参数形式的函数，并调用
'''
print(Q3)

def fun_all(x,y=1,*arg,**kwarg):
    print('this is x:',x)
    print('this is y:',y)
    print('this is args:',arg)
    print('this is kwargs:',kwarg)
    return x,y,arg,kwarg

a = (1,2,3,4,5)
b = {'w':2,'x':3}

print('默认顺序添加',fun_all(1,2,a,b))

print('指定添加',fun_all(1,2,*a,b))

print('多位置指定添加',fun_all(1,2,*a,b=4))

print('字典类型添加',fun_all(1,2,3,b=4))

'''
#题目四
Q4 = '''
题目四：定义一个函数，能够输入字典和元组。函数返回一个字典和元组，字典的值和元组的值交换
'''
print(Q4)

def fun_ex(*arg,**kwarg):
    d1 = {}
    li = list(arg)
    print('原元组：',arg)
    print('原字典：',kwarg)
    for i in range(len(li)):
        #print(i)
        for j in range(len(kwarg)):
            if i == j:
                li[i] = list(kwarg.values())[j]
                d1[list(kwarg.keys())[j]] = arg[i]
            elif i < j:
                d1[list(kwarg.keys())[j]] = list(kwarg.values())[j]
            elif i > j:
                li[i] = li[i]
    print('交换后：',tuple(li))
    print('交换后：',d1)

di = {'a':1,'b':2,'c':3}
tu = (3,4,6)
d2 = {'a':1,'b':2,'c':3,'d':4}
t2 = (8,9,10,11,12)

print('元组和字典长度相同')
f = fun_ex(*tu,**di)
print('\n字典比元组长度长')
e = fun_ex(*tu,**d2)
print('\n元组比字典长度长')
h = fun_ex(*t2,**di)    
    
#讲解

di = {'a':1,'b':2,'c':3}
tu = (3,4,6)

def exchange(*arg,**kwarg):
    print("输入的元祖",arg)
    print('输入的字典',kwarg)
    tu = list(arg)
    di = kwarg
    i = 0
    for key in di.keys(): #不需要管字典的长度超出范围
        if i < len(tu):  #保证元祖不会超出索引范围  
            tu[i],di[key] = di[key],tu[i]
        i += 1
    return tuple(tu),di

'''
元祖不可变  转成列表  list(arg)
step2:通过key改字典的值
step3:怎么一次获得key for key in di.keys():
step4:  怎么交换  tu[i],di[key] = di[key],tu[i]

#长度不等时：
保证元祖不会超出索引范围
if i < len(tu)
字典的长度超出范(不会超出key数量)
for key in di.keys():
'''
