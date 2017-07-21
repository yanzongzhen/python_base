#第七次作业
'''
13-晓振-Py201706062-第七次作业
'''

#第二题
Q2 = '''
    题二：定义一个函数，输入一个序列(序列元素是同种类型)，
判断序列是顺序还是逆序，顺序输出UP，逆序输出DOWN，否则输出None
'''
print(Q2)

def rank(x):
    if list(x) == list(sorted(x)):
        print('UP')
    elif list(x) == list(reversed(sorted(x))):
        print('Down')
    else:
        print('None')

a = (1,2,3,6,7)
b = [2,4,5,6,3,3]
s = 'kji'

print('测试升序元祖',a)
test1 = rank(a)
print('测试列表',b)
test2 = rank(b)
print('测试字符串',s)
test3 = rank(s)


#第三题
Q3 = '''
    题三：一个列表，有4个由数字组成的长度
为4的元组，对这四个元组，按每个元组的第2个数字大小排序
'''
print(Q3)

li = [(1,2,3,4),(1,6,4,5),(2,3,4,5),(2,4,5,8)]
print('利用key进行排序\n')
l1 = sorted(li,key = lambda x:x[1],reverse =True)
l2 = sorted(li,key = lambda x:x[1])
print('逆序',l1)
print('顺序',l2)
    
#测试二
ls = [(1,8,5,4),(5,7,9,6),(9,10,7,6),(1,0,2,3)]
l3 = sorted(li,key = lambda x:x[1])
print('测试通过',l3)
