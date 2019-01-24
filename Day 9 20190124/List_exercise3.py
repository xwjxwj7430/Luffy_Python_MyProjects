li = ['alex', 'eric', 'rain']

# 计算列表长度并输出
print(len(li))

# 列表中追加元素"seven",并输出添加后的列表
li.append("seven")
print(li)

li = ['alex', 'eric', 'rain']
# 请在列表的第一个位置插入元素“Tony”，并输出添加后的列表
li.insert(0, 'Tony')
print(li)

# 请修改列表第2个位置的元素为"Kelly"，并输出修改后的列表
li[1] = "Kelly"
print(li)

# 请删除列表中的元素"eric"，并输出修改后的列表
li.remove("eric")
print(li)

# 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
ele_deleted = li.pop(1)
print(ele_deleted)
print(li)

# 请删除列表中的第3个元素，并输出删除元素后的列表
li = ['alex', 'eric', 'rain']
del li[2]
print(li)

# 请删除列表中的第2-4个元素，并输出删除元素后的列表
li.append("alex")
li.append("seven")
li.append("eric")
print(li)
del li[1:4]
print(li)

# 请将列表所有的元素反转，并输出反转后的列表
li = ['alex', 'eric', 'rain']
li.reverse()
print(li)

# 请使用for、len、range输出列表的索引
for i in range(len(li)):
    print(i)

# 请使用enumerate输出列表元素和序号（序号从100开始）
for i, element in enumerate(li, start=100):
    print(i, element)

# 请使用for循环输出列表的所有元素:
for i in range(len(li)):
    print(li[i])