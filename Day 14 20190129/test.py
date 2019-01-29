c = {
    'p1': {'c1': ['d1', 'd2', 'd3'], 'c2': ['d4', 'd5', 'd6']},
    'p2': {'c3': ['d7', 'd8', 'd9'], 'c4': ['d10', 'd11', 'd12']}
}

exit_flag = False


while not exit_flag:
    choice_level_1 = input('欢迎来到国家省市区查询系统，按任意键开始查询，退出请输q：')
    if choice_level_1 == 'q':
        print('系统已退出')
        exit_flag = True

    else:
        if len(c) == 0:
            choice_level_2 = input('对不起，当前查询系统数据为空，请您添加后查询，输入任意字符开始添加，退出请输q: ')
            if choice_level_2 == 'q':
                print('系统已退出')
                exit_flag = True
            else:
                while True:
                    province_add = input('请您添加省份名称(如果已经添加完毕，请按q返回初始菜单):  ')
                    if province_add == 'q':
                        break
                    else:
                        add_confirm = input('您想要添加的省份名称为：%s，确认请输1，重新输入请输2' % province_add)
                        if add_confirm == '1':
                            if province_add not in c.keys():
                                c[province_add] = {}
                                print('%s添加成功！' % province_add)
                            else:
                                print('对不起，您要添加的省份已经在系统数据中，请勿重复添加，谢谢！')
                        elif add_confirm == '2':
                            continue
                        else:
                            print('输入有误，请重新输入')

        else:
            while True:
                s_p = '省份列表'
                print(s_p.center(50, '-'))
                if len(c) == 0:
                    s_n = '无'
                    print(s_n.center(50, ' '))
                else:
                    for index, i in enumerate(c.keys()):
                        print('%s. %s' % (index, i))
                print(s_p.center(50, '-'))

                choice_level_3 = input('输入a：增加；输入d：删除；输入e：修改；输入n：进入城市子列表；退出请输q：')
                if choice_level_3 == 'a':
                    while True:
                        province_add = input('请输入新增省份名称（退回上级请输q)： ')
                        if province_add == 'q':
                            break
                        else:
                            add_confirm = input('您想要添加的省份名称为：%s，确认请输1，重新输入请输2' % province_add)
                            if add_confirm == '1':
                                if province_add not in c.keys():
                                    c[province_add] = {}
                                    print('%s添加成功！' % province_add)
                                else:
                                    print('对不起，您要添加的省份已经在系统数据中，请勿重复添加，谢谢！')
                            elif add_confirm == '2':
                                continue
                            else:
                                print('输入有误，请重新输入')
                                continue

                elif choice_level_3 == 'd':
                    while True:
                        province_del = input('请输入删除省份名称（退回上级请输q)： ')
                        if province_del == 'q':
                            break
                        else:
                            del_confirm = input('您想要删除的省份名称为：%s，确认请输1，重新输入请输2' % province_del)
                            if del_confirm == '1':
                                if province_del in c.keys():
                                    c.pop(province_del)
                                    print('%s删除成功！' % province_del)
                                else:
                                    print('对不起，您要删除的省份不在系统数据中，请重新输入，谢谢！')
                            elif del_confirm == '2':
                                continue
                            else:
                                print('输入有误，请重新输入')
                                continue

                elif choice_level_3 == 'e':
                    while True:
                        province_edit = input('请输入要修改的省份名称（退回上级请输q)： ')
                        if province_edit == 'q':
                            break
                        else:
                            province_new = input('请输入修改后的省份名称为：')
                            edit_confirm = input('您想要将省份%s的名称变更为%s，确认请输1，重新输入请输2' % (province_edit, province_new))
                            if edit_confirm == '1':
                                if province_edit in c.keys():
                                    c.pop(province_edit)
                                    print('修改成功！%s的名字已经变为%s' % (province_edit, province_new))
                                else:
                                    print('对不起，您要修改的省份不在系统数据中，请重新输入谢谢！')
                            elif edit_confirm == '2':
                                continue
                            else:
                                print('输入有误，请重新输入')
                                continue

                elif choice_level_3 == 'n':
                    while True:
                        choice_province = input('请您输入省份名称，输入成功后进入该省份的城市子列表（退出请输q）：')
                        if choice_province == 'q':
                            break
                        elif choice_province in c.keys():
                            print()
                        else:
                            print('对不起，您输入的省份名称不存在，请重新输入')
                            continue

                elif choice_level_3 == 'q':
                    break

                else:
                    print('对不起，您所输入的操作不存在，请重新输入，谢谢！')

