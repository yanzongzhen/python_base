#python基础

#集合 就和数学里面的集合一个意思  set
se = {1,2,2,'a','c'}
#{'a', 1, 2}
#无序  不重复
set('abc')
##set(['a','b',[1,2],[1,2,3]])  嵌套的列表不行  可能会出现重复，违反唯一性原则
set(['a','b',(1,2)])  #元组不可变所以可以
sa = {1,2,'a','b'}
se & sa # & 交集 集合相同的部分
se | sa  #| 并集   两个集合合起来组成一个集合
se - sa #- 差集  前面这个集合去掉后面这个集合重复的部分  保留不同的部分

se.add('f')  #add一次只能添加一个
se.update('h','d')  #一次可以添加多个
##se.remove('h')
a = set()
##se.clear()

#集合其他方法了解就行
##se & s2  #se.intersection(s2)   se.intersection_update(s2)
##s1 | s2  #se.union(s1)
##se - s2  #se.difference(s2)   se.difference_update(s2)
##
###集合方法
##se.add(1)
##
##se.isdisjoint(s1) #判断有无交集
##cose = se.copy()
##se.issubset(cose) #判断是否被包含于cose
##se.issuperset(se) #判断是否包含 se
###se.pop()
##se.symmetric_difference(s2) #返回一个对称差
##se.update(s1)
#集合基本了解就行，一般来说用不到

#字典  dict
di = {'a':1,'b':2}  #'a' 是key  1 是values {key:value}   key:value  键值对
d1 = dict(c=3)
d1.fromkeys('abc')
d1.fromkeys('abc',1)  #返回一个新的字典
di.get('a') #取value
di['a']   #字典取value
di.get('C')
di.get('c',3) #没有key  返回给定值默认是None
a,b = di.get('c',(1,2))
list(di.items())  #获得键值对
list(di.keys()) #获得key
list(di)
##di.pop('a')  #和列表用法有区别，必须要有一个key  如果没有这个key就会报错
##di.popitem() #返回键值对
di.setdefault('a') #key存在和get一样
di.setdefault('a',2)
di.setdefault('c') #key不存在就添加，然后value默认None
di.setdefault('d',4)
di.update({'a':2,'c':3,}) #更新key的值
di.update({'f':5})  #没有的时候添加进去啦
di['h'] = 8  #key存在跟新 不存在添加
di.update(d1)
list(di.values()) #返回所有的values

#字典的作用
"""
1.键不重复，集合的特性
2.键值可变  列表
3.码表 就和我们用的字典一样  其实我们python的命名空间就是用的字典去存储的
"""
'''
总结：
    可变对象：list set dict
    不可变对象： str tuple  number
'''

#运算符
1 == 1  #判断相等
1  != 2 #判断不相等  比较运算符 返回bool值

'a' in di
2 in di
2 not in di

a = 1723548901
b = a
a is b
a is not b

1 == 1 and 2 == 2  #两边都是True才返回True
1 == 1 or 2 == 3
1 == 2 or 2 == 3 #有一边为真就放回真

not 1==1  #取反



