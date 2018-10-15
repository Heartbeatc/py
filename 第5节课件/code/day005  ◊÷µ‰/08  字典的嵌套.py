wf = {
    "name": "汪峰",
    "age": 48,
    "成名曲": "春天里",
    "wife": {
        "name": "章子怡",
        "age": 39,
        "工作": "演员"
    },
    "children":[
        {"num": "001", "name": "汪一", "hobby": "唱歌"},
        {"num": "002", "name": "汪二", "hobby": "演戏"} # wf['children'][1]['name']
    ]
}

wf['wife']['age'] = wf['wife']['age'] + 10
print(wf)


