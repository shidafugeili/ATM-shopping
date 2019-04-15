import os
import sys
BASE_PATH=os.path.dirname(os.path.dirname(__file__))
DB_PATH=os.path.join(BASE_PATH,'db')
standard_format = '[%(asctime)s][task:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

# id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
fh1_path = os.path.join(BASE_PATH,'log','atm_shop_log.log')


LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'ch': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'fh1': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': fh1_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        # 'fh2': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
        #     'formatter': 'simple',
        #     'filename': fh2_path,  # 日志文件
        #     'maxBytes': 1024*1024*5,  # 日志大小 5M
        #     'backupCount': 5,
        #     'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        # },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['ch', 'fh1',],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            # 'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}