#python基础

'''
问题1、什么是正则
'''
a = 'python'
b = 'python pn pyn pytn python'
'''
if a in b:
    print ('OK')
else:
    print ('NO')
'''

def str_in(stra,strb):
    if stra in strb:
        return True
    else:
        return False
'''
只管首尾不管中间元素
'''
def str_on(sts,ste,stra):
    be = end = 0
    li = []
    for i in stra:
        if i == sts:
            be = stra.index(i,end)
        elif stra[be] == sts and i == ste:
            end = stra.index(i,be) + 1
            li.append(stra[be:end])
        else:
            continue
    return li
str_on('p','n',b)

#在python中使用正则要导re模块
import re
re.findall(r'p[\w]*n',b) #很大的提高我们效率
#上面的就是正则

'''
问题二：python如何写正则表达式
'''
#例子一
re.findall('a','abdfgaa') #前面参数是要匹配的字符串  后面的是被查找的字符串
re.findall('.','abc.a.a')

#正则元字符
#. ^ $ * + ？ {} [] \ | ()
'''
以上字符在正则中不识原来的意思
'''
re.search('\bs\b','abc s w')
re.search(r'\bs\b','abc s w') 
'''
<_sre.SRE_Match object; span=(4, 5), match='s'>
span=(4, 5)  表示字符串出现的位置
match='s' 表示匹配的字符
'''
#正则必须加r保持元字符  以免以上符号被转义
'''
.    匹配除换行符之外的所有的字符
\d  匹配0~9的数字   
\s   匹配任意的空白符，包括空格，制表符(Tab)，换行符等
\w 匹配字母或数字或下划线或汉字等 
\b  表示单词的边界		
^    脱字符，匹配输入字符串的开始的位置
$   匹配输入字符串的结束位置，解除元字符的特殊功能例
\.   表示匹配点号本身
\D、\S、\W、\B是与小写的相反的作用
\D除啦数字以外的字符
'''
#实例
re.search(r'.','hc')
re.search(r'.','\nhc')
re.search(r'\d','ab123')
re.search(r'\d+','ab123')
re.search(r'\s','ab 123')
re.search(r'\w','i2')
re.search(r'\w','啥')
re.search(r'\w','_2')
#单词边界
re.search(r'\bc\b','ab c 12')
re.search(r'\ba','ab c 12')
re.search(r'2\b','ab c 12')

re.search(r'\.','ab.cd')

re.search(r'\D','ab123')
re.search(r'\S','ab 123')

re.search(r'^a','abc')  #匹配是不是以a开始
re.search(r'c$','abc')  #结尾

#{} 匹配次数
re.search(r'\d','12ab23')
re.search(r'\d{1,3}','12ab23')
re.search(r'\d{1,3}','1234ab23')  #匹配1-3次

#比较{}数字的作用
re.search(r'\d{1,}','123423')  #后面没写就是一次到无限次
re.search(r'\d{0,}','1234ab23')  #匹配0次  不等于 不匹配
re.search(r'\d{0,}','aa1234ab23')
re.search(r'\d{,3}','1234ab23') #前面不写 等于 {0，3} 默认是0次

re.findall(r'\d{3}','12sf23332333')  #匹配三次

# * + ？
re.findall(r'\d*','12sf2334455') #{0,}  
re.findall(r'\d+','12sf2334455') #{1,}
re.findall(r'\d?','12sf2334455')  #{0,1}

#*? +?
re.findall(r'\d*?','12sf2334455')  #{0,0}
re.findall(r'\d+?','12sf2334455')  #{1,1}
re.findall(r'\d{1,}?','12sf2334455')

'''
* + 被称为贪婪模式
？ 懒惰模式
后面加？{n,m} - > {n,n} 非贪婪模式
'''

#子组匹配
#[] 字符类，将要匹配的一类字符集放在[]里面
re.findall(r'[\d]','12ab233')
re.findall(r'[0-9]','12ab233')

re.findall(r'[ab]','12ab233')
re.findall(r'ab','12ab233')
re.findall(r'[a|b]','12ab233')
re.findall(r'a|b','12ab233')
'''
[ . ? * ( ) {} ]     匹配里面的这些符号
[0-9]                 匹配0到9的数字相当于\d
[^\d]                  匹配除数字以外的字符，相当于\D
[a-z]                  匹配所有的小写字母
[^a-z]                 匹配非小写字母
|                       相当于或（or）分支条件
'''

re.findall(r'[^\d]','12ab233')  #在子组里面^是去反的意识
re.findall(r'[. ? * ( ) {} +]','12. ? * ( ) {} +ab233')  #不用特意去转义

'''
[]里面可以放你想要匹配的东西 注意在这个里^是代表 取反的意思
'''

#()分组
#()  分组，将要匹配的一类字符集放在()组成一个小组
re.findall(r'(2|3)','12ab2333')
re.findall(r'(23)','12ab2333')
re.findall(r'(\d)','12ab2333')

re.findall(r'(^2)','2ab2333')  #()里面的^是开始的位置

#re模块
'''
re模块的常用方法 
    search()   遍历字符串，找到正则表达式匹配的第一个位置   
    findall() 遍历字符串，找到正则表达式匹配的所有位置并以列表的形式返回
    compile() 编译正则表达式为模式对象
    sub()      替换,和字符串的replace类似
    split()    和字符串的split方法类似
    match()   判断一个正则表达式是否从开始处匹配字符串 
   
查看匹配对象中的信息   
    group() 返回匹配到的字符串
    star()返回匹配的开始位置  
    end()返回匹配的结束位置  
    span()  返回一个元组表示匹配位置（开始，结束）
'''
#compile() 编译正则表达式为模式对象
a = re.compile(r'\d')
a.findall('12ad333')

#sub()      替换,和字符串的replace类似
re.sub('i','o','pythin',1)  #想换掉的字符  替代的字符  要改变的字符串  替换次数

b = re.compile('i')
b.sub('o','python',1)

#split()    和字符串的split方法类似
re.split(r'a','abc de rf')
re.split(r'[\s|,]','abc de, rf')
re.split(r'[\s|,]','abc de,s rf')
re.split(r'\s',' ass')   #空格前面没有东西 所以分割后会有空字符

#match()   判断一个正则表达式是否从开始处匹配字符串   相当于^字符
re.match(r'\d','112233aa')
re.match(r'3$','ad112233dd')


c = re.search(r'[2|3]','12ab.?*+(){}233566')
c.group()#返回匹配到的字符串
c.start()#返回匹配的开始位置 
c.end()#返回匹配的结束位置  
c.span() # 返回一个元组表示匹配位置（开始，结束）
