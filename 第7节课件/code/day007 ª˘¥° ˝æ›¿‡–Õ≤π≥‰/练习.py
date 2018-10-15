
cars = ["鲁A 10086", "黑A 45678", "黑C 12345", "京B 00001", "京C 78912", "京A 66666"]
locations = {"鲁": "山东", "黑": "黑龙江", "京": "北京", "沪": "上海"}
dic = {}

# for car in cars:
#     paitou = car[0]
#     if dic.get(locations[paitou]) == None:
#
#         dic[locations[paitou]] = 1
#     else:
#         dic[locations[paitou]] = dic[locations[paitou]] + 1


print(len(cars))

for i in cars:
    paitou = i[0]  # 鲁 == paitou
    # 山东 locations[鲁] 取到的是字典里面的key为鲁，取到的值为山东，此时需要定义一个新的字典
    # num = dic.get(locations[paitou],0)
    # num = num + 1
    # dic[locations[paitou]] = num
    dic[locations[paitou]] = dic.get(locations[paitou], 0) + 1


print(dic)
