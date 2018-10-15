'''
1. ASCII: 8bit 1byte 英文字母 数字 特殊字符.
2. GBK: 16bit 2byte 主要是存中文。日文， 韩文, 繁字体。 中文的特殊字符  中国 (abcd)
3. UNICODE: 32bit 4byte
4. UTF-8: 可变长度的unicode
    英文： 8bit， 1byte
    欧洲文字：16bit, 2byte
    中文: 24bit, 3byte  (abcd)
GBK和UTF-8不能直接互换
转码
'''
# 在python2里面. 默认的编码是ASCII
# 在python3中unicode是可以使用的。 默认用的就是Unicode. 代码用utf-8来存储

#  如果用unicode存储, 如果用utf-8
# s = "你好啊"   # 看到的就是unicode
# print(s)

# 1. 编码. 把unicode转换成utf-8
# s = "刘伟很皮" # 12个字节
# abc = s.encode("UTF-8")  # encode之后的结果是bytes类型  依然是原来的字符串
# print(abc)  # b'数据'

# 解码
# abc = b'\xe5\x88\x98\xe4\xbc\x9f\xe5\xbe\x88\xe7\x9a\xaf'
# s = abc.decode("UTF-8") # 解码。 用什么编码， 就用什么解码
# print(s)

# s = "赵瑞鑫"
# print(s.encode("GBK"))
# bs = b'\xd5\xd4\xc8\xf0\xf6\xce'
# print(bs.decode("GBK")) # GBK的编码不能用UTF-8解码

# GBK的编码. 把这句话变成UTF-8
# bs = b'\xd5\xd4\xc8\xf0\xf6\xce'
# # 先解码
# s = bs.decode("GBK")
# # 重新编码
# bs2 = s.encode("UTF-8")
# print(bs2)
