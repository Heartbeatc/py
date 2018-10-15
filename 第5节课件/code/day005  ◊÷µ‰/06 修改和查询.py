# dic = {"刘能": "王小利", "赵四": "刘晓光", "王木生": "范伟", "谢大脚": "于月仙", "李大国": "小鬼"}
# # dic['王木生'] = "刘伟"
# dic2 = {"刘能": "大阳哥", "赵四": "github", "王木生": "汪峰", "谢大脚": "冯提莫", "王大拿": "金老板"}
# dic.update(dic2)
# print(dic)
#
# # 查询
# dic = {'刘能': '大阳哥', '赵四': 'github', '王木生': '汪峰', '谢大脚': '冯提莫', '李大国': '小鬼', '王大拿': '金老板'}
# # 1. 最直观。 直接用key
# print(dic['周杰伦'])  # 当这个key不存在的时候会报错
# # 2. get方法
# print(dic.get("谢大脚", "周杰伦不在这里"))  # 没有key. 返回None
# # 3. setdefault()  1. 新增(先看有没有key， 如果有就过， 如果没有，执行新增) 2.根据key把值返回
# dic = {}
# dic["盖伦"] = "德玛西亚之力"
# value = dic.setdefault("菲奥娜", "无双剑姬")  # 新增
# value2 = dic.setdefault("盖伦", "刘伟")  # 由于已经存在了key。 所以新增不执行。 直接查询结果
# value3 = dic.setdefault("薇恩", "坑")
#
# print(value3)
# print(dic)


dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}

# for i in dic:
#     print(i,dic[i])



# dic['k1'] = 'alex'
# print(dic)


for key, value in dic.items(): # ?? 这个是解构
    print(key, value)



