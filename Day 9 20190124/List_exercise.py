# 请用代码实现： 利用下划线将列表的每一个元素拼接成字符串， li = ['alex', 'eric', 'rain']

li = ['alex', 'eric', 'rain']
all = ''
for i in range(2):
    print(li[i])
    all = all + li[i] + '_'

all = all + li[2]
print(all)
