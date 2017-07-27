#第九次作业
'''
13-晓振-Py201706062-第九次作业
'''

#第二题
Q2 = '''
第二题：实现一个正方形类的加减乘除
'''
#print(Q2)

class Rectangle:
    def __init__(self,length,width):
        if isinstance(length,(int,float)) and isinstance(width,(int,float)):
            self.length = length
            self.width  = width
    def area(self):
        areas = self.length * self.width
        return areas
class Square(Rectangle):
    def judgement(self):
        if self.length == self.width:
            return '这是正方形'
        else:
            return '不是正方形，请重新传参'

    def __add__(self,other):
        areas = self.area() + other.area()
        return areas
    def __sub__(self,other):
        areas = self.area() - other.area()
        return areas
    def __mul__(self,other):
        areas = self.area() * other.area()
        return areas
    def __mod__(self,other):
        areas = self.area() % other.area()
        return areas
    def __truediv__(self,other):
        areas = self.area() / other.area()
        return areas
    def __floordiv__(self,other):
        areas = self.area() // other.area()
        return areas      
a =  Square(3,3)
b =  Square(5,5)
#print('两个正方形相加',a+b)
#print('两个正方形相减',a-b)
#print('两个正方形相乘',a*b)
#print('两个正方形相除',a/b)
#print('两个正方形相整除',a//b)

#第三题
Q3 = '''
第三题：测试归并排序和冒泡排序哪个更快
'''
print(Q3)

li = [(1,2,3,4),(1,6,4,5),(2,3,4,5),(2,4,5,8)]

import time 
def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        print('star time: %s'%(time.strftime('%x',time.localtime())) )
        back = func(*args,**kwargs)
        print('end time: %s'%(time.strftime('%x',time.localtime())) )
        print('###run time: %s###'%(time.time() - t0))
        return back
    return new_fun

print("归并")
@run_time
def merge_sort(li):
    if len(li) <= 1:
        return li
    num  = int(len(li)/2)
    left = merge_sort(li[:num])
    right =merge_sort( li[num:])
    return merge(left,right)

def merge(left,right):
    #print('in')
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

test1 = merge_sort(li)
print('结果',merge_sort(li))

print("冒泡")
@run_time
def bubble_sort(li):
    for i in range(len(li)):   
         
        for j in range(0,len(li) - i -1):  
            if li[j][1] > li[j+1][1]:  
                li[j],li[j+1] = li[j+1],li[j] 
        
    return li

test2 = bubble_sort(li)
print('结果',bubble_sort(li))
