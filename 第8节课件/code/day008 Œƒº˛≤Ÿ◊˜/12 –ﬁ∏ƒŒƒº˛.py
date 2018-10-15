import os # 引入os模块

with open("alex", mode="r", encoding="utf-8") as f1, \
     open("alex_副本", mode="w", encoding="utf-8") as f2:

    for line in f1:
        new_line = line.replace("good", "sb")
        f2.write(new_line)

os.remove("alex")
os.rename("alex_副本", "alex")
