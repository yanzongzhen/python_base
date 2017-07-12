#字符串的拼接
s = 'hello'
t = 'python'
r = '!'

#1、+
s + t + r
s + ' ' + t + ' ' + r

#2、格式化  %s
'%s%s%s'%(s,t,r)
'%s %s %s'%(s,t,r)

#3、join   常用在列表拼接成字符串
' '.join([s,t,r])  # S.join(iterable) -> str
'**'.join('abc')
#列表字符串互相转化
a = s.split()
a = ' '.join(a) 

#4、format
'{} {} {}'.format(s,t,r)   #后面参数只能多不能比大括号少
'{0} {1} {2}'.format(s,t,r) 
'{2} {0} {1}'.format(s,t,r)
'{n1} {n2} {n3}'.format(n1=s,n2=t,n3=r)

li = ['a','b']
'{0[0]} {0[1]}'.format(li)
'{0[0]} {0}'.format(li)


#格式化输出



#深复制 浅复制
