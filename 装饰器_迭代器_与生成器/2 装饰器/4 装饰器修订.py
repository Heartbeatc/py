import time
from functools import wraps

def timmer(func):
    @wraps(func)
    def inner(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is :[%s]' %(stop_time-start_time))
        return res

    return inner

@timmer
def index():
    '''
    index function
    :return:
    '''
    time.sleep(3)
    print('welcome to index page')
    return 123

@timmer #home=timmer(home) #home=inner
def home(name):    
    time.sleep(2)
    print('welcome %s to home page' %name)
    return 456

# res=index() # res=inner()
# print(res)
#
# res=home('egon') #inner('egon')
# print(res)

# print(index.__doc__)
print(help(index))

