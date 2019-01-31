# userdata.txt中的字典数据结构如下：
# 第一个key值为用户名，用户名下面的子字典的password存储密码，history存储购买记录，balance存储上次购买后的余额
#
# f = open('userdata.txt', 'w', encoding='utf-8')
# user_info = {'alex': {'password': ['shuai'], 'history': [0, 1, 0, 3], 'balance': 5000},
#              'eric': {'password': ['ge'], 'history': [0, 1], 'balance': 50},
#              'john': {'password': ['jiu'], 'history': [0], 'balance': 0},
#              'nick': {'password': ['shi'], 'history': [], 'balance': 0},
#              }
# f.write(str(user_info))
# f.close()

# goodslist.txt中的字典数据结构如下：
# f = open('goodslist.txt', 'w', encoding='utf-8')
#
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
# ]
#
# f.write(str(goods))
# f.close()


# 购物车正式开始，首先是欢迎界面和登录环节
# ---------------------------------------------------------------------------------------------------------------------
print('\033[7m 欢迎来到天上人间网上购物中心！\033[0m')  # 欢迎界面

f = open('userdata.txt', 'r', encoding='utf-8')  # 打开、读取存储用户名密码的userdata文件，给变量user_data赋值，用于登录验证
user_data = eval(f.read())
f.close()

f = open('goodslist.txt', 'r', encoding='utf-8')  # 打开、读取存储商品列表的goodslist文件，给变量goods赋值，用于展示商品列表和购物
goods = eval(f.read())
f.close()

while True:
    username = input('请输入您的用户名（输入q退出）：').strip()  # 用户输入用户名
    if not username:  # 用户名为空，则停在此循环
        continue
    if username == 'q':  # 输入q退出
        exit('程序已退出\n欢迎下次光临！')
    if username in user_data():  # 如果用户已存在，则验证密码，新用户则提示是否注册，见后面
        password = input('请输入您的密码：').strip()
        if password == user_data[username]:  # 密码验证成功
            print('\033[7m 登陆成功！欢迎%s的归来！\033[0m' % username)  # 打印欢迎消息
            print('\033[7m 您的余额为%s元\033[0m' % user_data[username]['balance'])  # 打印余额信息
            balance = user_data[username]['balance']  # 读取余额信息，作为此次消费的承继基数，用作后续计算
            check_history = input('请问您是否要查看以往购物记录？（输入y查看，否则继续）').strip()  # 询问是否需要查看以往购物记录
            if check_history == 'y':  # 读取user_history中的数据并打印
                s_shopping_history = '曾经购买的商品清单'
                print(s_shopping_history.center(50, '-'))
                for index, i in enumerate(user_data[username]['history']):
                    print('%s. %s %s元' % (index, goods[i]['name'], goods[i]['price']))
                print(s_shopping_history.center(50, '-'))
                break  # 跳出登陆循环
            else:  # 不打印历史记录，跳出登录循环，准备购物
                break
        else:
            print('\033[7m 用户名或密码错误，请重新输入！\033[0m')  # 密码错误，重新输入

    else:  # 新用户提示是否注册
        add_choice = input(
            '系统检测到这是您第一次登陆天上人间，请问要向本系统添加您的信息，以便下次光临吗？（输入y添加，否则不添加）')  # 询问是否添加并允许记录余额、消费记录等信息
        if add_choice == 'y':  # 允许添加，让客户输入密码，存储用户名密码对，打印提示信息，进入购物
            print('您即将添加的用户名：%s' % username)
            password = input('请设置您的密码：').strip()
            print('\033[7m 谢谢您，系统添加成功！快去购物吧！\033[0m')
            user_data[username] = {}  # 添加用户名
            user_data[username]['password'] = password  # 添加用户名下的密码子字典
            user_data[username]['history'] = []  # 添加用户名下的购物记录子字典
            user_data[username]['balance'] = []  # 添加用户名下的余额记录子字典
            break  # 跳出登陆循环
        else:
            print('\033[7m 很遗憾，那下次再添加吧，先去购物吧！\033[0m')
            break  # 跳出登陆循环

# --------------------------此处开始登录环节就结束了，下面开始购物环节----------------------------------------------------















