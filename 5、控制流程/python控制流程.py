#python  控制流程

a = 3
b = 2
#if a == b:
#    print('a和b相等')
#else:
#    print('a和b不相等')

'''
if a > b:    #if可以单独出现
    print('a大')
elif a < b:
    print('b大')
#elif a == b:
else:
    pass  #要不起
print('a和b 不相等')
'''

#让程序随生成
import random
n = random.randint(1,10)

#print(n)

'''
a = input("请输入一个不大于十的数：")
#input返回为字符串
if a.isdigit():
    a = int(a)   #类型转换
    if a <= 10 and a >= 1: 
        if a > n:
            print("输入大了")
        elif a < n:
            print("输入小了")
        else:
            print("相等，您对了")
    else:
        print("输入范围不对")
else:
    print("typeerror")

'''


#循环语句
a = 0
while a < 5:  #TRUE执行  false 不执行
   # print(a)
    if a == 3:
        #print('***',a)
#        a += 1
        #break      #不是回到while  直接终止循环
#        continue  #跳过本次循环  不进行后面的运行 进入下个循环  直接到while
        a += 1
    else:
        pass
    a += 1
'''
num = 0
while num < 3:
    a = input("请输入一个不大于十的数：")
    #input返回为字符串
    num += 1
    if a.isdigit():
        pass
        a = int(a)   #类型转换
        if a <= 10 and a >= 1: 
            if a > n:
                print("输入大了")
            elif a < n:
                print("输入小了")
            else:
                print("相等，您对了")
                break
        else:
            print("输入范围不对")
    else:
        print("typeerror")
    #num += 1
else:
    print("次数用完了")

#正常结束while会执行else  如果循环被break终止  就不会执行else
'''
#range
range(10)
range(1,10)  
range(1,10,2)

#for
'''
for i in range(10):
    #print(type(i))
    print(i)
'''

for i in 'abc':   #判断是否为可迭代
    #print(i)
    pass

a = 0
'''
while a <= 100:
    if a%2 == 0:
        print(a)
        pass
    a += 1
'''

for i in range(100):
    print('**',i)
    if i % 2 == 0:
        print(i)
    
