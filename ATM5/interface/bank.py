from db import db_handler
from lib.common import get_logger
logger1=get_logger('bank')


def tixian_interface(name,money):
    user_dic=db_handler.select(name)
    money1=money*1.05
    money2=money*0.05
    if user_dic['balance']<money1:
        return False,'余额不足，提现失败'
    else:
        user_dic['balance']-=money1
        info='用户%s提现%s成功,手续费%s元'%(name,money,money2)
        logger1.info(info)
        user_dic['flow'].append(info)
        db_handler.save(user_dic)
        return True,info


def huankuan_interface(name,money):
    user_dic = db_handler.select(name)
    user_dic['balance']=+money
    info='用户%s还款%s成功'%(name,money)
    logger1.info(info)
    user_dic['flow'].append(info)
    db_handler.save(user_dic)
    return info

def zhuanzhang_interface(name,to_user,to_money):
    user_dic = db_handler.select(name)
    to_user_dic = db_handler.select(to_user)
    if not to_user_dic:
        return False,'转账用户%s不存在'%to_user
    else:
        if user_dic['balance']<to_money:
            return False,'转账金额比余额大，转账失败'
        else:
            user_dic['balance']-=to_money
            to_user_dic['balance']+=to_money
            info='用户%s转账%s元给用户%s成功'%(name,to_money,to_user)
            logger1.info(info)
            user_dic['flow'].append(info)
            db_handler.save(user_dic)
            db_handler.save(to_user_dic)
            return True,info

def flow_interface(name):
    user_dic=db_handler.select(name)
    return user_dic['flow']

def pay_shopping_cart_interface(name,cost):
    user_dic=db_handler.select(name)
    if user_dic['balance']<cost:
        return '您的余额不足，支付失败'
    else:
        user_dic['balance']-=cost
        info='用户%s购物支付%s元成功'%(name,cost)
        logger1.info(info)
        db_handler.save(user_dic)
        return info

