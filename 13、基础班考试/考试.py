#python基础班 考试
'''
13-晓振-Py201706062-基础考试
'''
Q1 = '''
一、在编辑文本中，我们经常需要在文本中找到某个模式出现的位置。比如我要在文本中找到某个字符串出现的次数
    和位置，这种问题称为字符串匹配问题。我们简化为在一个字符串中找到模式出现的位置。
      如：字符串为：str1='adhvahabcabcabcfjiaohgio'
          模式为：str2='abc'
          找出str1中模式出现的位置(6,9,12)
'''
print('\n第一题解答')
str1 = 'adhvahabcabcabcfjiaohgio'
str2 = 'abc'
def getindex(substr,str):
    count = 0
    li = []
    i = str1.count(str2)
    print('先整体查询要求字符串的个数',i)
    while i > 0:
        index = str.find(substr)
        if index == -1:
            return -1
        else:
            str = str[index+1:]   #第一次出现该字符串后后面的字符
            i -= 1
            count = count + index + 1   #位置数总加起来
            co = count - 1 
            li.append(co)
    return tuple(li)
                          
testq1 = getindex(str2,str1)
print('索引位置',testq1)

Q2 = '''
二、有时，我们会需要一连串等间距的数字（这在数据分析和进度控制等方面格外有用），例如：[0, 2, 4 , 6, 8]
    对于上述例子，使用 list(range(0, 10))可以十分方便的完成。
    但是 range 的步长只能是整数，因此，加入我们需要 [0, 0.1, 0.2, ... , 0.9]，
    那么 range 就不能满足我们的需求了。
    因此，写一个类似 range 的生成器，来支持浮点数的步长。
'''
#print('\n第二题解答')
def f_range(start,end=None,step=1):
    #浮点数的步长
    #print('步长为',step)
    if isinstance(step,float):
        jingdu = len(str(step).split('.')[1])  #获取浮点数整数步长
        #print(str(step).split('.')[1])
    else:
        jingdu = 0
           
    if end == None:
        i = 0
        while i < start:
            i = round(i,jingdu)  #四舍五入
            yield i
            i += step
    else:
        i = start
        while i < end:
            i = round(i,jingdu)
            yield i
            i += step
q2_answer = list(f_range(0,1,0.1))
#print(q2_answer)


Q3 = '''
三、之前给大家演示过如何利用装饰器，测试函数的运行时间，现在要求大家做如下测试：
    现在要求，在这个装饰器的基础上，完善这个装饰器。使其：
    1. 依然可以测试函数运行的时间
    2. 依然可以将函数运行的时间输出到屏幕上
    3. 除了以上两点，还可以将运行时间，以日志的形式记录在指定的文件中（当作日志）。
    4.测试函数大家自己选取   
'''
#print('\n第三题解答')
#本次会使用到不同的 程序 要考虑日志的实用性  明确指出运行时间
#时间装饰器
li = [1,2,5,64,88,51,24,78,451,56,748,81,51,2,5]
di = {'a':1,'b':2,'c':3}
tu = (3,4,6)
import time
def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        print('函数：%s开始时间: %s'%(func.__name__,time.strftime('%x',time.localtime())))
        back = func(*args,**kwargs)
        print('函数：%s 终止时间: %s'%(func.__name__,time.strftime('%x',time.localtime())))
        times = time.time() - t0
        print('函数:%s 运行时间:%s'%(func.__name__,times))
        with open('timelog.txt','a+',encoding='utf8') as f:
            run_times = '函数:%s 运行时间为:%s'%(func.__name__,times)
            f.write(run_times+'\n'+'\n')
        return back,times
    return new_fun
@run_time
def exchange(*arg,**kwarg):
    #print("输入的元祖",arg)
    #print('输入的字典',kwarg)
    tu = list(arg)
    di = kwarg
    i = 0
    for key in di.keys():
        if i < len(tu):  
            tu[i],di[key] = di[key],tu[i]
        i += 1
    return tuple(tu),di
@run_time
def bubble_sort(li):
    for i in range(len(li)):    
        for j in range(0,len(li) - i - 1):  
            if li[j] > li[j+1]:   
                li[j],li[j+1] = li[j+1],li[j]  
    return li

#测试
#exchange(*tu,**di)
#bubble_sort(li)

Q4 = '''
四、字符串里面的count可以统计字符出现的次数，现在要求大家定义这样的一个类，
这个类里有一个方法可以统计字符串里的所有的字符出现的次数，并作为一个字典返回，
同时这个类还有字符串的所有方法。
'''
#print('\n第四题解答')
class StrExtend(str):  #继承字符串类
    def __init__(self,st):
        if isinstance(st,str): 
            self.st = st
        else:
            raise TypeError
    #定义取值函数
    def getcount(self):
        di = {}
        for i in range(len(self.st)):
            #print(i)
            di.setdefault(self.st[i],self.st.count(self.st[i])) 
        return di
st1 = 'ababababasndndndndmfm'           
a = StrExtend(st1)       
b = a.getcount()       
#print('测试字符串%s\n测试结果%s'%(st1,b))
