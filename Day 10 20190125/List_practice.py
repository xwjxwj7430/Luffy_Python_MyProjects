names = []
names.append('old_driver')
names.append('rain')
names.append('jack')
names.append('shanshan')
names.append('peiqi')
names.append('black_girl')
names.insert(-1, 'alex')
names[names.index('shanshan')] = '姗姗'
names.insert(names.index('rain') + 1, ['oldboy', 'oldgirl'])
names.index('peiqi')
new_li = [1, 2, 3, 4, 2, 5, 6, 2]
names.extend(new_li)
print(names[4:8])
print(names[2:11:2])
print(names[-3:])
print(names)

# count = 0
# for i in names:
#     if count % 2 == 0:
#         i = -1
#     print(count, i)
#     count += 1

first = names.index(2)  # 找到第一个2的位置
print(first)
second = names[(first+1):].index(2)  # 找到第二个2在切片中的位置
print(first + second + 1)
