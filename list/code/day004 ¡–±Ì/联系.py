#1，

# 写代码，有如下 表，按照要求实现每 个功能


'''



# li = ["alex", "WuSir", "ritian", "barry", "wenzhou","eric"]
#1)计算 表的 度并输出
#print(len(li))

#2) 表中追加元素"seven",并输出添加后的列表
# li.append("seven")
# print(li)


#3)请在 表的第1个位置插 元素"Tony",并输出添加后的列表

# li.insert(1,"Tony")
# print(li)

#4)请修改 表第2个位置的元素为"Kelly",并输出修改后的

# li[2] = "Kelly"
# print(li)


#5)请将 表l2=[1,"a",3,4,"heart"]的每 个元素添加到列表li中，一行代码实现，不允许循环添加。

# l2=[1,"a",3,4,"heart"]
#
# li.extend(l2)
# print(li)

#6)请将字符 s = "qwert"的每 个元素添加到列表li中，一行代码实现，不允许循环添加。


# s = "qwert"
#
# li.extend(s)
# print(li)


#7)请删除列表中的元素"eric",并输出添加后的列表

# li.remove("eric")
# print(li)

#8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表

# for i in li:
#     if i == li[2]:
#         li.pop(2)
#         print(i)
#         print(li)


# deleted = li.pop(2)
# print(deleted)
# print(li)


#9)请删除 表中的第2 4个元素，并输出删除元素后的列表

# print(li[2:4])
# del li[2:4]
#
# print(li)


#10)请将列表所有得元素反转，并输出反转后的列表

# li.reverse()
# print(li)


#11)请计算出"alex"元素在 表li中出现的次数，并输出该次数。

# print(li.count('alex'))



'''




#2，写代码，有如下 表，  切 实现每 个功能



# li = [1, 3, 2, "a", 4, "b", 5,"c"]
#
#
# l1 = li[:3]
# print(l1)
#
#
# l2 = li[3:6]
# print(l2)
#
#
#
# l3 = li[::2]
# print(l3)
#
#
# l4 = li[1:6:2]
# print(l4)
#
#
# l5 = li[-1:]
# print(l5)
#
# l6 = li[-3::-2]
# print(l6)
#
#
#
#
# li=['alex', 'eric', 'rain']
# print("_".join(li))
# print(li[0]+"_"+li[1]+"_"+li[2])
#
#
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
#
#
# for i in range(len(li)):
#     print(i,li[i])
#
#
#
#
# lst = []
# for i in range(100, 9, -1):
#     if i % 2 == 0 and i % 4 == 0:
#         lst.append(i)
# print(lst)



##倒序打印100-1
# for i in range(100,0,-1):
#     print(i)


#
# l = []
#
#
# for i in range(50):
#     if i % 3 == 0:
#         l.append(i)
#
#
# print(l)


#
# for i in range(1,30):
#     l.append(i)
#
#
#
# for i in range(len(l)):
#     if l[i]  % 3 == 0:
#         l[i] = '*'
# print(l)




# 查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并
# 以"c"结尾的所有元素，并添加到⼀个新列表中,最后循环打印这个新列表。


# li = ["TaiBai ", "ale xC", "AbC ", "egon", " ri TiAn", "WuSir", " aqc"]
#
# l2 = []
#
# for i in li:
#     i = i.replace(" ","")
#     if i.upper().startswith('A') and i.endswith('c'):
#         l2.append(i)
#
#
# print(l2    )


# 敏感词列表 li = ["苍⽼师", "东京热", "武藤兰", "波多野结⾐"]
# 则将⽤户输⼊的内容中的敏感词汇替换成等⻓度的*（苍⽼师就替换***），并添
# 加到⼀个列表中；如果⽤户输⼊的内容没有敏感词汇，则直接添加到上述的列
# 表中。


#
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣",'sb','你妈b']
#
# content = input("请输入评论的内容")
#
# for i in li:
#     if i in content:
#         content = content.replace(i, "*"*len(i))
# print(content)


# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
#
# for i in li:
#     if type(i) == list:
#         for le in i:
#             print(le)
#     else:
#         print(i)


#用函数的递归递归调用
# def get(l):
#     for item in l:
#         if isinstance(item,list):
#             get(item)
#         else:
#             print(item)
#
#
#
# get(li)