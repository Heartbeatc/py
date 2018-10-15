# dic = {}
# # 徐峥：人在囧途
# dic['徐峥'] = "人在囧途" # 直接用key往里面存数据即可
# dic['黄渤'] = "疯狂的石头"
# dic["王宝强"] = "天下无贼"
# dic["王宝强"] = "士兵突击" # 如果key已经存在。 那么会替换掉原来的value, 修改
#
# dic.setdefault("黄秋生")
# dic.setdefault("黄秋生", "无间道")    # 如果存在了key， 不会执行新增
#
# print(dic)




dic = {}

dic['cuijianzhong'] = 'jianzhong'


print(dic['cuijianzhong'])
dic.setdefault('jianzhong','cui')
print(dic)
