'''
1、为什么要用装饰器：开放封闭原则，对扩展是开放的，对修改是封闭的

2、什么是装饰器
    - 用来装饰它人，装饰器本身可以是任意可调用对象，被装饰器的对象也可以是任意可调用对象
    - 遵循的原则：1、不修改被装饰对象的源代码 2、不修改被装饰对象的调用方式
    - 目标是：在遵循原则1和2的前提，为被装饰器对象添加上新功能


'''

import time

def timmer(func):
    # func=index #最原始的index函数的内存地址
    def inner():
        start_time=time.time()
        func()
        stop_time=time.time()
        print('run time is :[%s]' %(stop_time-start_time))
    return inner

@timmer #index=timmer(index)
def index():
    time.sleep(3)
    print('welcome to index page')


index()



