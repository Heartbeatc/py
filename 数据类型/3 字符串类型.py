#用途：名字，性别，地址
name='egon' #name=str('egon')
# print(id(name),type(name),name)


#优先掌握的操作：
# 按索引取值(正向取+反向取) ：只能取
# print(name[0],type(name[0]))
# print(name[-2])
# name[0]='E'

# 切片(顾头不顾尾，步长)
# print(name[1:3])
# msg='hello world'
# print(msg[1:7])
# print(msg[1:7:2])

# msg='abcdefg' #bdf
# # print(msg[1:6:2])
# # print(msg[::2])
# print(msg[6::-1]) #了解

# 长度len
# msg='ab c '
# print(len(msg))

# 成员运算in和not in
# msg='hello alex'
# print('a' in msg)
# print('alex' in msg)
# print('ae' not in msg)


# 移除空白strip
# password='   alex3714              '
# password=password.strip()
# print(password)
# print(password.strip())

# msg='***egon***********'
# print(msg.strip('*'))

# msg='***eg**on***********'
# print(msg.strip('*'))

# 切分split
user_info='root:x:0:0::/root:/bin/bash'
# print(user_info[0:4])
# print(user_info.split(':')[0])
# print(user_info.split(':',1))

# cmd='put       a.txt'
# print(cmd.split())

# filepath='put /a/b/c/d/a.txt'
# print(filepath.split())

#
# msg='alex say i have on tesla'
# print(msg.split(maxsplit=1)[0])


#isdigit:用来判断字符是否是由纯数字组成（bytes，unicode）


# 循环






#常用操作

# msg='***alex****'
# print(msg.strip('*'))
# print(msg.lstrip('*'))
# print(msg.rstrip('*'))

# msg='alex_SB'
# print(msg.startswith('alex'))
# print(msg.endswith('SB'))


# msg='alex say i have one telsa, my name is alex'
# print(msg.replace('alex','SB',1))


# print('my name is %s my age is %s' %('egon',18))
# print('my name is {} my age is {}'.format('egon',18))
# print('{1} {0} {1}'.format('egon',18))

# print('my name is {x} my age is {y}'.format(y=18,x='egon'))


#split
# user_info='root:x:0:0::asdfasdf'
# l=user_info.split(':')

#join
#
# print(':'.join(l))
# print(''.join(l))
# print(' '.join(l))


#center,ljust,rjust,zerofill
#=================egon===================
# print('egon'.center(30,'='))
# print('egon'.rjust(30,'='))
# print('egon'.ljust(30,'='))
# print('egon'.zfill(30))



#了解部分
#find,rfind,index,rindex,count
# msg='hello world'
# print(msg.find('ell'))#从左到右找，如果有，则返回第一个字符的索引
# print(msg.find('easdfasdf'))#从左到右找，如果没有，返回-1

# print(msg.index('d',0,3))#从左到右找，如果有，则返回第一个字符的索引
# print(msg.index('x'))#从左到右找，如果有，则返回第一个字符的索引
#
# print(msg.count('l',0,4))
# print(msg.count('l',0,3))


# msg='abc\tdeft'
# print(msg.expandtabs(3))


# msg='alex Say hello'
# print(msg.capitalize())
# print(msg.upper())
# print(msg.lower())
# print(msg.title())
# print(msg.swapcase())


#is系列
# msg='Alex Say Hello'
# print(msg.isupper())
# print(msg.islower())
# print(msg.istitle())

#
# msg='asasdf123'
# print(msg.isalnum()) #字符串是由字母或数字组成
msg='asdfasdf'
print(msg.isalpha())

#
# msg='   1'
# print(msg.isspace())
# msg='aaaai fabc'
# print(msg.isidentifier())


#判断数字
# age=10
# inp=input('>>: ').strip()
# if inp.isdigit():
#     inp=int(inp)
#     if inp > age:
#         print('ok')
#
# else:
#     print('必须输入数字')

num1=b'4' #bytes
num2=u'4' #unicode,python3中无需加u就是unicode
num3='四' #中文数字
num4='壹'
num5='Ⅳ' #罗马数字


#bytes,unicode
# print(num1.isdigit())
# print(num2.isdigit())
# print(num3.isdigit())
# print(num4.isdigit())
# print(num5.isdigit())

#unicode
# print(num2.isdecimal())
# print(num3.isdecimal())
# print(num4.isdecimal())
# print(num5.isdecimal())


#unicode,汉字，罗马
# print(num2.isnumeric())
# print(num3.isnumeric())
# print(num4.isnumeric())
# print(num5.isnumeric())