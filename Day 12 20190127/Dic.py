# dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
#
# for k in dic.keys():
#     print(k)
#
# for v in dic.values():
#     print(v)
#
# for k, v in dic.items():
#     print(k, v)
#
# for k in dic:
#     print(k, dic[k])
#
#
# dic['k4'] = 'v4'
# print(dic)
#
# dic.pop('k1')
# print(dic)
#
# dic.pop('k5', 'None')
#
# dic['k2']
#
# dic.get('k6', 'None')
#
# dic2 = {'k1': 'v111', 'a': 'b'}
# dic2.update(dic)
#
# lis = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
#
# lis[0][1][2]['k1'][0] = 'TT'
#
# lis[0][1][2]['k1'][0] = lis[0][1][2]['k1'][0].upper()
#
# dic2 = {'k1': ['TT', 3, '1']}
# lis[0][1][2].update(dic2)
#
# lis[0][1][2]['k1'][1] = '100'
# dic2 = {'k1': ['tt', '100', '1']}
# lis[0][1][2].update(dic2)
#

li = [1, 2, 3, 'a', 'b', 4, 'c']
dic = {}
if dic.get('k1') is None:
    dic.setdefault('k1', [])
    for i in li:
        if li.index(i) % 2 != 0:
            dic['k1'].append(i)

elif type(dic['k1']) is list:
    for i in li:
        if li.index(i) % 2 != 0:
            dic['k1'].append(i)
