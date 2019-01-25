products = [['iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
cart = []

print('------------商品列表-----------')

count = 0
for i in products:
    print('%s. %s  %s' % (count, i[0], i[1]))
    count += 1

print('------------商品列表-----------')

while True:
    add_to_cart = input('请问您想买几号商品：')
    if add_to_cart.isdigit():
        cart.append(products[int(add_to_cart)])
    elif add_to_cart == 'q':
        break
    print('您目前购物车内的商品为 ', cart)

print('------------结账清单-----------')

count = 1
for j in cart:
    print('%s. %s  %s' % (count, j[0], j[1]))
    count += 1

print('------------结账清单-----------')









