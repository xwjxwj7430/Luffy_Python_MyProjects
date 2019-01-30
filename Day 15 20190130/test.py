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

exit_flag = False

while not exit_flag:
    choice_level_1 = input('欢迎来到国家省市区街道公司查询系统，按任意键开始查询，退出请输q：')
    if choice_level_1 == 'q':
        exit_flag = True

    else:
        while not exit_flag:
            s_p = '区域列表'
            print(s_p.center(50, '-'))
            for index, i in enumerate(menu.keys()):
                print('%s. %s' % (index, i))
            print(s_p.center(50, '-'))

            choice_province = input('输入区域名称查看下属地方列表；返回上级请输b，退出请输q：')
            if choice_province == 'q':
                exit_flag = True
            elif choice_province == 'b':
                break
            elif choice_province in menu.keys():
                if len(menu[choice_province]) == 0:
                    print('对不起，当前区域名称下没有子列表，请重新输入，谢谢！')
                else:
                    while not exit_flag:
                        s_c = '%s下属地方列表' % choice_province
                        print(s_c.center(50, '-'))
                        for index, i in enumerate(menu[choice_province].keys()):
                            print('%s. %s' % (index, i))
                        print(s_c.center(50, '-'))

                        choice_city = input('输入地方名称查看下属街道列表；返回上级请输b，退出请输q：')
                        if choice_city == 'q':
                            exit_flag = True
                        elif choice_city == 'b':
                            break
                        elif choice_city in menu[choice_province].keys():
                            if len(menu[choice_province][choice_city]) == 0:
                                print('对不起，当前地方名称下没有子列表，请重新输入，谢谢！')
                            else:
                                while not exit_flag:
                                    s_d = '%s%s下属街道列表' % (choice_province, choice_city)
                                    print(s_d.center(50, '-'))
                                    for index, i in enumerate(menu[choice_province][choice_city]):
                                        print('%s. %s' % (index, i))
                                    print(s_d.center(50, '-'))

                                    choice_district = input('输入街道名称查看下属公司列表；返回上级请输b，退出请输q：')
                                    if choice_district == 'q':
                                        exit_flag = True
                                    elif choice_district == 'b':
                                        break
                                    elif choice_district in menu[choice_province][choice_city]:
                                        if len(menu[choice_province][choice_city][choice_district]) == 0:
                                            print('对不起，当前街道名称下没有子列表，请重新输入，谢谢！')
                                        else:
                                            s_l = '%s%s%s公司列表' % (choice_province, choice_city, choice_district)
                                            print(s_l.center(50, '-'))
                                            for index, i in enumerate(menu[choice_province][choice_city][choice_district]):
                                                print('%s. %s' % (index, i))
                                            print(s_l.center(50, '-'))

                                            choice_company = input('已到达最小级公司列表；返回上级请输b，退出请输q：')
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
