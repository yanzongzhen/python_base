#python基础 面向对象

#1.把上课的例子都敲一遍


#2.实现一个正方形类的加减乘除
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
            return True
        else:
            return False
        
    def __add__(self,other): #加法
        return self.area() + other.area()
        #return Square(self.area() + other.area(),self.area() + other.area())

    def __sub__(self,other):  #减法
        return abs(self.area() - other.area())  #abs取绝对值

    def __mul__(self,other):  # * 
        return self.area() * other.area()

    def __truediv__(self,other):  # / 
        return self.area() / other.area()

    def __floordiv__(self,other): # //
        return self.area() // other.area()

    def __radd__(self,other):  #先在前面找add,不能的话就找radd
        return other + self.area()

a = Square(3,3)
b = Square(5,5)
c = Square(8,8)

#3.测试归并排序和冒泡排序哪个更快
import time
def run_time(func):
    def new_fun(*args):
        t0 = time.time()
##        print('star time: %s'%(time.strftime('%x',time.localtime())) )
        back = func(*args)
##        print('end time: %s'%(time.strftime('%x',time.localtime())) )
        times = time.time() - t0
##        print('run time: %s'%(times))
        return back,times
    return new_fun

#冒泡排序 bubble_sort(lists)  time_com n^2  space_com 1
@run_time
def bubble_sort(lists):
    for i in range(len(lists)):  #从第一个开始
        # print('第%s执行开始'%(i),lists) #查看每次的结果
        for j in range(0,len(lists)-i-1): #从i后面一个开始
            if lists[j] > lists[j+1]:  #如果前面大于后面就交换元素
                lists[j],lists[j+1] = lists[j+1],lists[j]  #每次会把最小的放到最前
        # print('第%s执行结束'%(i),lists) #查看每次的结果
    return lists


# 归并排序  merge_sort  time_com  nlogn  space_com n

def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 比较
            result.append(left[i])  # 小的添加
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  # 当一个循环结束之后，另一个直接添加就行
    result += right[j:]
    return result


def merge_sort(lists):
    if len(lists) <= 1:  # 元素只有一两个的时候就不要再分
        return lists
    num = int(len(lists) / 2)
    left = merge_sort(lists[:num])  # 分到最小
    # print('left', left)
    right = merge_sort(lists[num:])  # 分到最小
    # print('right', right)
    return merge(left, right)  # 进行排序

@run_time
def merge_sort_list(lists):
    lists = merge_sort(lists)
    return lists

li = [2,3,4,5,3,8,6,7,7,0,1,2,9,5,3,6,2,6,7,8,4,1,3,2,7,10,3,2]

import random
def list_builder(times):
    li = []
    for i in range(times):
        li.append(random.randint(1,times))
##    li = [random.randint(1,times) for i in range(times)] #列表推导
    return li


#取平均值，根据平均值做比较
def test(times,length):
       
    bubble_sort_times = []
    merge_sort_list_times = []

    for i in range(times):
        li = list_builder(length)
        result,running_time = bubble_sort(li)
        bubble_sort_times.append(running_time)

    for j in range(times):
        li = list_builder(length)
        result1,running_time1 = merge_sort_list(li)
        merge_sort_list_times.append(running_time1)

    bubble_time = avg(bubble_sort_times)
    merge_time = avg(merge_sort_list_times)
    print(bubble_time,merge_time)

    if merge_time < bubble_time:
        print('归并排序更加快！')
    else:
        print('冒泡排序更加快！')


def avg(lists):
    length = len(lists)
    return sum(lists)/length




