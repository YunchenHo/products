products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

print(products[0][0])
print(products[1][1])

for p in products: #p=小清單
	print(p[0], '的價格是', p[1])