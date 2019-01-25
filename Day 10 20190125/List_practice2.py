products = [['iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]

print('------------商品列表-----------')

count = 0
for i in products:
    print('%s. %s  %s' % (count, i[0], i[1]))
    count += 1

