# 编写登陆接口基础需求：让用户输入用户名密码认证成功后显示欢迎信息输错三次后退出程序升级需求：可以支持多个用户登录
# (提示，通过列表存多个账户信息)用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态
# （提示:需把用户锁定的状态存到文件里）


f = open("lock_info.txt", "r")  # 首先打开lock_info.txt并读取lock_status的值；
if f.mode == "r":
    lock_status = f.read()
    if lock_status == "0":  # "0"表示当前未锁定，即开始进行主程序，进行输入和登陆；
        count = 1
        login_info = [["seven", "123"], ["alex", "456"], ["jack", "789"], ["nick", "901"]]  # 这里4个是登陆的用户名密码组成的list；

        while count <= 3:
            login_name = input("请输入您的用户名: ")
            login_password = input("请输入您的密码: ")

            if [login_name, login_password] in login_info:  # 当用户输入的一对名字和密码在login_info集合中，匹配成功，可登陆；
                print("登录成功！欢迎" + login_name + "的光临！")
                lock_status = "0"  # 成功登陆表示锁定状态为0（不锁定），3次中只要有1次正确就会重置状态为0；
                break
            else:
                print("登录失败！")
                count += 1
                lock_status = "1"  # 登陆失败表示锁定状态为1（已锁定），如果3次登陆都失败，状态就会被保持为1；

        f = open("lock_info.txt", "w+")  # 打开lock_info.txt并准备编辑；
        f.write(lock_status)  # 将锁定状态"0"或者"1"写入文档，注意：写入的内容只能为字符串，否则会报错；
        f.close()  # 关闭并保存文档，以备下次启动程序时读取状态；

    else:
        print("由于您登陆的失败次数过多，您的终端已经被锁定，请联系管理员解锁，谢谢！")
else:
    print("读取锁定文件失败，请重试")
