#python基础 面向对象

'''
1、概念
2、类的定义
3、类的实例化
4、类和实例的属性
'''
#概念
a = 1
type(a)
'''
把有相同特征的东西抽象出来，取个名字例如A，若下次有个东西也有这个特征
的时候，我们就称之属于A这个类，归并为A类
'''

#定义类
class Animal:  #驼峰命名法  #3中默认继承OBJECT类  2中必须写object
    ''' 这是一个动物类 '''
    eye = 2   #共有属性
    def __init__(self,name,food,color = 'yellow',leg = 4): #init 类的实例化初始函数
        self.name = name  #self代表实例化对象自己
        self.food = food  #实例属性
        self._color = color
        self.__leg = leg
        
    def play(self):  #实例调用的时候会传self进去
        print('%s;lalala'%(self.name))

    def GetName(self):
        self.play()
        
        
        
#实例化  得到这个类一个具体的例子    
minions = Animal('minions','banana')
dog = Animal('旺财','bone')

#属性 和 方法

#属性就是类里面的变量

#self代表实例化对象自己
#dog.play()  #实例调用方法时 会把实例本身传入

#方法里的SELF 只要实例调用这个方法  就必须写

#方法就是类的函数
#注意self的问题

'''
#self.name 称之为实例属性
#eye  类属性共有属性
#Animal.name   #类没有实例的属性 
'''
minions.eye = 1
dog.eye  #不改变原有属性

Animal.eye = 4
dog.eye   #类属性改变实例也会变

'''
实例的类属性都是指向类的，但是如果实例改变原来类属性就会新建一个对象
而不会改变类的属性
类本身属性变了 实例是指向类的化也会改变
'''

#类的私有属性

#一个_
#self._color

#两个_
dog._Animal__leg = 6
dog._Animal__leg

#私有的可以改但是不建议改

#数据的封装


