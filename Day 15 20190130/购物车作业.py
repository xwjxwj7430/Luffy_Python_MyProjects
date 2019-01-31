#  不知道如何读写文件，所以在此仅列举作为功能示例

#  user_info为储存用户登录名和密码的数据文件，用于后续登录验证
user_info = {'alex': 'password1',
             'eric': 'password2',
             'nick': 'password3',
             'john': 'password4'
             }

#  user_history为储存用户购买商品记录的数据文件，用户在最开始可以选择是否查看以往消费记录；
#  另外程序最后检测：如果用户名存在于user_info中，则为客户记录购买过的商品
user_history = {'alex': [0, 1, 2],
                'eric': [1, 3],
                'nick': [2],
                'john': []
                }

#  user_info为储存用户上一次购物之后的余额情况的数据文件，用于后续消费金额的扣除等运算
user_balance = {'alex': 5000,
                'eric': 100,
                'nick': 0,
                'john': 90000
                }

#  good为在售商品列表
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

#  设定初始程序终止标识符exit_flag与用户消费余额为0
exit_flag = False
balance = 0

while not exit_flag:
    print('\033[7m 欢迎来到天上人间网上购物中心！\033[0m')  # 欢迎界面

    while not exit_flag:
        username = input('请输入您的用户名（输入q退出）：')  # 用户输入用户名，准备进行比对
        if username == 'q':
            exit_flag = True
        else:
            password = input('请输入您的密码：')
            if username in user_info.keys():  # 如果用户已存在，则验证密码
                if password == user_info[username]:  # 密码验证成功
                    print('\033[7m 登陆成功！欢迎%s的归来！\033[0m' % username)  # 打印欢迎消息
                    print('\033[7m 您的余额为%s元\033[0m' % user_balance[username])  # 打印余额信息
                    balance = user_balance[username]  # 读取余额信息，作为此次消费的承继基数
                    check_history = input('请问您是否要查看以往购物记录？（输入y查看，否则继续）')  # 询问是否需要查看以往购物记录
                    if check_history == 'y':  # 读取user_history中的数据并打印
                        s_shopping_history = '曾经购买的商品清单'
                        print(s_shopping_history.center(50, '-'))
                        for index, i in enumerate(user_history[username]):
                            print('%s. %s %s元' % (index, goods[i]['name'], goods[i]['price']))
                        print(s_shopping_history.center(50, '-'))
                        break  # 跳出登陆循环
                    else:
                        break
                else:
                    print('\033[7m 用户名或密码错误，请重新输入！\033[0m')  # 密码错误，重新输入
            else:  # 如果用户不存在，询问是否注册
                add_choice = input(
                    '系统检测到这是您第一次登陆天上人间，请问要向本系统添加您的信息，以便下次光临吗？（输入y添加，否则不添加）')  # 询问是否添加并允许记录余额、消费记录等信息
                if add_choice == 'y':  # 允许添加，则将用户名、密码对添加到user_info，初始化user_history为空和user_balance为0
                    print('\033[7m 谢谢您，系统添加成功！快去购物吧！\033[0m')
                    user_info[username] = password
                    user_history[username] = []
                    user_balance[username] = balance
                    break  # 跳出登陆循环
                else:
                    print('\033[7m 很遗憾，那下次再添加吧，先去购物吧！\033[0m')
                    break  # 跳出登陆循环
    while not exit_flag:
        salary = input('请输入您的工资（单位：元）输入q退出：')  # 用户输入此次工资收入，加上上次余额，总和即为此次可消费最大金额

        if salary.isdigit():
            salary = int(salary)
            balance += salary  # 计算此次可消费的最大金额
            shopping_cart = []  # 初始化购物车
            buy_success = []  # 初始化购买成功的商品清单
            total_price = 0  # 初始化此次购物车中商品总价
            print('\033[7m您当前的可用余额为%s\033[0m' % balance)  # 高亮提醒客户当前总可消费金额

            while not exit_flag:
                s_list = '商品列表'  # 打印在售商品清单
                print(s_list.center(50, '-'))
                for index, i in enumerate(goods):
                    print('%s. %s %s元' % (index, i['name'], i['price']))
                print(s_list.center(50, '-'))

                item_buy = input('请输入您想要购买的商品编号（输入c查看购物车并结账，输入q退出）： ')  # 询问客户决定
                if item_buy == 'q':
                    exit_flag = True
                elif item_buy.isdigit():  # 如果客户成功输入一个数字
                    item_buy = int(item_buy)
                    if item_buy < len(goods):  # 并且该商品在在售列表之中
                        shopping_cart.append(item_buy)  # 添加至购物车
                        print('\033[7m 商品 %s 已经添加到购物车啦！\033[0m' % goods[item_buy]['name'])  # 添加购物车成功提示
                    else:
                        print('对不起，商品不存在，请重新输入，谢谢！')  # 提示客户重新输入在售范围内的有效商品编号
                elif item_buy == 'c':  # 如果客户选择查看购物车清单
                    if len(shopping_cart) == 0:  # 如果当前购物车无商品，提示用户先添加商品再查看
                        print('\033[7m 对不起，当前购物车为空，请先添加商品，谢谢！ \033[0m')
                    else:
                        s_shopping_cart_list = '购物车商品清单'  # 如果当前购物车不为空，打印购物车清单
                        print(s_shopping_cart_list.center(50, '-'))
                        for index, i in enumerate(shopping_cart, start=1):
                            print('%s. %s %s元' % (index, goods[i]['name'], goods[i]['price']))
                            total_price += goods[i]['price']
                        print(s_shopping_cart_list.center(50, '-'))
                        print('\033[7m 共计%s元 \033[0m' % total_price)  # 打印购物车清单总价
                        print('\033[7m您当前的可用余额为%s\033[0m' % balance)  # 再次提示客户可用余额，方便比对

                        decision = input('请问您是否现在结账？结账请输y，退出请输q，否则继续购物： ')  # 询问客户是否结账
                        if decision == 'y':  # 如结账，则计算当前余额是否足够，不够则提示，够则扣款，并提示扣款成功信息
                            if balance >= total_price:
                                balance -= total_price
                                buy_success.extend(shopping_cart)
                                print('\033[7m 购物车所有商品扣款成功，您的商品即将进入物流，请耐心等待，谢谢您的支持！ \033[0m')
                                exit_flag = True  # 成功扣款，退出程序，此次购买完毕
                            else:
                                print('\033[7m 对不起，您的余额不足，请充值后再试！（系统即将为您跳回至购物界面） \033[0m')  # 余额不足，提示充值，并返回购物界面
                        elif decision == 'q':
                            exit_flag = True
                        else:
                            pass
                else:
                    print('对不起，商品编号有误，请重新输入，谢谢！')  # 输入的商品编号为非数字，也不是退出q，提示出错，重新输入

            s_buy_list = '已购买的商品清单'  # 最后打印已购买商品清单，如空，则打印‘无’，否则正常打印
            print(s_buy_list.center(50, '-'))
            if len(buy_success) == 0:
                s_n = '无'
                print(s_n.center(58, ' '))
            else:
                for index, i in enumerate(buy_success, start=1):  # 正常打印
                    print('%s. %s %s元' % (index, goods[i]['name'], goods[i]['price']))
                if username in user_info:  # 如果客户是已存在用户，将购买记录的列表和余额数字存储至相应数据文件
                    user_history[username].extend(buy_success)
                    user_balance[username] = balance
            print(s_buy_list.center(50, '-'))
            print('\033[7m 您的余额为%s元 \033[0m' % balance)  # 最后打印此次购买结束后的余额情况

        elif salary == 'q':
            exit_flag = True
        else:
            print('对不起，工资输入有误，请重新输入，谢谢！')  # 工资为非数字，提示报错

print('系统已退出')
print('期待您再度光临！')
