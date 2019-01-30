#  有两个列表

l1 = [11, 22, 33]
l2 = [22, 33, 44]

# # 1. 获取内容相同的元素列表
# for i in l1:
#     if i in l2:
#         print(i)
#
# # 2. 获取l1中有，l2中没有的元素列表
# for i in l1:
#     if i not in l2:
#         print(i)
#
# # 3. 获取l2中有，l1中没有的元素列表
# for i in l2:
#     if i not in l1:
#         print(i)

# 4. 获取l1和l2中内容都不同的元素
dif1 = []
dif2 = []
for i in l2:
    if i not in l1:
        dif1.append(i)

for i in l1:
    if i not in l2:
        dif2.append(i)

print(dif1)
dif1.extend(dif2)
print(dif1)
