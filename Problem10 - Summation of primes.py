import math
def isprime (n):
	if n == 1:
		return False
	elif n<4 :
		return True
	elif n%2 ==0:
		return False
	elif n<9:
		return True
	elif n%3 ==0:
		return False
	else:
		r = 5
		while r <= math.ceil(math.sqrt(n)):
			if n%r == 0:
				return False
			if n%(r+2) ==0:
				return False
			r=r+6

	return True

sumofPrimes = 0

for i in range (1,2000001):
	if isprime(i):
		sumofPrimes += i
print(sumofPrimes)