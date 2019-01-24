# 查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。

li = ["al ec ", "ari  c", "A   le     x", "Ton  y", "r  ai n"]

tu = ("alec", "aric", "Alex", "Tony", "rain")

dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

# 分析：因为列表中的空格在每个元素中，无法识别，不能删除，所以首先将每个元素内部分开，把空格识别并删除，最后再将其合并成新元素

li_new = []
num_li = len(li)  # 首先得到li中的元素个数，看整个循环要循环几次

for i in range(num_li):
    split = []  # 首先为了利用批量修改元素值的特性将每个元素内部进行分离，定义一个空列表
    split[0:] = li[i]  # 通过这一步,原来列表中的"al ec "，被变为"a", "l", " ", "e", "c", " "6个元素替代到split中

    while split.count(' ') > 0:  # 当split中有空格元素时，就进行删除，直到空格没有为止
        split.remove(' ')
    print(split)  # 中途显示一下中间结果，验证一下是否正确，空格是否已全部删除

    merge = ''  # 将merge赋值为空的字符串，方便后续利用前一个练习的合并字符串的技巧
    num_split = len(split)  # 首先要直到for要循环几次，循环的次数就是split中的英文字母的个数，用len()求个数
    for j in range(num_split):
        merge = merge + split[j]  # 将所有单个英文字母合并成一个字符串，并打印看结果
    print(merge)

    li_new.append(merge)  # 再把拼接好的单词添加到空白的列表当中，添加循环完成后，新列表应当包含没有空格的len(li)个元素

print(li_new)       # 看一下新列表是不是符合要求

for k in range(len(li_new)):        # 将新的列表拆开看首尾字母，方法同前面一样
    split = []
    split[0:] = li_new[k]
    if split[0] == 'a' or split[0] == 'A':
        if split[-1] == 'c':
            print(li_new[k])
