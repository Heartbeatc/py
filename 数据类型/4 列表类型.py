#作用：多个装备，多个爱好，多门课程，多个女朋友等

#定义：[]内可以有多个任意类型的值，逗号分隔
my_girl_friends=['alex','wupeiqi','yuanhao',4,5] #本质my_girl_friends=list([...])


#优先掌握的操作：
# 按索引存取值(正向存取+反向存取)：即可存也可以取
# print(my_girl_friends[2])
# print(my_girl_friends[-1])
# print(id(my_girl_friends))
# my_girl_friends[0]='SB'
# print(id(my_girl_friends))
# print(my_girl_friends)

# 切片(顾头不顾尾，步长)
# print(my_girl_friends[0:2])
# print(my_girl_friends[0:4:2])


# 长度
# print(len(my_girl_friends))

# 成员运算in和not in
# print('alex' in my_girl_friends)
# print(5 in my_girl_friends)



# 追加
# my_girl_friends.append('6号')
# print(my_girl_friends)

# 删除
# del my_girl_friends[2]
# print(my_girl_friends)

# print(my_girl_friends.remove('yuanhao')) #remove是单纯的删除，不会返回删除的值，并且是按照值去删
# res=my_girl_friends.pop(1) #按照索引取删，默认从末尾开始删
# print(res)

# my_girl_friends.pop() #按照索引取删，默认从末尾开始删

# print(my_girl_friends)

# 循环


#常用操作：

my_girl_friends=['alex','wupeiqi','alex','yuanhao',4,5] #本质my_girl_friends=list([...])

# my_girl_friends.insert(0,'sb_alex')
# my_girl_friends.insert(2,'yh')

# my_girl_friends.extend([1,2,3,4])

# print(my_girl_friends.count('alex'))
# print(my_girl_friends)


#了解
# my_girl_friends.clear()
# print(my_girl_friends)
# l=my_girl_friends.copy()
# print(l)


#
# my_girl_friends.reverse()
# print(my_girl_friends)

# l=[3,4,-1,2]
# l.sort(reverse=True)
# print(l)




#练习：
#队列：先进先出
#append，pop
# l1=[]
# l1.append('first')
# l1.append('second')
# l1.append('third')
#
# print(l1.pop(0))
# print(l1.pop(0))
# print(l1.pop(0))



#堆栈：先进后出

# l1=[]
# l1.append('first')
# l1.append('second')
# l1.append('third')
#
# print(l1.pop())
# print(l1.pop())
# print(l1.pop())

l1=[]
l1.insert(0,'first')
l1.insert(0,'second')
l1.insert(0,'third')
print(l1)
print(l1.pop(0))
print(l1.pop(0))
print(l1.pop(0))





























