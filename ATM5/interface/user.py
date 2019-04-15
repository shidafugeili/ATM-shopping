from db import db_handler


def register_interface(name,pwd):
    user_dic=db_handler.select(name)
    if user_dic:
        return False,'该用户已经注册'
    else:
        user_dic={'name':name,'pwd':pwd,'balance':15000,'flow':[],'shopping_cart':{}}
        db_handler.save(user_dic)
        return True,'用户%s注册成功'%name

def login_interface(name,pwd):
    user_dic=db_handler.select(name)
    if not user_dic:
        return False,'该用户尚未注册'
    else:
        if user_dic['pwd']!=pwd:
            return False,'用户密码错误'
        else:
            return True,'登录成功'

def get_balance_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['balance']