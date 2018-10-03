#闭包函数定义：定义在函数内部的函数，特点是：包含对外部作用域而不是对全局作用域名字的引用，该函数就称之为闭包函数

# x=1
# def outter():
#     x=2
#     def inner():
#         print(x)
#     return inner
#
#



# f=outter()
#
# def f1():
#     x=1000000000
#     f()
#
# f1()



from urllib.request import urlopen

#函数体内内部需要一个变量，有两种解决方案
#一种是：以参数的形式传入
# def get(url):
#     return urlopen(url).read()
# get('http://www.baidu.com')
# get('http://www.baidu.com')
# get('http://www.baidu.com')


#另外一种：包起来
# def get(url): #url='http://www.baidu.com'
#     # url='http://www.baidu.com'
#     def inner():
#         return urlopen(url).read()
#     return inner
#
# baidu=get('http://www.baidu.com')
# print(baidu)
# res=baidu()
# baidu()
# baidu()
# baidu()
# baidu()





# def get(x,y):
#     def inner():
#         print(x,y)
#     return inner
#
# baidu=get('a','b')
#
# print(baidu.__closure__[0].cell_contents)
# print(baidu.__closure__[1].cell_contents)

x,y=1,2
def get():
    y=111111
    def inner():
        print(x,y)
    return inner

baidu=get()
baidu()