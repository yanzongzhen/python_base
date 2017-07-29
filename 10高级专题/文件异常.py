#python 高级专题

#文件
path = 'test.txt'  #path 就是路径的意思  相对路径

#path = r'~\yanzongzhen\python_base\10高级专题\test1.txt'#绝对路径  必须带r

#f = open(path,'w+') # w 写入模式，文件存在会清空之前的内容
f = open(path,'a+',encoding = 'utf-8') # a 追加写入模式，不清空之前的文件
#python3 中py文件默认为 utf-8的模式  但是open打开的文件默人不是utf8

a = ['人生苦短，我用python','python是最好的编程语言','测试']

f.writable() #文件可写
    
f.flush() #写入硬盘 从内存写入硬盘
#IO input output 输入输出

#文件指针  从文件开始到结束
#写之后 文件指针在最后

f.read()  #文件指针在最后  read返回空字符串
#并不是文件关闭后再打开文件指针就会回到最开始的位置
#mod r(读) 是回到最开始  a(追加) 为最后

f.tell() #代表文件指针位置
f.seek(0,0) #修改文件指针位置  前面代表偏移   (0,0)为开头
f.seek(2,0) #代表回到开头偏移两个字节

f.write(a[0])
f.write('\n')
f.writelines(a)
f.writelines('\n'.join(a))

#文件指针回到最前面
#seek  close 然后在Open('r')
f.close()
f.closed #判断文件是否关闭 

f = open(path,'r',encoding = 'utf-8')

f.read()  #一次性读完
f.readable() #判断文件是否可读
f.readline() #一次读一行  一行一行读 的读取
f.readlines() #全部读取 返回一个列表  每行作为一个元素

f.mode #查看打开的模式  
f.name #查看路径和文件名字
f.encoding  #查看编码类型

#chardet python2利用pip进行安装

#with
with open(path,'r',encoding = 'utf8') as f2:
    print(f2.read())
#用with打开文件不需要加close 会自己去close
    
#异常
#f1 打开文档
'''
try:
    print('111')
    f1 = open(path,'r',encoding = 'utf-8')
    print(f1.read())
    print('222')
#except NameError as e:
    #print('bbb')

except TypeError as e:
    print('bbb')
except Exception as e:  #as 别名  把异常的信息放到e里面去
    print(e,'bbb')

else:  #没有异常结束就执行  否则不执行
    print('this is a else')

finally:  #不管有没有异常 finaly还是会在执行的
    f1.close()
    print('this is a finally')
#keyboardinterrupt  finally里面还会执行
#except获取异常    
#print('b')
'''
'''
try:
    f = 'this is an error 第%s行输入有误'%4
    raise Exception(f)  #raise 抛出异常  自定义异常
except Exception as e: #这个e是局部的
    print(e)
'''

#assert 断言
assert 1 == 1
#assert 1 == 2

#不需要每一步打印 只有满足一些天监事才报错
#为真不报错 为假才报错   #AssertionError



