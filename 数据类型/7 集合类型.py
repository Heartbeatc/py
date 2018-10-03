# pythons=['alex','wupeiqi','egon','yuanhao','gangdan','oldboy']
# linuxs=['egon','oldboy','tiedan','liudan']
#
# l=[]
# for item in pythons:
#     if item in linuxs:
#         l.append(item)
# print(l)


# 作用：去重，关系运算，

# 定义：
# 1：每个元素必须是不可变类型(可hash，可作为字典的key)
# 2:没有重复的元素
# 3：无序
# s={1,2,'a','b','c','d','e','f'} #s=set({1,2,'a'})

# print(type(s),s)



# 优先掌握的操作：
# 长度len
# s={1,2,'a','b','c','d','e','f'}
# print(len(s))
# 成员运算in和not in
# print('a' in s)
# for item in s:
#     print(item)



# | 并集
# s1={1,2,3}
# s2={3,4,5}
# print(s1 | s2)

# & 交集
# print(s1 & s2)

# -差集
# print(s1 - s2)
# print(s2 - s1)

# ^ 对称差集
# s1={1,2,3}
# s2={3,4,5}


# ==
# > ， >= ， <, <= 父集，子集
# s1={1,2,3,4}
# s2={3,4,5}
# print(len(s1) > len(s2))

# s1={1,2,3,4}
# s2={3,4}
# print(s1 > s2)
# print(s1 >= s2)




#练习：
# pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
#
# linuxs={'wupeiqi','oldboy','gangdan'}
#
# # 　1. 求出即报名python又报名linux课程的学员名字集合
# print(pythons & linuxs)
# # 　　2. 求出所有报名的学生名字集合
# print(pythons | linuxs)
# # 　　3. 求出只报名python课程的学员名字
# print(pythons -  linuxs)
# # 　　4. 求出没有同时这两门课程的学员名字集合
# print(pythons ^ linuxs)

#常用操作
s1={1,2,3,'a',4}
# print(s1.pop()) #随机删，并返回删除的结果

# s1.remove('a') #单纯地删，不会返回删除的结果，并且如果删除的元素不存在则报错
# s1.remove('asdfasdfa') #单纯地删，不会返回删除的结果
# print(s1)
# print(s1.discard('a')) #单纯地删，不会返回删除的结果，并且如果删除的元素不存在返回None，不会报错
# print(s1)

# s1.add('b')
# print(s1)

s1={1,2,3}
s2={4,5}
# print(s1.isdisjoint(s2)) #如果s1和s2没有交集则返回True




#了解
# s1={1,2,3,4}
# s2={3,4,5}


# | 并集
# print(s1.union(s2))

# & 交集
# print(s1.intersection(s2))
# s1.intersection_update(s2) #s1=s1.intersection(s2)
# print(s1)
# -差集
# print(s1.difference(s2))

# ^ 对称差集
# print(s1.symmetric_difference(s2))


# ==
# > ， >= ， <, <= 父集，子集
# s1={1,2,3,4}
# s2={3,4}
# print(s1.issuperset(s2))
# print(s2.issubset(s1))



#去重
# l=['a','b',1,'a','a']
# print(list(set(l)))

# l=['a','b',1,'a','a']
# l_new=list()
# s=set()
# for item in l:
#     if item not in s:
#         s.add(item)
#         l_new.append(item)
l=[
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
]
l_new=list()
s=set()
for item in l:
    res = (item['name'], item['age'], item['sex'])
    if res not in s:
        s.add(res)
        l_new.append(item)


print(l_new)


#了解：不可变集合
fset=frozenset({1,2,3})
fset.