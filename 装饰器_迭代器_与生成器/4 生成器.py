'''
定义：只要函数内部出现yield关键字，那么再调用该函数，将不会立即执行函数体代码，会到到一个结果
该结果就是生成器对象


'''

'''
def func():
    print('===>first')
    yield 1
    print('===>second')
    yield 2
    print('====>third')
    yield 3


g=func()
# print(next(g))
for i in g:
    print(i)
'''
#生成器本质就是迭代器 
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# print(next(func()))
# print(next(func()))
# print(next(func()))




# for i in g:
#     print(i)
#
# for i in g:
#     print(i)
#
# for i in g:
#     print(i)

'''
yield的功能：
    - 为我们提供了一种自定义迭代器的方式
    - 对比return，可以返回多次值，挂起函数的运行状态

'''

#自定义功能，可以生成无穷多个值，因为同一时间在内存中只有一个值
# def my_range(start,stop,step=1):
#     while start < stop:
#         yield start
#         start+=step


# g=my_range(1,5,2) #1  3
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# for i in my_range(1,1000000000000000000000000000000000000000000,step=2):
#     print(i)




#tail -f access.log | grep '404'
# import time
# def tail(filepath): 
#     with open(filepath,'rb') as f:
#         f.seek(0,2)
#         while True:
#             line=f.readline()
#             if line:
#                 yield line
#             else:
#                 time.sleep(0.2)

# def grep(pattern,lines):
#     for line in lines:
#         line=line.decode('utf-8')
#         if pattern in line:
#             yield line

# g=grep('404',tail('/Volumes/docker/Py/装饰器_迭代器_与生成器/access.log'))
# for line in g:
#     print(line)

















#yield的表达式形式的应用
'''
def eater(name):
    food_list=[]
    print('%s 开动啦' %name)
    while True:
        food=yield food_list #food=‘骨头’
        print('%s 开始吃 %s' %(name,food))
        food_list.append(food)

g=eater('alex')

g.send(None) #next(g)
print(g.send('骨头'))
print(g.send('shi'))
'''


def f1():
    while True:
        x=yield
        print(x)

g=f1()
next(g)  #g.send(None)
g.send(1)
g.send(1)
g.close()
g.send(1)
g.send(1)
g.send(1)



















