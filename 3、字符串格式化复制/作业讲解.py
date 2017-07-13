#作业讲解

'''
格式化 %
拼接 + join format
'''
#1.a = '苦短' b = 'Python' 用字符串拼接的方法输出'人生苦短，我用Python'
a = '苦短'
b = 'Python'
'人生' + a + ',' + '我用' + b
'人生%s,我用%s'%(a,b)
''.join(['人生',a,',','我用',b])
'人生{},我用{}'.format(a,b)

#2.列表li = ['I','like','python'],将里面的单个单词拼成一句话

li = ['I','like','python']

' '.join(li)

'%s %s %s'%(li[0],li[1],li[2])

'{0[0]} {0[1]} {0[2]}'.format(li)

#3.用格式化输出的方式，打印上面的两句话
s1 = '人生苦短,我用Python'
s2 = 'I like python'

'%s'%s1
'%s2'%s2
