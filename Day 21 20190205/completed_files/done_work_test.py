title_list = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']


def read_file(where):
    staff_list = []
    f = open('%s' % where, mode="r+", encoding='utf-8')
    data = f.read()
    row = data.split('\n')
    for staff in row:
        staff_list.append(staff.split(','))
    return staff_list


def find_staff(how):
    # 首先先筛选，输出需要打印的员工名单，即在staff_list中的index号
    # how[0]为目标比较项，如age，name等，how[1]为比较符，如大于小于等于等等，how[2]为去比较的值，如年龄22，电话号码等
    selected_staff = []
    if how[0] == 'staff_id' or how[0] == 'age':  # 如果比较的项是员工ID或者年龄这类数字

        if how[1] == '>':
            def func(arg):

            for index, i in enumerate(staff_list):
                if int(i[title_list.index(how[0])]) > int(how[2]):  # 筛选完毕
                    selected_staff.append(index)  # 输出符合条件的所有staff的index的列表selected_staff_index
            return selected_staff

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


#  --------------------------------------------函数区结束，下面为实现代码区---------------------------------------------


search_instruction = input('please type in your searching instruction:').strip()
words = search_instruction.split(' ')  # words = ['find', 'name,age', 'from', 'staff_table', 'where', 'age', '>', '22']

if words[0] == 'find' and len(words) == 8:  # 命令的第一个字符串识别是哪一类操作，如果为find，开始进行find功能，将关键参数传入函数，函数命令元素为8个，多了少了都不行

    staff_list = read_file(words[3])  # 调用read_file函数读取文档，生成对应的列表文件
    # 列表类似staff_list = [['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01'],
    # ['2', 'Jack Wang', '28', '13451024608', 'HR', '2015-01-07']]

    selected_staff = find_staff(words[5:])  # words[5:]为条件str语句的列表['age', '>', '22']
    #  输出的这个selected_staff的列表内容为[1, 2, 3, 5]等等的被筛选后需要打印信息的员工在staff_list里面的索引
    print(selected_staff)
    # if what == '*':  # 如果信息列表显示要求的字段的字符串为*，则为显示全部信息
    #     print_list = title_list
    #     print(print_list)
    #     print(eval(how))
    #     # for i in staff_list:
    #     #     if int(i[2])
    # elif words[1].isalpha() or ',' in words[1] and words[1] != ',' and words[
    #     1] != 'f':  # 如果信息列表显示要求的字段字符串为英文字母的，则符合命令要求，进行下一步判断
    #     print_list = words[1].split(',')
    #     print_list = list(set(print_list))
    #     print(print_list)
    #     # for i in key_word:

# if words[0] == 'add'
# if words[0] == 'del'
# if words[0] == 'update'
