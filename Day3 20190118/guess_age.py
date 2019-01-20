# name = input("What is your name: ")
# print("Hello " + name)
# print("Hello", name)


# 加了逗号就自带空格，不用在Hello后面再加空格了


# username = input("username: ")
# password = input("password: ")

# print(username, password)
# print(username + password)


# name = input("What is your name: ")
# age = input ("How old are you: ")
# hometown = input("Where is your hometown: ")

# print("Hello", name, "you are", age, "years old", "your hometown is", hometown)

# age = 22
# name = "Alex"
# print(type(age))
# print(type(name))

# 人很容易分清数字和汉字，一定要告诉计算机数据的“数据类型”，数字就可以运算，文字就不能运算加减乘除。

# name = input("please type in your name: ")
# age = input("please enter your age: ")
# job = input("please enter your job: ")
# hometown = input("please enter your hometown name: ")

# title_first = "---------------- info of"
# title_second = "------------"
# print(title_first, name, title_second)
# print("Name:           ", name)
# print("Age:            ", age)
# print("Job:            ", job)
# print("Hometown:       ", hometown)
# print("---------------- end-----------")

# name = input("Name: ")
# age = input("Age: ")
# age = int(input("Age: "))
# job = input("Job: ")
# hometown = input("Hometown: ")

# info = '''
# ----------------- info of %s ------------
# Name: %s
# Age: %f
# Job: %s
# Hometown: %s
# ------------------ end -------------
# '''  % (name, name, age, job, hometown)

# 这里的%s是作为占位符，后面的%（）就是按顺序填补上面的占位符
# s = string
# d = digit
# f = float
# 如果是%d的话，就只能是数字类型，即int
# 但是input的输出结果都是string字符串，即使输入的是22数字，结果还是字符串，所以这里的age如果使用%d就会报错。
# 如果一定要使用%d的话，对于input就要进行int（）的函数化处理，将输出转为整数类型
# 如果使用%f的话，结果就会变成2.00000之类的小数

# print(info)

# 基本运算符：算数，比较，赋值，逻辑

# 算数：+ - * / % // **
# a = 2
# b = 3
# a + b
# a - b
# a * b
# a / b
# a % b # 这叫取模，即取a除以b的余数，a = 10, b = 2, a % b = 0，可以用来判别奇偶数
# a // b # 这叫取整除，返回a除以b的商的整数部分，a = 10, b =2, a // b = 5

# 比较：
# a > b
# a < b
# a == b # =是赋值，==是比较中的等于
# a != b # !=是不等于
# a >= b
# a <= b

# 赋值运算:
# a += b # 即a = a + b
# a -= b # 即a = a - b
# a *= b # 即a = a * b
# a /= b # 即a = a / b
# a **= b # 即a = a ** b
# a %= b # 即a = a % b
# a //= b # 即a = a // b

# 逻辑运算：
# a and b # 即与门
# a or b # 系统会自动从a开始，a为true即停止并返回true，否则继续b c d一个个下去
# not a and b  # 即对a and b的结果取反


# if 条件：
# 满足条件执行代码
# else：
# if条件不满足就走这段

# age_of_oldboy = int(input("enter the age of oldboy: "))
# if age_of_oldboy > 45:
# print("time to retire!bye bye")
# # 这叫单分支

# age_of_oldboy = int(input("enter the age of oldboy: "))
# if age_of_oldboy > 45:
# print("time to retire!bye bye")
# else:
# print("还能再折腾几年")
# # 这叫双分支


# name = input("enter your name:")
# gender = input("enter your gender:")

# _male = "male"
# _female = "female"

# if gender == _female:
# print("我喜欢女生！")
# else:
# print("一起来搞基！")


# name = input("enter your name:")
# gender = input("enter your gender:")
# age = int(input("enter your age:"))

# _male = "male"
# _female = "female"

# if gender == _female:
# if age < 28:
# print("我喜欢女生！")
# else:
# print("姐弟恋也很好奥！")
# else:
# print("一起来搞基！")

# if 条件：
# 满足条件执行代码
# elif 条件：
# 上面的条件不满足就走这个
# elif 条件：
# 上面的条件不满足就走这个
# elif 条件：
# 上面的条件不满足就走这个
# else:
# 上面所有条件都不满足就走这段

# _userscore = int(input("Score: "))

# if _userscore >100:
# print("成绩最多只能到100")

# elif _userscore >= 90:
# level = "A"
# print(level)

# elif _userscore >= 80:
# level = "B"
# print(level)

# elif _userscore >= 60:
# level = "C"
# print(level)

# elif _userscore >= 40:
# level = "D"
# print(level)

# elif _userscore >= 0:
# level = "E"
# print(level)

# else:
# print("成绩不能为负数")


# get_up_time = int(input("get up time:"))

# if get_up_time > 24:
# print("做你的白日梦，一天能超过24小时吗？")

# elif get_up_time >= 20:
# print("你也别起了，天都黑了，睡睡就到明天了")

# elif get_up_time >= 18:
# print("刚好吃晚饭")

# elif get_up_time >= 12:
# print("刚好吃午饭")

# elif get_up_time >= 9:
# print("还可以")

# elif get_up_time >= 6:
# print("很勤奋，继续加油！")

# elif get_up_time >= 4:
# print("太早了，再睡会儿，别搞坏身体")

# elif get_up_time >= 0:
# print("干啥？期末考试啊？熬夜？快睡！")

# else:
# print("又做白日梦！回到过去了啊！白痴！")


# KFC = input("KFC?")


# if KFC == "y":
# print("KFC coming")

# elif KFC == "n":
# spicy = input("spicy?")
# if spicy == "y":
# print("sichuan cuisine coming")
# elif spicy == "n":
# sweet = input("sweet?")
# if sweet == "y":
# print("suzhou cuisine coming")
# elif sweet == "n":
# print("no food  be hungry ")
# else:
# print("invalid choice in sweet")
# else:
# print("invalid choice in spicy")
# else:
# print("invalid choice in KFC")


# sex = input("请问您想要男服务员还是女服务员？")
# if sex == "男":
# age = int(input("请问您想要多大年纪的服务员呢？"))
# if age <= 0:
# print("别瞎几把喊可以吗？")
# elif age <= 18:
# print("请输入合法的要求，谢谢，请勿违法！")
# elif age <= 25:
# print("没问题，年轻小伙子看着，老板楼上请啦！")
# elif age <= 50:
# print("好叻，成熟男士看着，楼上候着啦！")
# else:
# print("不好意思，超龄了，本店不提供服务，谢谢！")

# elif sex == "女":
# age = int(input("请问您想要多大年纪的服务员呢？"))
# if age <= 0:
# print("别瞎几把喊可以吗？")
# elif age <= 18:
# print("请输入合法的要求，谢谢，请勿违法！")
# elif age <= 25:
# print("没问题，年轻美眉老板楼上请啦！")
# elif age <= 50:
# print("好叻，成熟女性楼上候着啦！")
# else:
# print("不好意思，超龄了，本店不提供服务，谢谢！")


# elif sex == "人妖":
# area = input("请问您哪里的人妖呢？")
# if area == "泰国":
# print("泰国人妖来咯！")
# elif area == "本土":
# print("本土人妖来咯！")
# else:
# print("不好意思，本店没有您想要的人妖地区，请另寻别家，谢谢！")

# else:
# print("不好意思，本店没有您想要的服务，请另寻别家，谢谢！")


age = 26
user_guess = int(input("your guess:"))
if user_guess == age:
    print("恭喜你答对了，可以抱得傻姑娘回家！")
elif user_guess < age:
    print("try bigger")
else:
    print("try smaller")












