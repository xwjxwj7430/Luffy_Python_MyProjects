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
                print()
    elif choice == 'w':
        print()
    elif choice == 'q':
        print('退出成功')
        exit_flag = True
    else:
        print('对不起，您输入的操作代码有误，请重新输入')

