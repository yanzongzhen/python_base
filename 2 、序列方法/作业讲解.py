#第一题
li = ['a','b','c']
li.append('ef')
li.extend('hg')
li.extend(['f','e']) #这是一个列表参数
li.insert(1,'add1')

li += [1,2]   #列表的加法


#第二题
li = ['a','b','c','d','ee']
li.index('c')
li.insert(3,'add1')
li.pop(4)

li[0] = 'bb'
li[1] = ['a1','b1']
li[1][0]


#第三题

te = 'string test'
#te = te.repalce('test','OK')

