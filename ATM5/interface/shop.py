from db import db_handler
from lib.common import get_logger
logger2=get_logger('shop')

def add_shopping_cart_interface(name,shopping_cart):
    user_dic = db_handler.select(name)
    user_dic['shopping_cart']=shopping_cart
    logger2.info('购物车添加商品成功')
    db_handler.save(user_dic)
def show_shopping_cart_interface(name):
    user_dic=db_handler.select(name)
    return user_dic['shopping_cart']






