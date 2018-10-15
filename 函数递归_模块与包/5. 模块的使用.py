#第一部分：impoet


'''


import spam


import sys

print(sys.modules)
print('spam' in sys.modules)





#import 倒入文件都做了哪些事
#1 以源文件为准产生一个名称空间
#2 以刚刚产生的名称空间为准，执行源文件的代码
#3 会在当前文件中定义一个名字，这个名字就是模块名，


'''






#为模块起别名

'''


import spam as sm

print(sm.money)





engine_type='oracle'


if engine_type == 'msyql':
    import mysql as engine
elif engine_type == 'oracle':
    import oracle as engine




engine.parse()

'''

'''


#在一行倒入多个模块


import spam,time



'''


##第二部分  from....money.....

'''
from spam import money,read1

print(money)

'''





import spam







