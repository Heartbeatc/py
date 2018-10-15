'''




critical=50
error=40
warning=30
info=20
debug=10
notset=0

'''


'''


import logging  #默认的日志级别是warning ,默认的的输出目标是：终端



logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')


'''



##控制日志打印到文件中，并且自己定制日志的输出格式
import logging


logging.basicConfig(
    filename='access.log',
    #filemode='w', 默认是'a'模式
    #format 指定日志输出格式
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=10
)


logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')



##待解决的问题
#1：既往终端打印，又往文件中打印
#2：控制输出不同目标（终端+文件）的日志，有各自的配置信息





 





