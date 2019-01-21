# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

h = 100
count = 1
length = 100

while count <= 10:
    count += 1
    h = h * 0.5
    length = length + h * 2


print(length)
print(h)

