import math
product =1
for i in range (1,11):
	product *= i

for i in range(2,11):
	while product%i ==0:
		dividableNum = True
		for x in range (1,11):
			if (product/i)/x != 0:
				dividableNum = False
		if dividableNum:
			product = product/i
	

print(product)