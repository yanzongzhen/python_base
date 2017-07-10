#第二次作业
'''
提交人：13-晓振-Py201706062
日 期：2017、07、10
'''
#第一题：
Q1 = '''
第一题：用多种方法往列表里面插值
'''
print(Q1)

li = [1,2,3,4,'a']
print('定义新的列表',li)

#解题
print('方法一：使用append')
li.append('add1') #方式一
print("li.append('add1')的操作结果:",li)
print('               ')
print('方法二：使用insert')
li.insert(1,'add2') #方式二
print("li.insert(1,'add2')操作结果:",li)
print('              ')
print('方法三：使用extend')
l_2 = ['i love python']
print('定义一个新的列表l_2:',l_2)
li.extend(l_2) #方式三
print("li.extend(l_2)的操作结果:",li)

#第二题：
Q2 = '''
第二题：如何替换列表中的元素
'''
print(Q2)
#解题
A1 = '''
替换的方式：先用index索引再用insert插入最后用pop删除index+1
'''
print(A1)
print('先用index索引再用insert插入最后用pop删除index+1')
l_3 = [1,2,3,4,5,6]
print('定义一个新的列表对象l_3:',l_3)
print('l_3.index(2)索引值：',l_3.index(2))
l_3.insert(1,'new')
print("l_3.insert(1,'new')操作结果：",l_3)
l_3.pop(2)
print('l_3.pop(2)操作结果:',l_3)


#第三题
Q3 = '''
第三题:te = 'string test'  如何把te 中的'test' 替换成'OK'
'''
print(Q3)

te = 'string test'
print('首先创建新的字符串te:',te)
te = te.replace('test','OK')
print('利用replace方法进行操作结果为',te)
