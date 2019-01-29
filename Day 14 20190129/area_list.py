c = {
    'p1': {'c1': ['d1', 'd2', 'd3'], 'c2': ['d4', 'd5', 'd6']},
    'p2': {'c3': ['d7', 'd8', 'd9'], 'c4': ['d10', 'd11', 'd12']}
}

exit_flag = False
p_exit_flag = False
c_exit_flag = False
d_exit_flag = False
t_exit_flag = False
l_exit_flag = False

while not exit_flag:
    choice = input('请问您是要查看还是修改地域字典，查看请输入r，修改请输入w，退出请输入q：')
    if choice == 'r':
        if len(c) > 0:
            while not p_exit_flag:

                s_province = '省列表'  # 此处打印省列表
                print(s_province.center(50, '-'))
                for i in c.keys():
                    print(i)
                print(s_province.center(50, '-'))

                choice_p = input('请问您要查看哪个省的列表？(#号键返回上级菜单)')  # 此处询问客户后续操作

                while not c_exit_flag:
                    if choice_p in c.keys():

                        s_city = '%s省城市列表' % choice_p  # 此处打印用户选择的省的城市清单
                        print(s_city.center(50, '-'))
                        for i in c[choice_p].keys():
                            print(i)
                        print(s_city.center(50, '-'))

                        choice_c = input('请问您要查看哪个市的列表？(#号键返回上级菜单)')  # 此处询问客户后续操作

                        while not d_exit_flag:
                            if choice_c in c[choice_p].keys():

                                s_district = '%s省%s市列表' % (choice_p, choice_c)  # 此处打印用户选择的省的城市的区清单
                                print(s_district.center(50, '-'))
                                for i in c[choice_p].keys():
                                    print(i)
                                print(s_district.center(50, '-'))

                                choice_d = input('请问您要查看哪个区的列表？(#号键返回上级菜单)')  # 此处询问客户后续操作

                                while not t_exit_flag:
                                    if choice_d in c[choice_p][choice_c]:

                                        s_town = '%s省%s市%s区列表' % (choice_p, choice_c, choice_d)  # 此处打印用户选择的省的城市的区的镇清单
                                        print(s_town.center(50, '-'))
                                        for i in c[choice_p][choice_c]:
                                            print(i)
                                        print(s_town.center(50, '-'))

                                        choice_d = input('按#号键返回上级菜单，按q键返回至初始菜单')  # 此处询问客户后续操作

                                        while not l_exit_flag:
                                            if choice_d == '#':
                                                l_exit_flag = True
                                            elif choice_d == 'q':
                                                print('返回初始菜单成功！')
                                                p_exit_flag = True
                                            else:
                                                print('输入有误，请重新输入，返回上级菜单请输入#号,按q键返回至初始菜单')
                                    elif choice_p == '#':
                                        d_exit_flag = True
                                    else:
                                        print('输入有误，请重新输入，返回上级菜单请输入#号')
                            elif choice_p == '#':
                                c_exit_flag = True
                            else:
                                print('输入有误，请重新输入，返回上级菜单请输入#号')

                        elif choice_p == '#':
                            p_exit_flag = True
                        else:
                            print('输入有误，请重新输入，返回上级菜单请输入#号')

        else:
            print('对不起，当前地域字典为空，请先添加后再查看')
    elif choice == 'w':
        print()
    elif choice == 'q':
        print('退出成功')
        exit_flag = True
    else:
        print('对不起，您输入的操作代码有误，请重新输入')
