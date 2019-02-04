#  定义程序要用到的3个函数


def func1(index):
    print('-' * 50)
    print('Name: ', user_info[username][2])
    print('Age: ', user_info[username][3])
    print('Job: ', user_info[username][4])
    print('Dept: ', user_info[username][5])
    print('Phone: ', user_info[username][6])
    print('-' * 50)


def func2():
    print('person data:', user_info[username])
    print('2. Name: ', user_info[username][2])
    print('3. Age: ', user_info[username][3])
    print('4. Job: ', user_info[username][4])
    print('5. Dept: ', user_info[username][5])
    print('6. Phone: ', user_info[username][6])
    while True:
        index_choice = input('[select column id to change:]')
        if index_choice.isdigit():
            if 0 < int(index_choice) <= (len(user_info[username])-1):
                print('current value>:', user_info[username][int(index_choice)])
                new_info = input('new value>:')
                user_info[username][int(index_choice)] = new_info
                break
            else:
                print('操作不合法，请重新输入!')
        else:
            print('操作不合法，请重新输入!')


def func3():
    while True:
        old_pwd = input('old password:')
        new_pwd = input('new password:')
        confirm_pwd = input('confirm new password:')
        if old_pwd == user_info[username][1]:
            if new_pwd == confirm_pwd:
                print('修改成功！')
                user_info[username][1] = new_pwd
                break
            else:
                print('两次输入不一致，请重新输入!')
        else:
            print('原密码错误，请重新输入!')


# 读取数据文件，将文件字符串内容转换成列表，然后转换成以用户名为关键字，用户其他信息为值的键值对，放入字典user_info

user_info = {}

f = open('account.txt', mode='r', encoding='utf-8')  # 打开文档，只读模式
data = f.readlines()  # 读取每一行，每一行作为一个元素，类型为字符串，输出在data这个大列表中，数据格式为data = ['第一行内容'， '第二行内容'...]
for i in data:
    user = i.strip().replace(' ', '').split(',')  # 将每行内容去除结尾\n换行符，去掉字符串中间空格，以逗号为分隔符将每行（字符串）变成列表
    # print(user)
    user_info[user[0]] = user
# print(user_info)

# 登陆程序代码开始
count = 1
while count <= 3:

    username = input('username: ').strip()
    password = input('password: ').strip()

    if username in user_info.keys() and password == user_info[username][1]:
        print('login success')
        s_welcome = 'welcome %s' % username
        print(s_welcome.center(50, '-'))
        break
    else:
        print('login failed')
        count += 1
else:
    exit('too many tries..')

# 登陆成功，功能开始
while True:

    print('1. 打印个人信息')
    print('2. 修改个人信息')
    print('3. 修改密码')

    choice = input('choice: ')
    if choice == '1':
        func1()
    if choice == '2':
        func2()
    if choice == '3':
        func3()
