c = {

}

exit_flag = False

while not exit_flag:
    choice_level_1 = input('欢迎来到国家省市区查询系统，按任意键开始查询，退出请输q：')
    if choice_level_1 == 'q':
        print('系统已退出')
        exit_flag = True

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

            choice_level_3 = input('输入a：增加；输入d：删除；输入e：修改；输入n：查看某省城市子列表；返回上级请输q：')
            if choice_level_3 == 'a':
                while True:
                    province_add = input('请输入新增省份名称（返回上级请输q)： ')
                    if province_add == 'q':
                        break
                    elif province_add not in c.keys():
                        add_confirm = input('您想要添加的省份名称为：%s，确认请输1，重新输入请输2' % province_add)
                        if add_confirm == '1':
                            c[province_add] = {}
                            print('%s添加成功！' % province_add)
                        elif add_confirm == '2':
                            pass
                        else:
                            print('输入有误，请重新输入')
                    else:
                        print('对不起，您要添加的省份已经在系统数据中，请勿重复添加，谢谢！')
            elif choice_level_3 == 'd':
                while True:
                    province_del = input('请输入删除省份名称（返回上级请输q)： ')
                    if province_del == 'q':
                        break
                    elif province_del in c.keys():
                        del_confirm = input('您想要删除的省份名称为：%s，确认请输1，重新输入请输2' % province_del)
                        if del_confirm == '1':
                            c.pop(province_del)
                            print('%s删除成功！' % province_del)
                        elif del_confirm == '2':
                            pass
                        else:
                            print('输入有误，请重新输入')
                    else:
                        print('对不起，您要删除的省份不在系统数据中，请重新输入，谢谢！')
            elif choice_level_3 == 'e':
                while True:
                    province_edit = input('请输入要修改的省份名称（返回上级请输q)： ')
                    if province_edit == 'q':
                        break
                    elif province_edit in c.keys():
                        province_new = input('请输入修改后的省份名称为：')
                        if province_new == province_edit:
                            print('对不起，新名称不能与旧名称相同，请重新输入')
                        elif province_new in c.keys():
                            print('对不起，您的修改后的新名称在省份数据库中已存在，请重新输入，谢谢')
                        else:
                            edit_confirm = input('您想要将省份%s的名称变更为%s，确认请输1，重新输入请输2' % (province_edit, province_new))
                            if edit_confirm == '1':
                                c[province_new] = c.pop(province_edit)
                                print('修改成功！%s的名字已经变为%s' % (province_edit, province_new))
                            elif edit_confirm == '2':
                                pass
                            else:
                                print('输入有误，请重新输入')
                    else:
                        print('对不起，您要修改的省份不在系统数据中，请重新输入谢谢！')
            elif choice_level_3 == 'n':
                if len(c) == 0:
                    print('当前数据库为空，请先添加后查看，谢谢！')
                else:
                    while True:
                        choice_province = input('请输入您想要查看的省份名称，输入成功后进入该省份的城市子列表（返回请输q）：')
                        if choice_province == 'q':
                            break
                        elif choice_province in c.keys():
                            while True:
                                s_c = '%s省城市列表' % choice_province
                                print(s_c.center(50, '-'))
                                if len(c[choice_province]) == 0:
                                    s_n = '无'
                                    print(s_n.center(50, ' '))
                                else:
                                    for index, i in enumerate(c[choice_province].keys()):
                                        print('%s. %s' % (index, i))
                                print(s_c.center(50, '-'))

                                choice_level_4 = input('输入a：增加；输入d：删除；输入e：修改；输入n：查看某市区级子列表；返回上级请输q：')
                                if choice_level_4 == 'a':
                                    while True:
                                        city_add = input('请输入新增城市名称（返回上级请输q)： ')
                                        if city_add == 'q':
                                            break
                                        elif city_add not in c[choice_province].keys():
                                            add_confirm = input('您想要添加的城市名称为：%s，确认请输1，重新输入请输2' % city_add)
                                            if add_confirm == '1':
                                                c[choice_province][city_add] = {}
                                                print('%s添加成功！' % city_add)
                                            elif add_confirm == '2':
                                                pass
                                            else:
                                                print('输入有误，请重新输入')
                                        else:
                                            print('对不起，您要添加的城市已经在系统数据中，请勿重复添加，谢谢！')
                                elif choice_level_4 == 'd':
                                    while True:
                                        city_del = input('请输入删除城市名称（返回上级请输q)： ')
                                        if city_del == 'q':
                                            break
                                        elif city_del in c[choice_province].keys():
                                            del_confirm = input('您想要删除的城市名称为：%s，确认请输1，重新输入请输2' % city_del)
                                            if del_confirm == '1':
                                                c[choice_province].pop(city_del)
                                                print('%s删除成功！' % city_del)
                                            elif del_confirm == '2':
                                                pass
                                            else:
                                                print('输入有误，请重新输入')
                                        else:
                                            print('对不起，您要删除的城市不在系统数据中，请重新输入，谢谢！')

                                elif choice_level_4 == 'e':
                                    while True:
                                        city_edit = input('请输入要修改的城市名称（返回上级请输q)： ')
                                        if city_edit == 'q':
                                            break
                                        elif city_edit in c[choice_province].keys():
                                            city_new = input('请输入修改后的城市名称为：')
                                            if city_new == city_edit:
                                                print('对不起，新名称不能与旧名称相同，请重新输入')
                                            elif city_new in c[choice_province].keys():
                                                print('对不起，新名称在%s省城市数据库中已存在，请重新输入，谢谢' % choice_province)
                                            else:
                                                edit_confirm = input(
                                                    '您想要将城市%s的名称变更为%s，确认请输1，重新输入请输2' % (city_edit, city_new))
                                                if edit_confirm == '1':
                                                    c[choice_province][city_new] = c[choice_province].pop(city_edit)
                                                    print('修改成功！%s的名字已经变为%s' % (city_edit, city_new))
                                                elif edit_confirm == '2':
                                                    pass
                                                else:
                                                    print('输入有误，请重新输入')
                                        else:
                                            print('对不起，您要修改的城市不在系统数据中，请重新输入谢谢！')

                                elif choice_level_4 == 'n':
                                    if len(c[choice_province]) == 0:
                                        print('当前数据库为空，请先添加后查看，谢谢！')
                                    else:
                                        while True:
                                            choice_city = input('请您输入城市名称，输入成功后进入该城市区级子列表（返回上级请输q）：')
                                            if choice_city == 'q':
                                                break
                                            elif choice_city in c[choice_province].keys():
                                                while True:
                                                    s_d = '%s省%s市区级列表' % (choice_province, choice_city)
                                                    print(s_d.center(50, '-'))
                                                    if len(c[choice_province][choice_city]) == 0:
                                                        s_n = '无'
                                                        print(s_n.center(50, ' '))
                                                    else:
                                                        for index, i in enumerate(c[choice_province][choice_city]):
                                                            print('%s. %s' % (index, i))
                                                    print(s_d.center(50, '-'))

                                                    choice_level_5 = input('输入a：增加；输入d：删除；输入e：修改；返回上级请输q：')
                                                    if choice_level_5 == 'a':
                                                        while True:
                                                            district_add = input('请输入新增区级名称（返回上级请输q)： ')
                                                            if district_add == 'q':
                                                                break
                                                            elif district_add not in c[choice_province][choice_city]:
                                                                add_confirm = input(
                                                                    '您想要添加的区级名称为：%s，确认请输1，重新输入请输2' % district_add)
                                                                if add_confirm == '1':
                                                                    c[choice_province][choice_city][district_add] = {}
                                                                    print('%s添加成功！' % district_add)
                                                                elif add_confirm == '2':
                                                                    pass
                                                                else:
                                                                    print('输入有误，请重新输入')
                                                            else:
                                                                print('对不起，您要添加的区级名称已经在系统数据中，请勿重复添加，谢谢！')

                                                    elif choice_level_5 == 'd':
                                                        while True:
                                                            district_del = input('请输入删除区级名称（返回上级请输q)： ')
                                                            if district_del == 'q':
                                                                break
                                                            elif district_del in c[choice_province][choice_city]:
                                                                del_confirm = input(
                                                                    '您想要删除的区级名称为：%s，确认请输1，重新输入请输2' % district_del)
                                                                if del_confirm == '1':
                                                                    c[choice_province][choice_city].pop(district_del)
                                                                    print('%s删除成功！' % district_del)
                                                                elif del_confirm == '2':
                                                                    pass
                                                                else:
                                                                    print('输入有误，请重新输入')
                                                            else:
                                                                print('对不起，您要删除的区级不在系统数据中，请重新输入，谢谢！')
                                                    elif choice_level_5 == 'e':
                                                        while True:
                                                            district_edit = input('请输入要修改的区级名称（返回上级请输q)： ')
                                                            if district_edit == 'q':
                                                                break
                                                            elif district_edit in c[choice_province][choice_city]:
                                                                district_new = input('请输入修改后的区级名称为：')
                                                                if district_new == district_edit:
                                                                    print('对不起，新名称不能与旧名称相同，请重新输入')
                                                                elif district_new in c[choice_province][choice_city]:
                                                                    print('对不起，新名称已经存在于%s省%s市的区级列表，请重新输入' % (
                                                                        choice_province, choice_city))
                                                                else:
                                                                    edit_confirm = input(
                                                                        '您想要将区级%s的名称变更为%s，确认请输1，重新输入请输2' % (
                                                                            district_edit, district_new))
                                                                    if edit_confirm == '1':
                                                                        c[choice_province][choice_city].pop(
                                                                            district_edit)
                                                                        c[choice_province][choice_city][
                                                                            district_new] = []
                                                                        print(
                                                                            '修改成功！%s的名字已经变为%s' % (
                                                                                district_edit, district_new))
                                                                    elif edit_confirm == '2':
                                                                        pass
                                                                    else:
                                                                        print('输入有误，请重新输入')
                                                            else:
                                                                print('对不起，您要修改的区级不在系统数据中，请重新输入谢谢！')

                                                    elif choice_level_5 == 'q':
                                                        break

                                                    else:
                                                        print('对不起，您所输入的操作不存在，请重新输入，谢谢！')
                                            else:
                                                print('对不起，您输入的城市名称不存在，请重新输入')

                                elif choice_level_4 == 'q':
                                    break

                                else:
                                    print('对不起，您所输入的操作不存在，请重新输入，谢谢！')
                        else:
                            print('对不起，您输入的省份名称不存在，请重新输入')

            elif choice_level_3 == 'q':
                break

            else:
                print('对不起，您所输入的操作不存在，请重新输入，谢谢！')
