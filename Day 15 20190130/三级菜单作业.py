menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

exit_flag = False  # 这个exit_flag是用于后面在任意一级菜单输入q都能退出的功能flag

while not exit_flag:
    choice_level_1 = input('欢迎来到国家省市区街道公司查询系统，按任意键开始查询，退出请输q：')  # 系统初始欢迎界面
    if choice_level_1 == 'q':
        exit_flag = True

    else:
        while not exit_flag:
            s_p = '区域列表'  # 首先打印一级菜单，即区域列表
            print(s_p.center(50, '-'))
            for index, i in enumerate(menu.keys()):
                print('%s. %s' % (index, i))
            print(s_p.center(50, '-'))

            choice_province = input('输入区域名称查看下属地方列表；返回上级请输b，退出请输q：')  # 让客户输入指令，确认下一步操作
            if choice_province == 'q':
                exit_flag = True
            elif choice_province == 'b':
                break
            elif choice_province in menu.keys():  # 如果客户输入的名称在一级菜单中，则进入二级菜单
                if len(menu[choice_province]) == 0:  # 但如果该名称的二级菜单为空，则仍旧保持在当前一级菜单不变
                    print('对不起，当前区域名称下没有子列表，请重新输入，谢谢！')
                else:  # 二级菜单不为空，则跳入二级菜单
                    while not exit_flag:
                        s_c = '%s下属地方列表' % choice_province  # 打印二级菜单
                        print(s_c.center(50, '-'))
                        for index, i in enumerate(menu[choice_province].keys()):
                            print('%s. %s' % (index, i))
                        print(s_c.center(50, '-'))

                        choice_city = input('输入地方名称查看下属街道列表；返回上级请输b，退出请输q：')  # 让客户输入指令，确认下一步操作
                        if choice_city == 'q':
                            exit_flag = True
                        elif choice_city == 'b':
                            break
                        elif choice_city in menu[choice_province].keys():  # 如果客户输入的名称在二级菜单中，则进入三级菜单
                            if len(menu[choice_province][choice_city]) == 0:  # 但如果该名称的三级菜单为空，则仍旧保持在当前二级菜单不变
                                print('对不起，当前地方名称下没有子列表，请重新输入，谢谢！')
                            else:
                                while not exit_flag:  # 打印三级菜单
                                    s_d = '%s%s下属街道列表' % (choice_province, choice_city)
                                    print(s_d.center(50, '-'))
                                    for index, i in enumerate(menu[choice_province][choice_city]):
                                        print('%s. %s' % (index, i))
                                    print(s_d.center(50, '-'))

                                    choice_district = input('输入街道名称查看下属公司列表；返回上级请输b，退出请输q：')  # 让客户输入指令，确认下一步操作
                                    if choice_district == 'q':
                                        exit_flag = True
                                    elif choice_district == 'b':
                                        break
                                    elif choice_district in menu[choice_province][
                                        choice_city]:  # 如果客户输入的名称在三级菜单中，则进入四级菜单
                                        if len(menu[choice_province][choice_city][
                                                   choice_district]) == 0:  # 但如果该名称的四级菜单为空，则仍旧保持在当前三级菜单不变
                                            print('对不起，当前街道名称下没有子列表，请重新输入，谢谢！')
                                        else:  # 打印四级菜单
                                            s_l = '%s%s%s公司列表' % (choice_province, choice_city, choice_district)
                                            print(s_l.center(50, '-'))
                                            for index, i in enumerate(
                                                    menu[choice_province][choice_city][choice_district]):
                                                print('%s. %s' % (index, i))
                                            print(s_l.center(50, '-'))

                                            choice_company = input(
                                                '已到达最小级公司列表；返回上级请输b，退出请输q：')  # 提示客户已到最底层菜单，客户输入指令，确认下一步操作
                                            if choice_district == 'q':
                                                exit_flag = True
                                            elif choice_district == 'b':
                                                break
                                            else:
                                                print('对不起，您所输入的操作不存在，请重新输入，谢谢！')

                        else:
                            print('对不起，您输入的操作不存在，请重新输入')
            else:
                print('对不起，您输入的操作不存在，请重新输入')

print('系统已退出')
