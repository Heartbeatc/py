f = open("d:/sylar.txt", mode="w", encoding="utf-8")
f.write("周笔畅\n") # 写的时候. 先清空. 再写入. w
f.write("胡辣汤\n")
f.write("实付款\n")

f.flush()
f.close()