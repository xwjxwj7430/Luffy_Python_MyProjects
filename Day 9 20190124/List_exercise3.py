li = ['alex', 'eric', 'rain']

# 计算列表长度并输出
print(len(li))

# 列表中追加元素"seven",并输出添加后的列表
li.append("seven")
print(li)

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
