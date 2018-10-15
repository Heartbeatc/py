dic = {"汪峰": "大陆音乐半壁江山", "周杰伦": "亚洲音乐天王", "罗志祥": "亚洲舞王"}

# 对字典的遍历
# print(dic.keys())   # dict_keys(['汪峰', '周杰伦', '罗志祥']) 像列表但不是列表
# for key in dic.keys():
#     print(key)  # 拿到key
#     print(dic[key]) # 拿到value

# print(dic.values())
# for value in dic.values():
#     print(value)


# 也可以遍历字典
# [('汪峰', '大陆音乐半壁江山'), ('周杰伦', '亚洲音乐天王'), ('罗志祥', '亚洲舞王')]
# print(dic.items())  # 拿到的是key和value
for k, v in dic.items(): # 当需要遍历字典. 在操作中涉及到key和value的时候.
    print(k) # 元组
    print(v)


# 字典本身是一个可迭代对象,可以直接进行for循环
for el in dic:  # 直接拿到key
    print(el)
    print(dic[el])

# 前面的变量的个数和后面解包的个数一致
# a, b = (10, 20) # 解构, 解包
# print(a)
# print(b)

