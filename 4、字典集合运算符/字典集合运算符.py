#20170714 Python基础


'''
集合
字典
运算符优先级
'''
#集合 和数学里的集合一致
#特点：无序 不重复

se = {1,2,2,'a'}
#{1, 2, 'a'}

set('abs')
set([1,2,3])
set((1,2,3))
#set(['a','c',[1,2],[1,2,3]])
#嵌套的列(列表可变)不可以set 可能会出现相同元素
set(['a','b',(1,2)])
#嵌套元祖  可以的  元祖不可变

#集合运算 & | -

sa = {1,2,'a','b'}

s1 = se & sa #交集{'a', 1, 2}
s2 = se | sa #并集{'a', 1, 2, 'b'}
s3 = sa - se #差集{'b'}
s3 = se - sa #set()  去掉被减集合中 同减集合的相同的

#集合方法
'''
s.add  添加一个
s.update   添加多个
s.remove   移除
s.clear 清空
'''
se.add(3)
se.update('f','c')
se.remove('f')
#se.clear()

#字典

di = {'a':1,'b':2}  #'a'为key  ’1‘为value {key:value}  键值对
d1 = dict(abc = 1)
d2 = dict(abc = 1,cde = 2)

d1.fromkeys('abc',1) # 产生新的字典

di.get('a')          #取value值 1
di['a']             #2
di.get('C')         # 没有key  就返回默认的  默认为none
di.get('C',3)       # 没有  就返回自己赋值
a,b = di.get('ab',(1,2))

di.items()          #把字典转换为键值对元祖列表
list(di.items())    #[('a', 1), ('b', 2)]

di.keys()          #获得键
list(di.keys())
list(di)

#di.pop('a')     #和列表有区别必须指定key  如果没有k报错
#di.pop('c',3)

#di.popitem()     #删除最后的键值对

#添加一
di.setdefault('c',2)  #如果值存在就返回  如果不存在就添加
#添加二
di.update({'a':2,'c':5})  #如果原来有就更新值
di.update({'w':6})      #没有就添加进去
#添加三
di['h'] = 8           #key存在更新  不存在添加

di.values()   #返回所有的values

#字典特点
'''
键值唯一
无序
'''
#字典的作用
'''
1、键不重复  集合的特性
2、键值可变 列表
3、码表 和我们用的字典一样
'''

#############
'''
总结
不可变：int float bool complex str tuple
可变 ：字典  集合  列表
'''
#############
#运算符优先级

#比较运算符返回布尔型值
1 == 1  #判断相等
1 != 2  #判断不相等
2 > 1   
1 < 2   
1 >= 1
1 <= 1

#成员运算符
li = [1,2]
1 in li
2 not in li

'a' in di
'2' not in di

#身份运算符
a = 1
b = a
c = 2
a is b
a is not c

#逻辑运算符
'''
and  同真为真
or   一真为真
not 取反
'''
1 == 1 and 2 == 2
1 == 2 or 2 == 2
not 1 == 1

