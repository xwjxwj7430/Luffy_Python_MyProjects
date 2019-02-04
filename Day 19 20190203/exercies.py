# # def sayhi():
# #     print("Hello, I'm nobody!")
# #
# #
# # sayhi()
#
# # #
# # a, b = 5, 8
# # # c = a ** b
# # # print(c)
# #
# # def calc(x, y):
# #     res = x ** y
# #     return res  # 返回函数执行结果
# #
# #
# # c = calc(a, b)  # 结果赋值给c变量
# # print(c)
#
#
# def stu_register(name, age, country, course):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("age:", age)
#     print("国籍:", country)
#     print("课程:", course)
# #
# #
# # stu_register("王山炮", 22, "CN", "python_devops")
# # stu_register("张交春", 21, "CN", "linux")
# # stu_register("刘老根", 25, "CN", "linux")
#
#
# def stu_register(name, age, course, country="CN"):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("age:", age)
#     print("国籍:", country)
#     print("课程:", course)
#
#
# stu_register("王山炮", 22, "python_devops")
# stu_register("张交春", 21, "linux")
# stu_register("刘老根", 25, "linux")

def stu_register(name, age, **args):
    print(name, age, args)
# stu_register('Alex', 22)

# stu_register("Jack", 32, country="CN", course="Python")




# def stu_register(name, age, course="PY", country="CN"):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("age:", age)
#     print("国籍:", country)
#     print("课程:", course)
#     if age > 22:
#         return False
#     else:
#         return True
#
# registration_status = stu_register("王山炮", 23, course="全栈开发", country="JP")
#
# if registration_status:
#     print("注册成功")
# else:
#     print("too old to be a student.")




name = "Alex Li"

def change_name():
    global name
    print("before change:", name)
    name = "金角大王，一个有Tesla的男人"
    print("after change", name)

change_name()

print("在外面看看name改了么", name)