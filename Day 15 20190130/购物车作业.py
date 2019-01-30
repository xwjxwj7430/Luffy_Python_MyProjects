goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

print('欢迎来到天上人间网上购物中心！')

# username = input('请输入您的用户名：')
# password = input('请输入您的密码：')
#
salary = int(input('请输入您的工资（单位：元）：'))
exit_flag = False
balance = salary
shopping_cart = []
buy_history = []
total_price = 0

while not exit_flag:
    s_list = '商品列表'
    print(s_list.center(50, '-'))
    for index, i in enumerate(goods):
        print('%s. %s %s元' % (index, i['name'], i['price']))
    print(s_list.center(50, '-'))

    item_buy = input('请输入您想要购买的商品编号（输入c查看购物车并结账，输入q退出）： ')
    if item_buy == 'q':
        exit_flag = True
    elif item_buy.isdigit():
        item_buy = int(item_buy)
        if item_buy < len(goods):
            shopping_cart.append(item_buy)
            print('商品%s已经添加到购物车啦！' % goods[item_buy]['name'])
        else:
            print('对不起，商品不存在，请重新输入，谢谢！')
    elif item_buy == 'c':
        if len(shopping_cart) == 0:
            print('对不起，当前购物车为空，请先添加商品，谢谢！')
            continue
        else:
            s_shopping_cart_list = '购物车商品清单'
            print(s_shopping_cart_list.center(50, '-'))
            for index, i in enumerate(shopping_cart, start=1):
                print('%s. %s %s元' % (index, goods[i]['name'], goods[i]['price']))
                total_price += goods[i]['price']
            print(s_shopping_cart_list.center(50, '-'))
            print('共计%s元' % total_price)
            print('您当前的可用余额为%s' % balance)

        decision = input('请问您是否现在结账？结账请输y，退出请输q，否则继续购物： ')
        if decision == 'y' or 'Y':
            if balance >= total_price:
                balance -= total_price
                buy_history.extend(shopping_cart)
                print('购物车所有商品扣款成功，您的商品即将进入物流，请耐心等待，谢谢您的支持！')
                exit_flag = True
            else:
                print('对不起，您的余额不足，请充值后再试！')
        elif decision == 'q':
            exit_flag = True
        else:
            continue
    else:
        print('对不起，商品编号有误，请重新输入，谢谢！')

s_buy_list = '已购买的商品清单'
print(s_buy_list.center(50, '-'))
if len(buy_history) == 0:
    s_n = '无'
    print(s_n.center(58, ' '))
else:
    for index, i in enumerate(buy_history, start=1):
        print('%s. %s %s元' % (index, goods[i]['name'], goods[i]['price']))
print(s_buy_list.center(50, '-'))
print('您的余额为%s元' % balance)
