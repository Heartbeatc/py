 # user={'name':'egon','pwd':'123'}
# with open('db.txt','w',encoding='utf-8') as f:
#     f.write(str(user))

# with open('db.txt','r',encoding='utf-8') as f:
#     data=f.read()
#     print(data)


import json
# user={'name':'egon','pwd':'123','age':18}
# with open('db.json','w',encoding='utf-8') as f:
#     f.write(json.dumps(user))


# with open('db.json','r',encoding='utf-8') as f:
#     data=f.read()
#     dic=json.loads(data)
#     print(dic['egon'])


user={'name':'egon','pwd':'123','age':18}
l=[1,2,3,'a']
json.dump(user,open('db.json','w',encoding='utf-8'))



# dic=json.load(open('db1.json','r',encoding='utf-8'))
# print(dic,type(dic),dic['name'])

