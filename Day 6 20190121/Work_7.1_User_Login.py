# 实现用户输入用户名和密码,当用户名为 seven 且密码为 123 时,显示登陆成功,否则登陆失败；

login_name = input("username:")
login_password = input("password:")

if login_name == "seven" and login_password == "123":
    print("登录成功！")
else:
    print("登录失败！")