products = [['iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]

print('------------商品列表-----------')

for index, i in enumerate(products):
    print('%s. %s  %s' % (index, i[0], i[1]))

