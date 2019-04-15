from core import src

from conf import settings
import logging.config

def auto_login(fn):
    def inner(*args,**kwargs):
        if src.user_info['name']:
            res=fn(*args,**kwargs)
            return res
        else:
            src.login()
    return inner
def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    return logging.getLogger(name)