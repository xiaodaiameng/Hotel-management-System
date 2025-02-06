### 一 .前言

话不多说.

我就说几句吧.

第三句是:各位前辈我献丑了,经过一学期,我硬生生地感悟到....[^感悟]

### 二.任务列表

- [x] 代码编写与测试
- [ ] 代码准确性
- [x] 提交正确性

### 三.代码

注意! 代码待替换!         这是不及格的,功能待修理的代码,仅用于查看md去仓库后的视图

```python
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
def get_2():
    wanted_room = input("请输入您要订的房间:")
    require_day = int(input("请输入您需要居住的天数:"))
    price = require_day * 100
    print(f"需支付{price}元.")
    if price > ordinary_customer_dict[name]:
        get = input("余额不足,请前往充值后再订房:\n")
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
        ordinary_customer_dict[name] -= price
        print(f'支付成功,入住愉快.卡内余额:{ordinary_customer_dict[name]} 元')
        filled_room_list.append(wanted_room)
        space_room_list.remove(wanted_room)
        get = input()
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
def get_3():
    check_out_room = input("请输入您要退掉的房间:")
    filled_room_list.remove(check_out_room)
    space_room_list.append(check_out_room)
    print("退房成功.")
    get = input()
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
def get_4():
    store = int(input("请输入您要充值的金额:"))
    ordinary_customer_dict[name] += store
    print(f'充值成功,余额:{ordinary_customer_dict[name]} 元.')
    get = input()
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
        input_0()
def get_5():
    print(f'卡内余额:{ordinary_customer_dict[name]} 元')
    get = input()
    if get == '1':
        get_1()
    if get == '2':
        get_2()
    if get == '3':
        get_3()
    if get == '4':
        get_4()

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
    print("5查询余额".center(50, '-'))
    get = input("请输入操作数:")
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
```

### 四.碎碎段

每次看自己写的代码就觉得非常愚蠢,请各位息怒 :cry:

<img src="https://www.wxbqb.com/res/2022/10-28/07/5788be0d97db5fb8aa739dd85fa1aba9.jpg" alt="小狗" style="zoom:30%;" align = "left" />

[^感悟]:看到大家各有所长,敲的代码和问的问题都让我崇拜与迷惑,我发现自己的能力远远不够.为了让自己不要徒生焦虑,按自己的进度学习,我退群了,现在状态好了一点,这个爪哇部落教会了我很多,我既对自己的水平感到恐惧,又在尽力平静心情认真地一点一点学下去,我一心期待加入,希望能继续收到你们的考核题.请求:能否将以后的考核发送给我的邮箱,如果可以的话,万分感谢:aaaaa1_2024@qq.com

