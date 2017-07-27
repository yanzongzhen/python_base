#1.把老师上课例子都敲一遍

#2.定义一个函数，输入一个序列(序列元素是同种类型)，判断序列是顺序还是逆序，顺序输出UP，逆序输出DOWN，否则输出None
def sud(seq):
    li = list(seq)
    if sorted(seq) == li:
        return 'UP'
    elif li == list(reversed(sorted(seq))):
        return 'DOWN'
    else:
        return 'NONE'
    
a = 'abcd'
b = 'dcba'
c = 'Abcd'

f = [1,2,3]
g = [3,4,3,2]

h = (1,2,3,4)
i = (3,2,1)

#3.一个列表，有4个由数字组成的长度为4的元组，对这四个元组，按每个元组的第2个数字大小排序
li = [(1,2,3,4),(1,6,4,5),(2,3,4,5),(2,4,5,8)]

#算法1 插入排序
'''
step1 最开始取前面两个 (1,2,3,4),(1,6,4,5)
step2 排序 2，6
step3:往后走(1,2,3,4),(1,6,4,5),(2,3,4,5)取第三个
step4：排序2,6,3
step5:3<6 交换(1,6,4,5),(2,3,4,5)位置
step6:(1,2,3,4),(2,3,4,5)，(1,6,4,5)
step7:往后走(1,2,3,4),(2,3,4,5)，(1,6,4,5)取(2,4,5,8)再依次和前面的作对比，比前面大不往前走
'''
def insert_sort(li):
    for i in range(1,len(li)):
       # print(i)
        print('第%s执行前'%(i),li)
        key = li[i]
       # print(li[i])
        j = i - 1
       #print(j)
        while j >= 0 and li[j][1] > key[1]:
            li[j + 1] = li[j]
            li[j] = key
            j -= 1
        print('第%s执行后'%(i),li)
    return li
#insert_sort(li)

#算法2  冒泡排序
'''
第0执行前 [(1, 2, 3, 4), (1, 6, 4, 5), (2, 3, 4, 5), (2, 4, 5, 8)]
第0执行后 [(1, 2, 3, 4), (1, 6, 4, 5), (2, 3, 4, 5), (2, 4, 5, 8)]
第1执行前 [(1, 2, 3, 4), (1, 6, 4, 5), (2, 3, 4, 5), (2, 4, 5, 8)]
第1执行后 [(1, 2, 3, 4), (2, 3, 4, 5), (1, 6, 4, 5), (2, 4, 5, 8)]
第2执行前 [(1, 2, 3, 4), (2, 3, 4, 5), (1, 6, 4, 5), (2, 4, 5, 8)]
第2执行后 [(1, 2, 3, 4), (2, 3, 4, 5), (2, 4, 5, 8), (1, 6, 4, 5)]
第3执行前 [(1, 2, 3, 4), (2, 3, 4, 5), (2, 4, 5, 8), (1, 6, 4, 5)]
第3执行后 [(1, 2, 3, 4), (2, 3, 4, 5), (2, 4, 5, 8), (1, 6, 4, 5)]
'''
def bubble_sort(li):
    for i in range(len(li)):
        print('第%s执行前'%(i),li)
        for j in range(i+1,len(li)):
            if li[i][1] > li[j][1]:
                li[i],li[j] = li[j],li[i]
        print('第%s执行后'%(i),li)
    return li

def bubble_sort(li):
    for i in range(len(li)):   #从第一个开始
        print('第%s次执行前'%(i),li)  #查看每次的结果
        for j in range(0,len(li) - i -1):   #从i后面一个开始
            if li[j][1] > li[j+1][1]:   #如果前面大于后面就交换元素
                li[j],li[j+1] = li[j+1],li[j]   #每次会把最小的放到最前
        print('第%s次执行后'%(i),li)
    return li

#bubble_sort(li)        

#算法3、归并排序  merge_sort
'''
1、列表分成两部分 left:(1, 2, 3, 4), (1, 6, 4, 5),(4,9,7,10) right:(2, 3, 4, 5), (2, 4, 5, 8)
2、分别左右排序
3、合并每部分
4、[] left 和 right 中最小的添加到空列表
5、【(1, 2, 3, 4)】 在比较剩下的
;;;;
6、[(1, 2, 3, 4), (2, 3, 4, 5), (2, 4, 5, 8)]  left:[(1, 6, 4, 5),(4,9,7,10)]  right:[]

'''
def merge(left,right):
    i,j = 0,0
    li = []
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            li.append(left[i])
            i += 1
        else:
            li.append(right[j])
            j += 1
    li += left[i:]
    li += right[j:]
    return li

def merge_sort(li):
    if len(li) <= 1:
        return li
    num  = int(len(li)/2)
    left = merge_sort(li[:num])
    print('left',left)
    right =merge_sort( li[num:])
    print('right',left)
    return merge(left,right)

 #一句搞定  Timsort   
sorted(li,key = lambda x:x[1])
