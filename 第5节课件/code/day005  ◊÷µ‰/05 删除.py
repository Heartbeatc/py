dic = {"黄日华": "天龙八部", "吕颂贤": "笑傲江湖", "苏有朋": "倚天屠龙记", "六小龄童": "西游记"}
# dic.pop("吕颂贤") # 指定key删除
# dic.popitem()  # 随机删除
# del dic["黄日华"]  # 删除
# dic.clear() # 清空字典

print(dic)

dic.pop('六小龄童')
dic.popitem()
dic.clear()

print(dic)