#作用：存多个值,key-value存取，取值速度快

#定义：key必须是不可变类型，value可以是任意类型
# d={'a':1}
# d={0:1}
# d={[1,2,3]:1} #列表不能当做字典的key
# d={(0,'mac'):3000}
#
# print(d[(0,'mac')])

info={'name':'egon','age':18,'sex':'male'} #本质info=dict({....})



#优先掌握的操作：
# 按key存取值：可存可取
# print(info['sex'])
# info['hobbies']=['read','music','play','sleep','eat']
# print(info)

# 长度len
# print(len(info))

# 成员运算in和not in


# 删除
# print(info.pop('name'))
# print(info.pop('name1213','确实是没有的，我的哥'))
# print(info.pop('name1213',None))


# 键keys()，值values()，键值对items()
# print(info.keys())
# print(info.values())
# print(info.items())


# for key in info.keys():
#     print(key)

# for val in info.values():
#     print(val)

# for item in info.items():
#     print(item[0],item[1])


# 循环


#常用方法
# info={'name':'egon','age':18,'sex':'male'}
# print(info['name123'])
# print(info.get('name123',123))
# print(info.popitem())
#
#
# for k,v in info.items(): #k,v=('name', 'egon')
#     print(k,v)

# print(info.setdefault('hobbies',['read','music'])) #有则不改，返回已经有的值，没有则新增，返回新增的值
# print(info)

# print(id(info.setdefault('hobbies',[])))
# print(id(info['hobbies']))
l=[]

info={'name':'egon','age':18,'sex':'male',}
# if 'hobbies' not in info:
#     info['hobbies']=[]
#     info['hobbies'].append('music')
# else:
#     info['hobbies'].append('read')
#
# if 'hobbies' not in info:
#     info['hobbies'] = []
#     info['hobbies'].append('music')
# else:
#     info['hobbies'].append('read')
#
# print(info)

# info.setdefault('hobbies',[]).append('music')
#
# # {'name': 'egon', 'age': 18, 'sex': 'male', 'hobbies': ['music', ]}
# info.setdefault('hobbies',[]).append('read') #['music', ].append('read')
# print(info)


#了解
# info_new={'a':1,'age':19}
# info.update(info_new)
# print(info)


# dic={'name':None,'age':None,'sex':None,'hobbies':None}
# dic1={}.fromkeys(['name','age','hobbies'],None)
# print(dic1)












#补充两种赋值方式：
#一：链式赋值
# x=10
# y=x
# x=y=z=10
# print(id(x),id(y),id(z))


#交换两个变量的值
# m=10
# n=20
# temp=n
# n=m #n=10
# m=temp
# print(m,n)
# m,n=n,m
# print(m,n)

#二：从一个数据类型中解压出我们想要的值
# t=(10.3,11.2,12.1,14.3,3.1)

# x,y,z,a,b=t
# print(x,y,z,a,b)

# x,_,_,_,b=t
# print(x,b)
# print(_)

# x,*_,b=t
# print(x,b)


# x,*_='hello'
# print(x)

# x,y,z={'a':1,'b':2,'c':3}
# print(x,y,z)



print('hello word')