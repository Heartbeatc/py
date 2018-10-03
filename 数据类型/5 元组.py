#作用：存多个值，对比列表来说，元组不可变（是可以当做字典的key的），主要是用来读
#定义方式：
ages=(10,12,18,33,18) #ages=tuple((10,12,18,33))
# print(id(ages),type(ages),ages)


#优先掌握的操作：
# 按索引取值(正向取+反向取)：只能取
# 切片(顾头不顾尾，步长)
# print(ages[0:2])
# print(ages)
# 长度
# print(len(ages))
# # 成员运算in和not in
# print(10 in ages)

#其他操作：
# print(ages.index(18))
# print(ages.index(123123123123))

# print(ages.count(18))




# l=['a','b','c','d','e']
# # l='abcde'
# l=('a','b','c','d','e')
# index=0
# while index < len(l):
#     print(l[index])
#     index+=1



# l1=['a','b','c','d','e']
# for item in l1:
#     print(item)
# l2='abcde'
# for item in l2:
#     print(item)
# l=('a','b','c','d','e')


# for i in range(1,10,2):
#     print(i)
# l1=['a','b','c','d','e']
# for i in range(len(l1)):
#     print(i,l1[i])



# msg_dic={
# 'apple':10,
# 'tesla':100000,
# 'mac':3000,
# 'lenovo':30000,
# 'chicken':10,
# }
#
# goods_l=[]
# while True:
#     for key in msg_dic:
#         print(key, msg_dic[key])
#     choice = input('商品名>>: ').strip()
#     if choice not in msg_dic:continue
#     count = input('个数>>: ').strip()
#     if count.isdigit():
#         goods_l.append((choice,msg_dic[choice],int(count)))
#         print(goods_l)




#while+else
# for i in range(5):
#     if i == 3:break
#     print(i)
# else:
#     print('ok')

print(hello word)



