# 实现用户输入用户名和密码,当用户名为 seven 或 alex 且密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次；
count = 1

while count <=3:
    login_name = input("username:")
    login_password = input("password:")

    if login_name == "seven" or login_name == "alex":
        if login_password == "123":
            print("登录成功！")
            break

    # 这是另一种实现方式，本质上相同，只是把两个if条件并到了一行，因为上面那个只适用于两人密码相同，如果两人密码不同就可
    # 能需要下面这种类型的代码。

    # if (login_name == "seven" and login_password == "123") or (login_name == "alex" and login_password == "123"):
    #     print("登录成功！")
    #     break

    print("登录失败！")
    count += 1


