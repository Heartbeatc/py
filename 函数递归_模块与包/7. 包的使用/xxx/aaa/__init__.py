# print('=====init=====')
# x=111
#
# from aaa import m1




#点的左边必须是包，from....import后必须是一个明确的名字，不能带点
# from aaa.m1 import f1
#
# from aaa.m2 import f2
#
#
#
# from aaa import bbb
#
#
# from .bbb.m3 import f3
# from aaa.ccc.m4 import f4



from .m1 import f1
from .m2 import f2
from . import bbb
from .bbb.m3 import f3
from .ccc.m4 import f4


