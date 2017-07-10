#python基本数据类型

li = [1,2,3,4,5]
#help(li.append)
li.append('a')  #L.append(object) -> None -- append object to end
                #默认增加到末尾

#li.clear()   清楚列表  删除列表内所有元素

l_2 = li.copy()
id(li)        #查看内存
id(l_2)       #新建对象

l_3 = li[:]
id(l_3)

x = li        #给列表对象多了一个引用
id(x)

li.count(1)
#li.count(value) --> integer  次数  统计value出现的次数

#iterable  可迭代   dir(a) 有__iter__为可迭代
a = 'i love python'
li.extend(a)  #将可迭代对象的每一个元素一次添加到末尾

li.index(1)  #索引  返回第一次出现的索引值
li.index(' ',7,12)  #从索引值为1开始查找 一直到12，后面区间第一次出现的位置  超出报错

li.insert(1,'a')  #在索引值指向位置加入值  index + object

li.pop()  #删除  默认删除最后一位并返回  加索引值删除索引指向值并返回 L.pop([index])
li.pop(0)

li.remove('a')  #移除 移除第一个出现匹配传入值

li.reverse()  #反转   list(reversed(li))元列表不变  要重新赋值
 
l_4 = [5,3,6,9,8]
l_4.sort()   #sort排序 只能同类型  默认是ASCII

l_5 = ['a','b','c','d','e']
l_5.sort()
l_5.append('aaa')
l_5.sort(reverse = True)  #先排序在反转

sorted(l_5)
sorted(sorted(l_5),key = len)  #key为关键字  int len str float lambda


######元祖#######  不可变即使在内存中也不可变
tu = ('a','b','c')

#count 计数
tu.count('c')

#index  索引
tu.index('a')

#####   字符串  ######
s = '人生苦短，我用python'
b = 'this is python test'

b.count('i')

b.endswith('t') #末尾判断
b.startswith('t') #开始判断

b.find('a')  #没有返回-1  
#b.index('a')  index报错

b.isalpha()  #判断是否都为字母  返回布尔型
a = 'ilovejuanjuan'
a.isalpha()  

d = '123456'
d.isdigit()  #是否为数字

b.lower()   #字母转成小写
b.upper()     #字母转成大写

b.replace('i','o')  #全部转换
b.replace('i','o',2)  #替换count个参数  次数

b.split()  #默认按照空格分割并产生新的列表
b.split('i')  #以某个元素去分割
b.split('i'，1) #1 代表分割一次

