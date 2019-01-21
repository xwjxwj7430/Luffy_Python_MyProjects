# a. 使用while循环实现输出2-3+4-5+6...+100 的和；

a = 2
s = 0

while a <= 100:
    if a % 2 == 0:
        s += a
    else:
        s -= a

    a += 1

print(s)