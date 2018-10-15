#spam.py
print('from the spam.py')

money=1000

def read1():
    print('spam模块：',money)

def read2():
    print('spam模块')
    read1()

def change():
    global money
    money=0




#print(__name__)  #文件当作脚本执行，该值等于 __main__，文件spam.py 当作文件导入时，改值等于spam
if __name__ == '__main__':
    read1()
    read2()
    change()



#main
