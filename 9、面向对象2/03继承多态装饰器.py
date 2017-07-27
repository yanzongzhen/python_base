#python基础 面向对象

#继承
class Animal:  #父类
    eye = 2 
    leg = []
    """ animal  class"""
    def __init__(self,name,food,color = 'yellow'):  
        self.name = name  
        self.food = food

    def play(self):    
        print('Animals are strong')

minions = Animal('minions','banana')   
dog = Animal('dog','bone')

class People(Animal):  #子类
    #初始化函数默认继承Animal的
    def __init__(self,weight):  #覆盖父类的初始化函数  不会影响父类
##        Animal.__init__(self,'xiaoming','apple')
##        super(People,self).__init__('xiaoming','apple')#可以调用父类的方法
        #People,self  可以省略，但是规范是加上的
        self.weight = weight
    def play(self):  #覆盖父类的方法  同一函数不同用法 就是多态
        Animal.play(self)
        super().play()
        print('小明正在玩')

xm = People(57)
##xm = People('xiaoming','apple')

#count  对不同的序列类型，内部实现方法不一样，用法是一样的

class Asian(Animal):
    def play(self):
        super(Asian,self).play()
        print('Asian is beautiful')
xmm = Asian('xiaomingma','rice')

class Chinese(People,Asian):
    def play(self):
        super().play()
        print('中国人第一')
##xmb = Chinese('xiaomingma','noodle')  #先找父类里面的初始化函数
xmb = Chinese(60) #继承两个的时候初始化函数是继承的第一个

#super 会对继承树做排序，保证每个父类只会被调用一次
'''
在多继承里面:
子类永远在父类前面
如果有多个父类，会根据它们在列表中的顺序被检查,前面的父类的方法优先于后面父类的方法
super和保证所有的类只被调用一次，不会被重复调用
'''
#类的特殊方法
class Rectangle:
    '这是一个矩形类'
    def __init__(self,length,width):
        if isinstance(length,(int,float)) and isinstance(width,(int,float)):
            self.length = length
            self.width  = width
        else:
            raise TypeError
            #return None
    def area(self):
        areas = self.length * self.width
        return areas
    
    def __str__(self):  #print(b)  覆盖object里面本来的方法
        return '宽为%s,高为%s'%(self.width,self.length)
    
    def __repr__(self):  #b
        return '面积为:%s'%(self.area())
    
    def __call__(self):
        return '这是call方法'

    def __add__(self,other):
        add_length = self.length + other.length
        add_width = self.width + other.width
        return add_length,add_width
    
b = Rectangle(3,5)
c = Rectangle(4,6)
b.__dict__ #数据属性组成 object类继承的
b.__doc__
#print(obj) #实际上是调用类的__str__方法
##'aa'+ 2 # 现在前面这个对象找add方法，如果没有，就去后面找radd方法

#4.装饰器

#闭包
def fx(x):
    x += 1
    def fy(y):
        return x*y
    return fy

fx(1)(2)
temp = fx(1)
temp(2)

def fu1(func):  #在python里面可以把函数当变量一样来传  
    print('fu1 running')
    def fu2(y):
        print('fu2 running')
        return func(y) + 1  #gun(y) + 1
    return fu2

def gun(m):
    print('gun running')
    return m*m

'''
temp = fu1(gun)
temp(1)

step1:print('fu1 running')
step2:return fu2
step3:temp(1)
step4:print('fu2 running')
step5:print('gun running')
step6:return 1*1
step7:return 1+1
'''

@fu1 #装饰器   #语法糖 deco = fu1(deco)
def deco(m):
    print('这是deco')
    return m*m   #这里通过装饰器的作用，实现啦给deco的返回值加 1 的功能

def test(): #@fu1对这个函数没有影响
    pass

'''
step1:fu1(deco)
step2:print('fu1 running')
step3:deco = fu2

deco = fu1(deco)
'''
#用装饰器来查看程序的运行时间
import time  #自带的时间模块
def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        print('star time: %s'%(time.strftime('%x',time.localtime())) )
        back = func(*args,**kwargs)
        print('end time: %s'%(time.strftime('%x',time.localtime())) )
        print('run time: %s'%(time.time() - t0))
        return back
    return new_fun

@run_time
def test():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%dx%d=%2s'%(j,i,i*j),end = ' ')
        print ()

#今后大家可以直接拿这个函数去测试你写的函数的执行效率，以及各种方法的执行速度

class Test_Class:
    def __init__(self,func):
        self.func = func
        
    def __call__(self):
        print('类')
        return self.func()
@Test_Class
def fun_test():
    print('测试')

#类的内置装饰器
class Rec:
    def __init__(self,length,width):
        self.width = width
        self.length = length
    def area(self):       #实例
        areas = self.length * self.width
        return areas
    
    @property  #就像访问属性一样
    def area2(self):
        return self.width*self.length
    
    @staticmethod   #静态方法
    def func():    #self  在调用的时候会报错
        print('staticmethod func')
##        print('%s'%self.length) #报错，没有传入self
        
    @classmethod    #类方法
    def show(cls):   #cls 代表类Rec本身
        print(cls)
        print('show fun')
        
e = Rec(3,4)
f = Rec(6,8)
#这几个东西在框架的时候用，一般不会用
