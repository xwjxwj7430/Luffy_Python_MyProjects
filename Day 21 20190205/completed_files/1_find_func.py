staff_list = [['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01'],
              ['2', 'Jack Wang', '28', '13451024608', 'HR', '2015-01-07'],
              ['3', 'Rain Wang', '21', '13451054608', 'IT', '2017-04-01'],
              ['4', 'Mack Qiao', '44', '15653354208', 'Sales', '2016-02-01'],
              ['5', 'Rachel Chen', '23', '13351024606', 'IT', '2013-03-16'],
              ['6', 'Eric Liu', '19', '18531054602', 'Marketing', '2012-12-01'],
              ['7', 'Chao Zhang', '21', '13235324334', 'Administration', '2011-08-08'],
              ['8', 'Kevin Chen', '22', '13151054603', 'Sales', '2013-04-01'],
              ['9', 'Shit Wen', '20', '13351024602', 'IT', '2017-07-03'],
              ['10', 'Shanshan Du', '26', '13698424612', 'Operation', '2017-07-02']]

title_list = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']
# instruction_list = ['find', 'add', 'del', 'update']
compare_operation_list = ['>', '<', '==', 'like']
# 1.可进行模糊查询，语法至少支持下面3种查询语法:
#
# find name,age from staff_table where age > 22
#
# find * from staff_table where dept = "IT"
#
# find * from staff_table where enroll_date like "2013"


# find 信息列表 from staff_list where 条件

search_instruction = input('please type in your searching instruction:').strip()
words = search_instruction.split(' ')
print('words', words)

if words[0] == 'find' and len(words) == 8:  # 命令的第一个字符串识别是哪一类操作，如果为find，开始进行find功能，将关键参数传入函数，函数命令元素为8个，多了少了都不行

    def func_find(what, where, *how):
        print(what, where, how)

        # 读取文件名为where的文件

        def read_file(where):
            staff_list = []
            f = open('%s' % where, mode="r+", encoding='utf-8')
            data = f.read()
            # print(data)
            row = data.split('\n')
            for staff in row:
                staff_list.append(staff.split(','))
                print(staff)

            return staff_list


        read_file(where)

        # func_find('name,age', 'staff_table', ('age', '>', '22'))

        # 首先先筛选，筛选完了再考虑打印什么。
        # how[0]为目标比较项，如age，name等，how[1]为比较符，如大于小于等于等等，how[2]为去比较的值，如年龄22，电话号码等

        if how[0] == 'staff_id' or how[0] == 'age':  # 如果比较的项是员工ID或者年龄这类数字
            if how[1] == '>':
                for i in staff_list:
                    if int(i[title_list.index(how[0])]) > int(how[2]):  # 筛选完毕
                        func_print(what)  # 打印完毕，for循环打印，传入打印的关键参数what

            elif how[1] == '<':
                for i in staff_list:
                    if int(i[title_list.index(how[0])]) < int(how[2]):  # 筛选完毕
                        func_print(what)  # 打印完毕，for循环打印

            elif how[1] == '==':
                for i in staff_list:
                    if int(i[title_list.index(how[0])]) == int(how[2]):  # 筛选完毕
                        func_print(what)  # 打印完毕，for循环打印

        elif how[0] == 'enroll_date' and how[1] == 'like':  # 比较入职日期，日期目前只有like+年份的操作
            for i in staff_list:
                if i[title_list.index(how[0])].startswith(how[2]):  # 筛选完毕
                    func_print(what)  # 打印完毕，for循环打印

        elif how[0] in title_list and how[1] == '==':  # 如果条件是除上述以外的项目，如比较名字、电话、部门
            for i in staff_list:
                if i[title_list.index(how[0])] == how[2]:  # 筛选完毕
                    func_print(what)  # 打印完毕，for循环打印

        else:
                print('对不起，您的输入有误，请重新输入！')


    if what == '*':  # 如果信息列表显示要求的字段的字符串为*，则为显示全部信息
        print_list = title_list
        print(print_list)
        print(eval(how))
        # for i in staff_list:
        #     if int(i[2])
    elif words[1].isalpha() or ',' in words[1] and words[1] != ',' and words[
        1] != 'f':  # 如果信息列表显示要求的字段字符串为英文字母的，则符合命令要求，进行下一步判断
        print_list = words[1].split(',')
        print_list = list(set(print_list))
        print(print_list)
        # for i in key_word:

func_find(words[1], words[3], words[5:])  # 成功将3个参数由input改写后传入func_find中，并运行搜索功能

# if words[0] == 'add'
# if words[0] == 'del'
# if words[0] == 'update'
