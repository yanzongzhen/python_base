#第三次作业
'''
提交人：13-晓振-Py201706062
'''

#第一题：
Q1 = '''
#第一题题目:a = '苦短' b = 'Python' 用字符串拼接的方法输出'人生苦短，我用Python'
'''
print(Q1)

a = '苦短'
b = 'Python'
print('首先定义两个字符串:\na为',a,'\nb为',b)

print('\n方式一：利用+进行拼接')
A1 = '人生'+a+','+'我用'+b
print("'人生'+a+','+'我用'+b -> 运行结果:",A1)

print('\n方式2:利用%s进行格式化输出拼接')
A2 = '人生%s,我用%s'%(a,b)
print("'人生%s,我用%s'%(a,b) -> 运行结果:",A2)

print('\n方式3:使用join进行拼接')
A3 = ','.join(['人生'+a,'我用'+b])
print("','.join(['人生'+a,'我用'+b]) -> 运行结果:",A3)

print('\n方式4:利用format进行拼接')
A4 = '人生{},我用{}'.format(a,b)
print("'人生{},我用{}'.format(a,b) -> 运行结果:",A4)

#第二题
Q2 = '''
第二题题目：列表li = ['I','like','python'],将里面的单个单词拼成一句话
'''

print('\n',Q2)

li = ['I','like','python']
print('首先定义li列表为:\n','li = ',li)
print('\n方式一:利用join进行拼接')
AN1 = ' '.join(li)
print("' '.join(li) -> 运行结果:",AN1)

print('\n方式二:利用索引进行拼接')
AN2 = str(li[0])+' '+str(li[1])+' '+str(li[2])
print("str(li[0])+' '+str(li[1])+' '+str(li[2]) -> 结果：",AN2)

print('\n方式三:索引配合FORMAT')
AN3 = '{} {} {}'.format(str(li[0]),str(li[1]),str(li[2]))
print("'{} {} {}'.format(str(li[0]),str(li[1]),str(li[2])) -> 结果:",AN3)

print('\n方式四：利用索引和%s配合')
AN4 = '%s %s %s'%(str(li[0]),str(li[1]),str(li[2]))
print("'%s %s %s'%(str(li[0]),str(li[1]),str(li[2])) -> 结果:",AN4)


#第三题
Q3 = '''
#第三题题目：用格式化输出的方式，打印上面的两句话
'''
print('\n',Q3)
print("\n第一题格式化输出的方式为:%s")   
AA1 = '人生%s,我用%s'%(a,b)
print("'人生%s,我用%s'%(a,b) -> 运行结果:",AA1)    

print("\n第二题格式化输出的方式为:%s")   
AA4 = '%s %s %s'%(str(li[0]),str(li[1]),str(li[2]))
print("'%s %s %s'%(str(li[0]),str(li[1]),str(li[2])) -> 结果:",AA4) 

