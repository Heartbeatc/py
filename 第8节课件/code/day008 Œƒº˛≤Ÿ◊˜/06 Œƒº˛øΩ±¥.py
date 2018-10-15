f1 = open("d:/linux学院-桌面背景.jpg", mode="rb")
f2 = open("E:/刘伟自拍.jpg", mode="wb")
for line in f1:
    f2.write(line)
f1.close()
f2.flush()
f2.close()