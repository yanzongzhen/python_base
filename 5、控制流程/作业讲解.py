#python基础


#1、例子调一遍


#2、输出99乘法口诀表
'''
for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print('%d x %d=%2d'%(j,i,i*j),end = ' ')   #print中sep表示分割  end默认表示换行
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print('%d x %d=%2d'%(j,i,i*j),end = ' ')   #print中sep表示分割  end默认表示换行
    print()

i = 1
while i < 10:
    j = 1
    while j < i+1:
        print('%d x %d=%2d'%(j,i,i*j),end = ' ')   #print中sep表示分割  end默认表示换行
        j += 1
    print()
    i += 1

'''
#3、有两个列表x 和 y，要求：y中的元素如果在x中也有的话，就把该元素从x中移除，不能利用集合的方法
#   在全部移除之后打印：“移除结束”，和x y
x = ['a','a','b','c',1,2,3]
y = ['a','b',2,3]
'''
for i in y:   
    for j in x:
        if i == j:
            x.remove(j)

'''

for i in y:
    while i in x:
        x.remove(i)
else:
    print('移除结束')
    print(x)
    print(y)
