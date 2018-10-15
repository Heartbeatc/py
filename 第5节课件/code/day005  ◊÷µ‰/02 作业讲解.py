# li = ["alex", "WuSir", "ritian", "barry", "wenzhou", "eric"]
#
# l2=[1,"a",3,4,"heart"]
# # print(len(li))
# # li.append("seven")
# li.extend(l2)
# li.remove(li[2])
# li.pop(2)
# print(li)

# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# # ["c"]
# print(li[-1:])

# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# lis[3][2][1][0] = "TT"
# lis[3][2][1][0] = lis[3][2][1][0].replace("t", "T")
# lis[3][2][1][0] = lis[3][2][1][0].swapcase()

# lis[3][2][1][1] = "100"
# lis[3][2][1][1] = str(lis[3][2][1][1] + 97)

# lis[3][2][1][2] = int(lis[3][2][1][2] + "01")
# lis[3][2][1][2] = 101
# lis[3][2][1][2] = int(lis[3][2][1][2]) + 100


# print(lis)



# li = ["alex", "eric", "rain", "刘伟","你很六"]
# # 1+2+3+4+5....
# s = ""
# for el in li:  # el 列表中的每一个字符串
#     s = s + el + "_"
# print(s[:-1])

#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)

# lst = []
# for i in range(50):
#     if i % 3 == 0:
#         lst.append(i)
#
# print(lst)

# for i in range(100, 0, -1):
#     print(i)

# lst = []
# for i in range(100, 9, -1):
#     if i % 2 == 0 and i % 4 == 0:
#         lst.append(i)
# print(lst)

# lst = []
# for i in range(1, 30):
#     lst.append(i)
#
# for i in range(len(lst)):
#     if lst[i] % 3 == 0:
#         lst[i] = "*"
# print(lst)


# 查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并
# 以"c"结尾的所有元素，并添加到⼀个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "ale xC", "AbC ", "egon", " ri TiAn", "WuSir", " aqc"]
#
# lst = []
# for el in li:
#     el = el.replace(" ", "")  # 去掉空格的
#     if el.upper().startswith("A") and el.endswith("c"):
#         lst.append(el)
# print(lst)


# 敏感词列表 li = ["苍⽼师", "东京热", "武藤兰", "波多野结⾐"]
# 则将⽤户输⼊的内容中的敏感词汇替换成等⻓度的*（苍⽼师就替换***），并添
# 加到⼀个列表中；如果⽤户输⼊的内容没有敏感词汇，则直接添加到上述的列
# 表中。
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# content = input("请开始你的评论:")
# for el in li:
#     if el in content:
#         content = content.replace(el, "*"*len(el))
# print(content)

# print(list)
# print(type([]))

# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn", [3, 7, 8, "TaiBai"]]
# for el in li:
#     if type(el) == list:
#         for el2 in el:
#             if type(el2) == str:
#                 print(el2.lower())
#             else:
#                 print(el2)
#     else:
#         if type(el) == str:
#             print(el.lower())
#         else:
#             print(el)

# for i in range(len(li)):
#     if i != 4:
#         print(li[i])
#     else: # 第四个是列表. 继续循环
#         for el in li[4]:
#             print(el)


# lst = []
# while 1:
#     info = input("请输入学生信息(Q退出):")  # 张三_44
#     if info.upper() == "Q":
#         break
#     lst.append(info)
# sum = 0
# for el in lst:  # 张三_44
#     sum += int(el.split("_")[1])
#
# print(sum/len(lst))

# 敲七
# n = int(input("请输入数字n:"))
# lst = []
# for i in range(1, n+1):
#     if i % 7 == 0 or "7" in str(i):
#         lst.append("咣")
#     else:
#         lst.append(i)
# print(lst)

