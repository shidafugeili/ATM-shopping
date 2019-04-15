from interface import user,bank,shop
from lib.common import auto_login

user_info={'name':None}
def register():
    while True:
        name=input('请输入注册用户：').strip()
        pwd= input('请输入用户密码：').strip()
        flag,msg=user.register_interface(name,pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)

def login():
    if user_info['name']:
        print('用户%s已经登录'%user_info['name'])
    else:
        while True:
            name=input('请输入登录用户：').strip()
            pwd= input('请输入用户密码：').strip()
            flag,msg=user.login_interface(name,pwd)
            if flag:
                print(msg)
                user_info['name']=name
                break
            else:
                print(msg)
@auto_login
def lookyue():
    res=user.get_balance_interface(user_info['name'])
    print(res)

@auto_login
def tixian():
    while True:
        money=input('请输入提现金额：').strip()
        money=int(money)
        flag,msg=bank.tixian_interface(user_info['name'],money)
        if flag:
            print(msg)
            break
        else:
            print(msg)
@auto_login
def zhuanzhang():
    while True:
        to_user=input('请输入转账用户：').strip()
        to_money = input('请输入转账金额：').strip()
        to_money=int(to_money)
        if to_user==user_info['name']:
            print('不能转账给同一个用户')
        else:
            flag,msg=bank.zhuanzhang_interface(user_info['name'],to_user,to_money)
            if flag:
                print(msg)
                break
            else:
                print(msg)

@auto_login
def huankuan():
    money = input('请输入还款金额：').strip()
    money=int(money)
    res=bank.huankuan_interface(user_info['name'],money)
    print(res)
@auto_login
def look_flow():
    res=bank.flow_interface(user_info['name'])
    print(res)
@auto_login
def shopping():
    goods_list=[
        ['凤爪', 50],
        ['T-shirt', 150],
        ['macbook', 21800],
        ['iphoneX', 7000]
    ]
    cost=0
    shopping_cart={}
    user_yue=user.get_balance_interface(user_info['name'])
    while True:
        for index,goods in enumerate(goods_list):
            print(index,goods)
        choice=input('请选择商品编号：').strip()
        if choice.isdigit():
            choice=int(choice)
            if choice>=0 and choice<len(goods_list):
                good_name,good_price=goods_list[choice]
                if user_yue<good_price:
                    print('该商品价格高于余额，请重新选择')
                else:
                    if good_name in shopping_cart:
                        shopping_cart[good_name]+=1
                    else:
                        shopping_cart[good_name]=1
                    cost+=good_price
                    shop.add_shopping_cart_interface(user_info['name'],shopping_cart)
            else:
                print('请输入编号以内的数字')
        elif choice=='q':
            if cost==0:
                print('取消购物')
                break
            else:
                confirm=input('请确认是否结束购物去支付Y/N:')
                if confirm=='Y':
                    msg=bank.pay_shopping_cart_interface(user_info['name'],cost)
                    print(msg)
                    break
        else:
            print('请正确输入')

@auto_login
def look_shopping_cart():
    res=shop.show_shopping_cart_interface(user_info['name'])
    print(res)

@auto_login
def logout():
    print('用户%s已经注销'%user_info['name'])
    user_info['name']=None

func={
'1':register,
'2':login,
'3':lookyue,
'4':tixian,
'5':zhuanzhang,
'6':huankuan,
'7':look_flow,
'8':shopping,
'9':look_shopping_cart,
'0':logout,
}
def run():
    while True:
        print('''
1 注册
2 登录
3 查看余额
4 提现
5 转账
6 还款
7 查看流水
8 购物
9 查看购物车
0 注销
Q 退出        
        ''')
        choice=input('请输入功能编号：')
        if choice in func:
            func[choice]()
        elif choice=='Q':
            break
        else:
            print('请正确输入编号')