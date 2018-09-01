#检查档案在不在
import os
products = []
if os.path.isfile('products.csv'):
	print("找到档案")
	#读取档案部分
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到档案')

#输入部分						
while True:
	name = input('请输入商品名称: ')
	if name == 'q':
		break
	price = input('请输入价格: ')
	products.append([name, price])
print(products)

#印出交易记录
for p in products:
	print(p[0], '的价格是', p[1])

#储存部分
with open('products.csv', 'w', encoding = 'utf-8') as f:		
	f.write('商品,价格\n')
	for p in products:						
		f.write(p[0] + ',' + p[1] + '\n')			