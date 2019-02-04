# name = "Alex"
#
# def change_name():
#     name = "Alex2"
#
#     def change_name2():
#         name = "Alex3"
#         print("第三层打印", name)
#
#     change_name2()  # 调用内层函数
#     print("第二层打印", name)
#
# change_name()
# print("最外层打印", name)
# change_name2()

# calc = lambda x, y: x ** y
# print(calc(2, 5))
#
# res = map(lambda x: x ** 2, [1, 5, 4, 7, 8])
# for i in res:
#     print(i)


def add(x, y, f):
    return f(x) + f(y)


res = add(3, -6, abs)
print(res)

#
# def calc(n):
#     print(n)
#     if int(n / 2) == 0:
#         return n
#     return calc(int(n / 2))
#
# calc(10)


def calc(n):
    v = int(n / 2)
    print(v)
    if v > 0:
        calc(v)
    print(n)

calc(10)
