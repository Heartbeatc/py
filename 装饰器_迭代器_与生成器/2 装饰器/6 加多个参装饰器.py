



import time
current_status={'user':None,'login_status':False}

def timmer(func):
    def inner(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is :[%s]' %(stop_time-start_time))
        return res

    return inner

def auth(egine='file'):
    # egine='file'
    def wrapper(func):
        def inner(*args,**kwargs):
            if current_status['user'] and current_status['login_status']:
                res = func(*args, **kwargs)
                return res

            if egine == 'file':
                u='egon'
                p='123'
            elif egine == 'mysql':
                u = 'egon'
                p = '123'
            elif egine == 'ldap':
                u = 'egon'
                p = '123'
            else:
                pass
            name = input('username>>:').strip()
            pwd = input('password>>:').strip()
            if name == u and pwd == p:
                print('login successfull')
                current_status['user'] = name
                current_status['login_status'] = True
                res = func(*args, **kwargs)
                return res
        return inner
    return wrapper


@timmer
@auth(egine='ldap') #@wrapper #index=wrapper(timmer_inner)
# @timmer #timmer_inner=timmer(index)
def index():
    time.sleep(1)
    print('welcome to index page')
    return 123


index() #inner()




