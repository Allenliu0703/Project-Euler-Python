Fibonacci = [1,2]
sum = 2
x = Fibonacci[-1]+Fibonacci[-2]
while x  < 4000000 :
	Fibonacci.append(x)
	if x % 2 == 0:
		sum = sum + x

	x = Fibonacci[-1]+Fibonacci[-2]
	
print (sum) 