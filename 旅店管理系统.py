# 旅店管理系统
#manager = {'张三':111,'李四':222}
ordinary_customer_dict = {'张三' : 300, '李四' : 400}
#member_customer_dict = {'王五' : 800, '赵六' : 600}
#空房间
space_room_list = ['201','202','203','204','205']
filled_room_list = []

def input_0():
    output = "再见,祝您一路顺风,欢迎下次光临."
    print(output)
    return
def get_1():
    print(f'空闲房间有{space_room_list}')
    get = input()
    if get == '0':
        input_0()
    if get == '1':
        get_1()
    if get == '2':
        get_2()
    if get == '3':
        get_3()
    if get == '4':
        get_4()
    if get == '5':
        get_5()
    else:

        get = input()
def get_2():
    wanted_room = input("请输入您要订的房间:")
    require_day = int(input("请输入您需要居住的天数:"))
    price = require_day * 100
    print(f"需支付{price}元.")
    if price > ordinary_customer_dict[name]:
        get = input("余额不足,请前往充值后再订房:\n")
        if get == '0':
            input_0()
        if get == '1':
            get_1()
        if get == '2':
            get_2()
        if get == '3':
            get_3()
        if get == '4':
            get_4()
        if get == '5':
            get_5()
        else:

            get = input()

    else:
        ordinary_customer_dict[name] -= price
        print(f'支付成功,入住愉快.卡内余额:{ordinary_customer_dict[name]} 元')
        filled_room_list.append(wanted_room)
        space_room_list.remove(wanted_room)
        get = input()
        if get == '0':
            input_0()
        if get == '1':
            get_1()
        if get == '2':
            get_2()
        if get == '3':
            get_3()
        if get == '4':
            get_4()
        if get == '5':
            get_5()
        else:
            get = input()
def get_3():
    check_out_room = input("请输入您要退掉的房间:")
    filled_room_list.remove(check_out_room)
    space_room_list.append(check_out_room)
    print("退房成功.")
    get = input()
    if get == '0':
        input_0()
    if get == '1':
        get_1()
    if get == '2':
        get_2()
    if get == '3':
        get_3()
    if get == '4':
        get_4()
    if get == '5':
        get_5()
    else:
        get = input()
def get_4():
    store = int(input("请输入您要充值的金额:"))
    ordinary_customer_dict[name] += store
    print(f'充值成功,余额:{ordinary_customer_dict[name]} 元.')
    get = input()
    if get == '0':
        input_0()
    if get == '1':
        get_1()
    if get == '2':
        get_2()
    if get == '3':
        get_3()
    if get == '4':
        get_4()
    if get == '5':
        get_5()
    else:
        get = input()
def get_5():
    print(f'卡内余额:{ordinary_customer_dict[name]} 元')
    get = input()
    if get == '0':
        input_0()
    if get == '1':
        get_1()
    if get == '2':
        get_2()
    if get == '3':
        get_3()
    if get == '4':
        get_4()
    if get == '5':
        get_5()
    else:
        get = input()
welcome = "欢迎来到旅店管理系统"
print(welcome.center(50, '*'))
print("1登录".center(50, '-'))
print("2注册".center(50, '-'))
print("0退出".center(50, '-'))
print("*" * 50)
_input = input("请输入操作数:")

if _input == '0':
    input_0()
if _input == '1':
    name = input("登录账号:")
    if name in ordinary_customer_dict:
        print(f"登录成功\n" + "*" * 50)
        # if name in manager:
        #     print("亲爱的管理员{name},您额外有增删房号的权利,增删房号请按+/-:")
        print(f"客户:{name}       余额:{ordinary_customer_dict[name]}        会员状态:未开通")
        print("1查询空闲房间".center(50, '-'))
        print("2开房".center(50, '-'))
        print("3退房".center(50, '-'))
        print("4充值".center(50, '-'))
        print("5查询余额".center(50, '-'))
        get = input("请输入操作数:")
        if get == '0':
            input_0()
        if get == '1':
            get_1()
        if get == '2':
            get_2()
        if get == '3':
            get_3()
        if get == '4':
            get_4()
        if get == '5':
            get_5()
        else:
            get = input()
    else:
        print("您未注册,请重新选择:")
        _input = input()
if _input == '2':
    name = input("设置账号名称:")
    ordinary_customer_dict[name] = 0
    print(ordinary_customer_dict)
    print(f"注册成功,已为您自动登录.\n" + "*" * 50)
    print(f"客户:{name}       余额:{ordinary_customer_dict[name]}        会员状态:未开通")
    print("1查询空闲房间".center(50, '-'))
    print("2开房".center(50, '-'))
    print("3退房".center(50, '-'))
    print("4充值".center(50, '-'))
    get = input("请输入操作数:")
    if get == '1':
        get_1()
    if get == '2':
        get_2()
    if get == '3':
        get_3()
    if get == '4':
        get_4()













