import time
import math
def isprime (n):
	if n == 1:
		return False
	elif n == 2 or n == 3 :
		return True

	else:
		for i in range (2,int(math.sqrt(n))):
			if n%i == 0:
				return False
			else:
				pass
		return True

number = 600851475143
boudnd = 775146
maxprime = 0
total =0
for i in range (2,boudnd):
	if number%i == 0:
		x = number/i
		if isprime(i) and i >maxprime:
			maxprime = i
		if isprime (x) and x>maxprime:
			maxprime = x
print (maxprime)