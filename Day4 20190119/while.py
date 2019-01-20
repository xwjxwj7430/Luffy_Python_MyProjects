
# age = 26
# user_guess = int(input("your guess:"))
# if user_guess == age:
# print("恭喜你答对了，可以抱得傻姑娘回家！")
# elif user_guess < age:
# print("try bigger")
# else:
# print("try smaller")


# while 条件：
# 执行代码


# a = -1
# while a < 100:
# a += 1
# print(a)

# a = 0
# while a <= 100:
# print("loop ", a)
# a += 1

# print("-----loop is ended----")

# a=0
# while a <= 100:
# print("double ", a)
# a += 2

# print("-----loop is ended----")

# a = 1
# while a <=100:
# if a == 50:
# pass
# elif a >= 60 and a <= 80:
# print("the square of loop is ", a*a)
# else:
# print("loop ", a)

# a += 1

# print("------loop is ended-----")

# a = 0
# while a <= 100:
# if a % 2 == 0:
# print("loop ", a)
# a += 1

# print("-----loop is ended----")


# count = 0
# while True:
# print("你是风儿我是沙，缠缠绵绵到天涯...", count)
# count += 1

# print("the end of loop.")


# age = 48
# trial_number = 1
# while trial_number <=3:
# userguess = int(input("your guess:"))
# if userguess == 48:
# print("恭喜你猜对了!")
# break
# elif userguess >= 0 and userguess < 48:
# print("try bigger")
# elif userguess < 0:
# print("please enter a valid age number")
# else:
# print("try smaller")

# trial_number_left = 3 - trial_number
# if trial_number_left == 0:
# print("对不起，系统检测到您的猜测次数已经用完，请充值后再试")
# else:
# print("你还剩下", trial_number_left, "次机会")
# trial_number += 1

# print("游戏结束")


# 首先设置答案年龄为48岁，同时重置尝试次数为1，最大尝试次数为3
age = 48
trial_number = 1
max_trial = 3
# 大背景是尝试的次数，当次数《=3时，用户可以继续试，每试一次次数循环+1，剩余次数即为3
while trial_number <= max_trial:
    userguess = int(input("your guess:"))
    if userguess == age:
        print("恭喜你猜对了!")
        break
    elif userguess >= 0 and userguess < age:
        print("try bigger")
    elif userguess < 0:
        print("please enter a valid age number")
    else:
        print("try smaller")

    trial_number_left = max_trial - trial_number
    if trial_number_left == 0:
        willing_to_go_on = input("对不起，系统检测到您的猜测次数已经用完，您还要重新玩一次吗?")
        if willing_to_go_on == "y":
            trial_number = 1

    else:
        print("你还剩下", trial_number_left, "次机会")
    trial_number += 1
else:
    print("所有次数都用上了！")
print("游戏结束")
























p

