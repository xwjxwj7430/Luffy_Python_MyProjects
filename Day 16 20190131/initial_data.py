# userdata.txt中的字典数据结构如下：
# 第一个key值为用户名，用户名下面的子字典的password存储密码，history存储购买记录，balance存储上次购买后的余额

f = open('userdata.txt', 'w', encoding='utf-8')
user_data = {'alex': {'password': 'shuai', 'history': [0, 1, 0, 3], 'balance': 5000},
             'eric': {'password': 'ge', 'history': [0, 1], 'balance': 50},
             'john': {'password': 'jiu', 'history': [0], 'balance': 0},
             'nick': {'password': 'shi', 'history': [], 'balance': 0},
             }
f.write(str(user_data))
f.close()

# goodslist.txt中的字典数据结构如下：
f = open('goodslist.txt', 'w', encoding='utf-8')

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

f.write(str(goods))
f.close()
