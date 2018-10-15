

#导入包实际上就是在导入包下面的__init__.py文件


import sys

sys.path.append(r'/Volumes/docker/Py/py/函数递归_模块与包/7. 包的使用/xxx')
'''
import aaa

#aaa.m1.f1()


aaa.f1()
aaa.f2()






# aaa.bbb.m3.f3()
aaa.f3()
aaa.f4()
'''


##前提是使用者必须对这个包的目录结构特别了解
'''

from aaa.ccc.m4 import f4

f4()

'''



##
import aaa.ccc.m4
aaa.ccc.m4.f4()