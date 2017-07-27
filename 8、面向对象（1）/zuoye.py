#python第八次作业
'''
13-晓振-Py201706062-第八次作业
'''

#第二题

Q2 = '''
2.定义一个矩形的类：
    要求：1.有长和宽的属性
         2.有一个计算面积的方法
'''
#print(Q2)

class RectMode:
    
    def __init__(self,length,width):
        #长宽参数不能为出int float以外的类型
        if isinstance(length,(int,float)) and isinstance(width,(int,float)):
            self.length = length
            self.width = width
        else:
            #print('类型错误')
            raise TypeError

    def cal_area(self):
        print('面积为：%d'%(self.length * self.width))
#实例化        
shape1  =  RectMode(15,5)
#print('测试1整数长宽测试：',end = '')
#shape1.cal_area()
shape2 = RectMode(11.5,5.4)
#print('测试1浮点数长宽测试:',end = '')
#shape2.cal_area()


#第三题
Q3 = '''
3.写一个正方形的类，继承矩形类
    要求：有一个判断是不是正方形的方法
'''
print(Q3)

class  Squera(RectMode):
    def judge(self):
        if self.length == self.width:
            #print("'长%d'='宽%d'"%(self.length,self.width))
            print('这是一个正方形')
        else:
            print('这不符合正方形')

squera1 = Squera(22,22)
print('测试正方形：',end = '')
squera1.judge()
squera2 = Squera(23,22)
print('测试不是正方形：',end = '')
squera2.judge()


#return  在编辑器里面 返回值不会打印  在shell里面会打印，返回值可以付给变量
#print  shell 和编辑器都可以
