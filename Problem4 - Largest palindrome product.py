maxPal = 0
for i in range (100,1000):
	for x in range (i, 1000):
		product = x*i
		if str(product) == str(product)[::-1]:
			if product > maxPal:
				maxPal = product
print(maxPal)