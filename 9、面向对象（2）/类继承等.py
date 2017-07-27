#python 面向对象
'''
1、类的继承
2、类的多态
3、多继承
4、类的特殊方法
5、装饰器
6、类的装饰器

'''
#继承
class Animal:  #父类
    ''' 这是一个动物类 '''
    eye = 2   
    def __init__(self,name,food,color = 'yellow',leg = 4): 
        self.name = name  
        self.food = food  
        self._color = color
        self.__leg = leg
        
    def play(self):  
        print('lalala')

class People(Animal):  #子类
    #初始化函数默认继承Animal
    def __init__(self,weight):  #rewrite覆盖父类继承过来的初始化函数  不会影响父类
        #Animal.__init__(self,'夏明','apple')  #重写后添加父类属性  方法一
        super(People,self).__init__(self,'夏明','apple')   #重写后添加父类属性 方法2
        #People,self  可以省略 淡水规范要加上
        self.weight = weight

    def play(self):   #覆盖父类方法  同意函数不同用法==》多态
        super().play()
        print('小明正在玩')

#xm = People('小明','鸡腿') 
xm = People(60)

#count 对不同的序列类型  内部实现方法不同 用法一样

class Asian(Animal):
    def play(self):
        super().play()
        print('Asian is beautiful')

xmm = Asian('xiaomingmama','rice')

class Chinese(People,Asian,):
    def play(self):
        super().play()
        print('china is NO1')
#先找父类中的初始化函数  
xmb = Chinese(60)  #继承两个时候 初始化函数 继承的是第一个

#super 会对继承做排序 保证每个类只会被  调用一次

#类的特殊方法
class RectMode:
    ''' class doc'''
    def __init__(self,length,width):
        if isinstance(length,(int,float)) and isinstance(width,(int,float)):
            self.length = length
            self.width = width
        else:
            print('类型错误')

    def cal_area(self):
        print('面积为：%d'%(self.length * self.width))

    def __str__(self):  #print(a)  覆盖OBJECT本来的方法
        return '长%s,宽%s'%(self.length,self.width)

    def __repr__(self): #直接返回这个对象  优先级  >> str
        return '面积为：%d'%(self.length * self.width)
    
    def __call__(self):
        return "这是一个call方法"
    
    def __add__(self,other):
        add_length = self.length + other.length 
        add_width = self.width + other.width
        return add_length,add_width
    
a = RectMode(3,5)
a.__dict__  #获得属性键值对
a.__doc__  #类的文档字符串
#print(obj) 实际调用类的STR方法
#obj 实际
c = RectMode(4,6)

'a'**2
'''
运算符方法
    __add__(self,other)     x+y
    __sub__(self,other)     x-y 
    __mul__(self,other)     x*y  
    __mod__(self,other)    x%y
    __iadd__(self,other)    x+=y
    __isub__(self,other)    x-=y 
    __radd__(self,other)    y+x
    __rsub__(self,other)     y-x 
    __imul__(self,other)    x*=y 
    __imod__(self,other)    x%=y
'''

