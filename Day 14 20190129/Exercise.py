# 1. 请用代码实现： 利用下划线将列表的每一个元素拼接成字符串， li = ['alex', 'eric', 'rain']
# li = ['alex', 'eric', 'rain']
# print('_'.join(li))

# 2. 查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素
#
# li = ["    a  l  e  c   ", "  a r i  c ", "A     l    e   x", "T  o  n  y      ", "   r  a  i  n "]
# li_join = '_'.join(li)
# new_li = li_join.replace(' ', '')
# check_li = new_li.split('_')
#
# for i in check_li:
#     if i.startswith('a') or i.startswith('A') and i.endswith('c'):
#         print(i)

# 3. 写代码，有如下列表，按照要求实现每一个功能

# li = ['alex', 'eric', 'rain']
# print(len(li))
#
# li.append('seven')
# print(li)
#
# li.insert(0, 'Tony')
# print(li)
#
# li[1] = 'Kelly'
# print(li)

# li.remove('eric')
# print(li)
#
# li.pop(1)
# print(li)
#
# del li[2]
# print(li)

# del li[1:4]
# print(li)

# li.reverse()
# print(li)

# for i in range(len(li)):
#     print(i)

# for index, i in enumerate(li, start=100):
#     print(index, i)
#
# for i in li:
#     print(i)

# 4. 写代码，有如下列表，按照要求实现每一个功能
# li = ['hello', 'seven', ['mon', ['h', 'kelly'], 'all'], 123, 446]
# print(li[2][1][1])
#
# li[2][2] = 'ALL'
# print(li)

# 4. 写代码，有如下元组，按照要求实现每一个功能
tu = ('alex', 'eric', 'rain')

# print(len(tu))
# print(tu[1])
# print(tu[0:2])
#
# for i in tu:
#     print(i)

# for i in range(len(tu)):
#     print(i)
#
# for index, i in enumerate(tu, start=10):
#     print(index, i)

# 6. 有如下变量，请实现要求的功能
# tu = ('alex', [11, 22, {'k1': 'v1', 'k2': ['age', 'name'], 'k3': (11, 22, 33)}, 44])

# 元组可存放多个值，元组中的值不可变，但是如果元组里面还有列表、元组、字典等就可变，属于浅不可变

# tu[0] = 'ALEX'
# 不可变

# 'k2'对应的值是一个列表['age', 'name']，可变
# tu[1][2]['k2'].append('Seven')
# print(tu)

# 'k3'对应的值是一个子元组，可变
# tu[1][2]['k3'] = (11, 22, 33, 'Seven')
# print(tu)

# 7. 字典
# dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11, 22, 33]}
# for i in dic.keys():
#     print(i)
#
# for i in dic.values():
#     print(i)

# for key,value in enumerate(dic):
#     print(key, value)
#
# dic.setdefault('k4', 'v4')
# print(dic)
#
# dic['k1'] = 'alex'
# print(dic)
#
# dic['k3'].append(44)
# print(dic)
#
# dic['k3'].insert(0, 18)
# print(dic)

# 8. 转换
# s = 'alex'
# li = [s]
# print(li)
# tu = (s)
# print(tu)
#
# li = ['alex', 'seven']
# tu = (li[0], li[1])
# tu2 = tuple(li)
# print(tu)
# print(tu2)
#
# tu = ('alex', 'seven')
# li = [tu[0], tu[1]]
# li2 = list(tu)
# print(li)
# print(li2)
#
# li = ['alex', 'seven']
# new_dict = {}
# for index, i in enumerate(li, start=10):
#     new_dict[index] = i
#
# print(new_dict)

# 9. 元素分类

# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {'k1': [], 'k2': []}
# for i in li:
#     if i > 66:
#         dic['k1'].append(i)
#     elif i < 66:
#         dic['k2'].append(i)
#
# print(dic)

