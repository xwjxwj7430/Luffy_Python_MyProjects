# 每⼀句对应的内容：序号,姓名,年龄,⼿机号,部分,⼊职时间
#
# 1,Alex Li,22,13651054608,IT,2013-04-01
# 2,Jack Wang,28,13451024608,HR,2015-01-07
# 3,Rain Wang,21,13451054608,IT,2017-04-01
# 4,Mack Qiao,44,15653354208,Sales,2016-02-01
# 5,Rachel Chen,23,13351024606,IT,2013-03-16
# 6,Eric Liu,19,18531054602,Marketing,2012-12-01
# 7,Chao Zhang,21,13235324334,Administration,2011-08-08
# 8,Kevin Chen,22,13151054603,Sales,2013-04-01
# 9,Shit Wen,20,13351024602,IT,2017-07-03
# 10,Shanshan Du,26,13698424612,Operation,2017-07-02

staff_list = []
f = open('staff_table', mode="r+", encoding='utf-8')

data = f.read()
print(data)

row = data.split('\n')
for i in row:
    staff_list.append(i.split(','))
    print(i)

print(staff_list)


def read_file(where):
    staff_list = []
    f = open('%s' % where, mode="r+", encoding='utf-8')
    data = f.read()
    # print(data)
    row = data.split('\n')
    for staff in row:
        staff_list.append(staff.split(','))
        print(staff)

    return staff_list