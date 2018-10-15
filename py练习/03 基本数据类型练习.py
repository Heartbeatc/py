


#1.有变 name = " aleX leNb" 完成如下操作:



# name = "alex leNb"
#
# print(name)
# print(name.strip(" "))
#
#
#
# print(name.lstrip("al"))
# print(name.rstrip('Nb'))
# print(name.lstrip('a').rstrip('b'))
# print(name.startswith('a'))
# print(name.endswith('b'))
#
# print(name.replace('l','p',1))
# print(name.split('l',1))
# print(name.upper())
# print(name.lower())
# print(name.swapcase())
# print(name.title())
# print(name.count('l'))
# print(name.find('l',4))

lst = []


while 1:
    name = input('请输入员工信息')
    if name.upper() == 'Q':
        print(lst)
        break
    else:
        lst.append(name)

##testd