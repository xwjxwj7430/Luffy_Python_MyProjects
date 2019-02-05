title_list = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']


def read_file(where):
    staff_list = []
    f = open('%s' % where, mode="r+", encoding='utf-8')
    data = f.read()
    row = data.split('\n')
    for staff in row:
        staff_list.append(staff.split(','))
    return staff_list

staff_list = read_file('staff_table')
print(staff_list)

if how[0] == 'staff_id' or how[0] == 'age':  # 如果比较的项是员工ID或者年龄这类数字
    if how[1] == '>':
        for index, i in enumerate(staff_list):
            if int(i[title_list.index(how[0])]) > int(how[2]):  # 筛选完毕
                selected_staff.append(index)  # 输出符合条件的所有staff的index的列表selected_staff_index
        return selected_staff

    for index, i in enumerate(staff_list):
        exec('''
                if 5 %s 7:
                    print(5)
                else:
                    print(7)
        ''' % how[1])

    elif how[1] == '<':
        for index, i in enumerate(staff_list):
            if int(i[title_list.index(how[0])]) < int(how[2]):  # 筛选完毕
                selected_staff.append(index)
        return selected_staff

    elif how[1] == '==':
        for index, i in enumerate(staff_list):
            if int(i[title_list.index(how[0])]) == int(how[2]):  # 筛选完毕
                selected_staff.append(index)
        return selected_staff

elif how[0] == 'enroll_date' and how[1] == 'like':  # 比较入职日期，日期目前只有like+年份的操作
    for index, i in enumerate(staff_list):
        if i[title_list.index(how[0])].startswith(how[2]):  # 筛选完毕
            selected_staff.append(index)
    return selected_staff

elif how[0] in title_list and how[1] == '==':  # 如果条件是除上述以外的项目，如比较名字、电话、部门
    for index, i in enumerate(staff_list):
        if i[title_list.index(how[0])] == how[2]:  # 筛选完毕
            selected_staff.append(index)
    return selected_staff

else:
    print('对不起，您的输入有误，请重新输入！')