#python基础

#1、字符串匹配

#朴素字符串匹配法  (n-m-1)m
t = 'adhvahabcabcabcfjiaohgioabc'
p = 'abc'

def naive_string_matcher(T,P):
    n = len(T)#文本长度
    m = len(P)#模式长度
    li = []
    for i in range(n-m+1):
        if P == T[i:i+m]:
            li.append(i)
    return tuple(li)
#用字符串
def find_str(T,P):
    li = []
    star = 0
    for i in range(T.count(P)):     #出现几次循环几次
        li.append(T.find(P,star))
        star = T.index(P,star) + len(P)  #加长度合理
    return li
#正则

#2、range_float
def f_range(start,end=None,step=1):
    #浮点数的步长
    #print('步长为',step)
    if isinstance(start,float) and isinstance(end,float):
        pass
    else:
        raise TypeError
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


#4
class CustomStr(str):
    def times(self):
        di = {}
        for i in set(self):  #去掉重复字符  减少循环次数
            di[i] = self.count(i)  #字典最常用
        return di
