#2017、07、14 第四次作业

#提交人：13-晓振-Py201706062
'''
#第一题
Q1 = '''
#题1:有两个列表 x = [1,2,3,'a','b','c']  y = ['a','b','c']找出x列表中在y 中也有的元素
'''
print(Q1)
x = [1,2,3,'a','b','c']
y = ['a','b','c']
#将列表转换成集合
x1 = set(x)
y1 = set(y)
#列出两个相同部分
A1 = list(x1 & y1)
print("x列表中在y 中也有的元素:",A1)


#第二题
Q2 = '''
#题2：新建一个字典，往字典里面插入两个值；访问这个字典的所有key和values
'''
print(Q2)

di_new = {'model':1688,'phone':'iphone'}
print('添加前的字典为:',di_new)
#方式一
di_new['cpu'] = 'i7-7900k'
#方式二
di_new.update({'screen':'5.6寸'})
#方式三
di_new.setdefault('memory','6gb')
print('三种方式插入后的字典为：',di_new,'\n')

#列出所有的key
print('利用keys方法进行获取key:',list(di_new.keys()),'\n')

#列出所有的values
print('利用values方法获取所有的value:',list(di_new.values()),'\n')
'''
#第三题
Q3 = '''
题三：创建一个字典基本数据类型组合使用（创建一个字典，字典中要包含列表，元组等）
'''
print(Q3)

da = {0:1,'st':1,2:'st',True:1,3:True,1 + 2j:3.4,('a','b'):[6,7],5:('3','5'),6:{8,9},7:{'h':5}}

print(da)


#可变不可做key  任何数据类型都可以做VALUE
