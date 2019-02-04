#  定义程序要用到的3个函数


def func1():
    print('-'*50)
    print('Name: ', user_info[username]['name'])
    print('Age: ', user_info[username]['age'])
    print('Job: ', user_info[username]['job'])
    print('Dept: ', user_info[username]['dept'])
    print('Phone: ', user_info[username]['phone'])
    print('-'*50)


def func2():



def func3():
    print(3)


# 读取数据文件，将文件字符串内容转换成列表，然后转换成以用户名为关键字，用户其他信息为值的键值对，放入字典user_info
user_info = {}

f = open('account.txt', mode='r', encoding='utf-8')  # 打开文档，只读模式
data = f.readlines()  # 读取每一行，每一行作为一个元素，类型为字符串，输出在data这个大列表中，数据格式为data = ['第一行内容'， '第二行内容'...]
for i in data:
    user = i.strip().replace(' ', '').split(',')  # 将每行内容去除结尾\n换行符，去掉字符串中间空格，以逗号为分隔符将每行（字符串）变成列表
    list_keyword = ['pwd', 'name', 'age', 'job', 'dept', 'phone']  # 将每一列的title的列表制作好，以备下面与对应值制作成子字典
    user_info[user[0]] = dict(
        zip(list_keyword, user[1:]))  # user_info的关键字为用户名，值为一个子字典，子字典的关键字为密码、工作、姓名等，值为实际客户的信息如abc123，IT，张三等

print(user_info)

# 登陆程序代码开始
count = 1
while count <= 3:

    username = input('username: ').strip()
    password = input('password: ').strip()

    if username in user_info.keys() and password == user_info[username]['pwd']:
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

    print('1. 修改个人信息')
    print('2. 打印个人信息')
    print('3. 修改密码')

    choice = input('choice: ')
    if choice == '1':
        func1()
    if choice == '2':
        func2()
    if choice == '3':
        func3()
