isbreak = False
for a in range(1,333):
	for c in range(333,500):
		b = 1000-a-c
		if a**2 + b**2 == c**2:
			print (a ,b,c)
			isbreak = True
			break
		else:
			continue
	if isbreak	:
		break
print(a*b*c)
