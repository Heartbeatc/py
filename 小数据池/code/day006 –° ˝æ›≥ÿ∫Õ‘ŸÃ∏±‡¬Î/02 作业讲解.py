# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# tu[1][2]['k2'].append("seven")  # 周四左右就有了
# print(tu)

av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}


''',给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个  元素：'量很大'。
    b,将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
    c,在此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表中添加"金老板最喜欢这个"。
    d,将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
e,给'大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
f,删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对。
g,给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'''
# av_catalog['欧美']['www.youporn.com'].insert(1, "量很大")
# av_catalog['欧美']['x-art.com'].pop(1)
# av_catalog['欧美']['x-art.com'].append("金老板最喜欢这个")
# av_catalog['日韩']['tokyo-hot'][1] = av_catalog['日韩']['tokyo-hot'][1].upper()
# av_catalog['大陆']['1048'] = ['一天就封了']
# av_catalog['欧美'].pop("letmedothistoyou.com")
# av_catalog['大陆']['1024'].insert(1, "可以爬下来")
# print(av_catalog)



# "k:1|k1:2|k2:3|k3:4"  => {'k':'1', 'k1':'2'...}

# s = "k:1|k1:2|k2:3|k3:4"
# dic = {}
# lst = s.split("|")
# for el in lst:
#     a, b = el.split(":") # 确定切出来的结果是两项
#     dic[a] = b
# print(dic)

#
# # li= [11,22,33,44,55,66,77,88,99,90]
# li= [11,22,33,44,55,66,77,88,99,90]
# result = {}
# for el in li:
#     pass
#     # if el < 66:
#     #     # setdefault可以帮我们执行新增, 如果key存在了就不新增了
#     #     # {'key1':[11,22]}
#     #     result.setdefault("key1", []).append(el)
#     # else:
#     #     result.setdefault("key2", []).append(el)
#
#
#     # if el < 66: # 11, 22
#     #     if result.get("key1") == None:
#     #         result["key1"] = [el] # 11
#     #     else:
#     #         result['key1'].append(el)
#     # else:
#     #     if result.get("key2") == None:
#     #         result["key2"] = [el] # 11
#     #     else:
#     #         result['key2'].append(el)
#
#
# print(result)

goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}, ]
# for el in goods:
for i in range(len(goods)):
    print(i+1, goods[i]['name'], goods[i]['price'])

while 1:
    content = input("请输入你要购买的商品序号:")
    if content.upper() == 'Q':
        print("程序退出中........")
        break
    if content.isdigit():
        content = int(content)-1
        if content >= 0 and content < len(goods):
            print(goods[content]['name'], goods[content]['price'])
        else:
            print("超过了商品的范围")
    else:
        print("不合法")

