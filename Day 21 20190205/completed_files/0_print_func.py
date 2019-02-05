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

# what的输入有两种，一种是*号，全部都要，另外一种是关键字字符串拼接，1-n个如'name'或'name,age'等

what = 'name,age'

title_list = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']


def print_info(what, list):  # 如print_info('name,age', [1, 3, 8])或者print_info('*', [1, 3, 8])

    # 首先是识别what参数传入进来需要显示的项目名称，
    index_list = []
    info_row = []
    s = ''
    what = what.split(',')  # 如果传进去what是'age, name'的话，这里就变成了['age', 'name']
    subset_flag = True
    global title_list
    for element in what:  # 先看一下用户传入的需打印的title是不是都是可打印的title，与title_list进行匹配
        if element in title_list:
            index_list.append(title_list.index(element))  # 将需打印的title在title_list当中的索引做成一个新列表，供打印使用
        else:
            subset_flag = False

    if subset_flag:  # 如果没有问题，都是合法的title
        for i in selected_staff:
            for index in index_list:
                s = s + title_list[index] + ' ' + staff_list[i][index] + ' '

            s = s + '\n'

        print(s)
    else:
        print('对不起，您的输入有误，请重新输入！')


print_info('name,age', [1, 4, 5, 6])
