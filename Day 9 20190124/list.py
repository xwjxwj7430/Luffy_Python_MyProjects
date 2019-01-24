names = list()
print(names)

naems = []
print(names)

names = ['aA', 'b', 'c', 'f', 'e', 'z', 'g', 'A', 'C', 'D', 'Z', 'B', 'Q']
names.reverse()
print(names)

name2 = [1, 2, 3, 4, 9, 4, 3]
name2.sort()
print(name2)

name3 = names + name2
print(name3)

name4 = names.extend(name2)

names.insert(3, '#')
names.insert(1, '*')
names.insert(3, '/')

names.copy()

n2 = names
n1 = names.copy()
names[2] = 'Alex'

print(n2)
print(n1)

# names = ['jack', 'nick', 123, 123, 1, 1, 2, 2, 3, 3, 3e2, [1, 2, 3]]

#
#
# names[2] = 999
# print(names)
# names[8:9] = '999'
# print(names)
#
# for i in names:
#     print(i)



# print(names[2:-1:3])
# print(names[2::3])
#
# names.append('peiqi')
# print(names)
# names.insert(0, 'abc')
# print(names[0])
# names.insert(3, 'efg')
# print(names[3])
# print(names)
# print(names)
#
# print(names[1])
#
# print(names[2])
#
# print(names[4])
#
# print(names[-1])
#
# print(names[-2])
#
# a = names.index('jack')
# print(a)
#
# b = names.index(1)
# print(b)
#
# c = names[names.index('jack')]
# print(c)
#
# d = names.count('jack')
# print(d)
#
# e = names.count(3)
# print(e)
