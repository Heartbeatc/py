lst = ["汪峰", "吴君如", "李嘉欣", "陈慧琳", "关之琳"]
# 遍历列表. 把列表中的每一项用"_" 做拼接
s = "_".join(lst) # 把列表转化成字符串
print(s)


s1 = "汪峰_吴君如_李嘉欣_陈慧琳_关之琳"
ls = s1.split("_") # 把字符串转化成列表
print(ls)

print("*".join("马化腾"))




import sys


print(sys.version)
