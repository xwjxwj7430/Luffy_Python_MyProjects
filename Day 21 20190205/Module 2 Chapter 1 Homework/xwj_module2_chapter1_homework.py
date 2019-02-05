def read_file_as_dict(where):
    staff_dict = {}
    f = open('%s' % where, mode="r+", encoding='utf-8')
    data = f.read()
    f.close()
    row = data.strip().split('\n')
    for staff in row:
        staff_info = staff.split(',')  # 每一条是这样的: ['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01']
        staff_dict[staff_info[3]] = staff_info
    return staff_dict


def save_back_to_file(where):
    s = staff_dict.values()
    s2 = ''
    for staff in s:
        for info in staff:
            s2 = s2 + info + ','
        s2 = s2.rstrip(',') + '\n'
    s2.rstrip('\n')

    f = open('%s' % where, mode="w", encoding='utf-8')
    f.writelines(s2)
    f.close()


def find_staff(how):
    # 首先先筛选，输出需要打印的员工名单，即在staff_list中的index号
    # how[0]为目标比较项，如age，name等，how[1]为比较符，如大于小于等于等等，how[2]为去比较的值，如年龄22，电话号码等
    selected_staff = []
    if how[0] == 'staff_id' or how[0] == 'age':  # 如果比较的项是员工ID或者年龄这类数字
        if how[1] == '>':
            for key, value in staff_dict.items():
                if int(value[title_list.index(how[0])]) > int(how[2]):  # 筛选完毕
                    selected_staff.append(key)  # 输出符合条件的所有staff的index的列表selected_staff_index
            return selected_staff

        elif how[1] == '<':
            for key, value in staff_dict.items():
                if int(value[title_list.index(how[0])]) < int(how[2]):  # 筛选完毕
                    selected_staff.append(key)
            return selected_staff

        elif how[1] == '=':
            for key, value in staff_dict.items():
                if int(value[title_list.index(how[0])]) == int(how[2]):  # 筛选完毕
                    selected_staff.append(key)
            return selected_staff

    elif how[0] == 'enroll_date' and how[1] == 'like':  # 比较入职日期，日期目前只有like+年份的操作
        for key, value in staff_dict.items():
            if value[title_list.index(how[0])].startswith(how[2]):  # 筛选完毕
                selected_staff.append(key)
        return selected_staff

    elif how[0] == 'name' and how[1] == '=':  # 比较姓名
        target_name = ' '.join(how[2:])  # 把已经拆分成两个列表元素的姓与名合并起来
        for key, value in staff_dict.items():
            if value[title_list.index(how[0])] == target_name:  # 筛选完毕
                selected_staff.append(key)
        return selected_staff

    elif how[0] in title_list and how[1] == '=':  # 如果条件是除上述以外的项目，如比较电话、部门
        for key, value in staff_dict.items():
            if value[title_list.index(how[0])] == how[2]:  # 筛选完毕
                selected_staff.append(key)
        return selected_staff

    else:
        print('对不起，您的输入有误，请重新输入！')


def print_info(what, list):  # 如print_info('name,age', [1, 3, 8])或者print_info('*', [1, 3, 8])

    # 首先是识别what参数传入进来需要显示的项目名称，
    index_list = []
    s = ''
    global title_list  # 呼叫全局变量，用作后续对比
    subset_flag = True  # 标识符，查看用户输入信息是否合法

    if what == '*':  # 输入为*号，即打印所有信息
        index_list = range(len(title_list))

    else:
        what = what.split(',')  # 如果传进去what是'age, name'的话，这里就变成了['age', 'name']
        for element in what:  # 先看一下用户传入的需打印的title是不是都是可打印的title，与title_list进行匹配
            if element in title_list:
                index_list.append(title_list.index(element))  # 将需打印的title在title_list当中的索引做成一个新列表，供打印使用
            else:
                subset_flag = False

    if subset_flag:  # 如果没有问题，都是合法的title
        for i in selected_staff:  # 将每个要打印的员工循环
            for index in index_list:  # 将每个员工的每个要打印的项目循环
                s = s + title_list[index] + ' ' + staff_dict[i][index] + ' '  # 将同一个员工的信息加在同一行

            s = s + '\n'  # 每个员工循环完毕，换行

        print(s)  # 打印全部需要打印的信息
    else:
        print('对不起，您的输入有误，请重新输入！')


def add_staff(words, staff_dict):
    new_staff_id = str(len(staff_dict) + 1)  # 新的staff_id就是现有的数量+1，为了后面写数据方便，格式转成字符串
    r_detailed_info = words[3].split(',')  # 将除了姓以外的所有数据处理，结果如[Li', '25', '134435344', 'IT', '2015-10-29']
    r_detailed_info[0] = words[2] + ' ' + r_detailed_info[0]  # 将姓氏加上
    r_detailed_info.insert(0, new_staff_id)  # 插入新的staff_id
    if r_detailed_info[3] in staff_dict:
        print('对不起，您想要添加的手机号已经存在，无法重复添加！')
    else:
        staff_dict[r_detailed_info[3]] = r_detailed_info  # 将新的员工信息，手机号作为键，所有信息的列表作为值，插入字典

        save_back_to_file(words[1])
        print('新员工信息%s，共1条已加入系统' % r_detailed_info)


def del_staff(selected_staff, staff_dict):
    for staff in selected_staff:  # 将查找到的员工信息删除
        deleted_staff = staff_dict.pop(staff)

    id_bigger_than_del_list = find_staff(['staff_id', '>', words[6]])  # 删除后只影响它后面的staff_id，需要-1
    for key in id_bigger_than_del_list:  # 更新staff_id
        staff_dict[key][0] = str(int(staff_dict[key][0]) - 1)

    save_back_to_file(words[2])
    print('老员工信息%s，共1条已删除' % deleted_staff)


def update_staff(selected_staff, staff_dict):
    global title_list
    for staff in selected_staff:  # 将查找到的员工信息更新
        staff_dict[staff][title_list.index(words[3])] = words[5]
    save_back_to_file(words[1])
    print('所有%s为%s的员工，%s已经变更为%s，共变更%s条' % (words[7], words[9], words[3], words[5], len(selected_staff)))


#  --------------------------------------------函数区结束，下面为实现代码区---------------------------------------------
title_list = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']

while True:
    search_instruction = input('please type in your searching instruction:').strip().replace('"', '')
    words = search_instruction.split(
        ' ')  # words = ['find', 'name,age', 'from', 'staff_table', 'where', 'age', '>', '22']

    if words[0] == 'find' and 8 <= len(words) <= 9:  # 命令的第一个字符串识别是哪一类操作，如果为find，开始进行find功能，将关键参数传入函数，函数命令元素一般为8个，查姓名为9个

        staff_dict = read_file_as_dict(words[3])  # 调用read_file函数读取文档，生成对应的列表文件
        # 列表类似staff_list = [['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01'],
        # ['2', 'Jack Wang', '28', '13451024608', 'HR', '2015-01-07']]

        selected_staff = find_staff(words[5:])  # words[5:]为条件str语句的列表['age', '>', '22']
        #  输出的这个selected_staff的列表内容为[1, 2, 3, 5]等等的被筛选后需要打印信息的员工在staff_list里面的索引

        # print(selected_staff)

        print_info(words[1], selected_staff)  # 然后是利用传入进来的list，打印list里每个人的what项目的信息，每人一行

        print('这条语句查询了%s条' % len(selected_staff))

    elif words[0] == 'add' and len(
            words) == 4:  # 姓占1个长度，['add', 'staff_table', 'Alex', 'Li,25,134435344,IT,2015-10-29']
        staff_dict = read_file_as_dict(words[1])  # 将change_file函数的返回值字典赋予staff_dict
        add_staff(words, staff_dict)

    elif words[0] == 'del' and len(words) == 7:  # ['del', 'from', 'staff_table', 'where', 'id', '=', '3']，命令长度为7

        staff_dict = read_file_as_dict(words[2])
        words[4] = 'staff_id'  # 将id改为staff_id以配合功能查询
        selected_staff = find_staff(words[4:])  # 用find_staff功能进行查询
        if not selected_staff:  # 如果selected_staff值为空，
            print('对不起，系统没有查询到，请重新查询！')
        else:  # 如果selected_staff值不为空，
            del_staff(selected_staff, staff_dict)

    elif words[0] == 'update' and len(
            words) == 10:  # 如['update', 'staff_table', 'set', 'dept', '=', 'Market', 'where', 'dept', '=', 'IT']
        staff_dict = read_file_as_dict(words[1])
        selected_staff = find_staff(words[7:])
        if not selected_staff:  # 如果selected_staff值为空，
            print('对不起，系统没有查询到，请重新查询！')
        else:  # 如果selected_staff值不为空，
            update_staff(selected_staff, staff_dict)

    elif search_instruction == 'q':
        exit('感谢您的使用，再见！')

    else:
        print('对不起，系统无法识别您的命令，请重新输入！')
