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
	

x = 1
counter = 1
while x<=10001 :
	if isprime(counter) :
		x=x+1
	counter=counter+1

print (counter-1)