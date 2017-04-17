# Project Euler Problem #5

def isDivisible(num):
	for i in range(11,21):
		if num % i != 0:
			return False
	return True

# set the initial number to the product of all primes from 1-20
num = 3*5*7*11*13*17*19

while not isDivisible(num):
	num += 3*5*7*11*13*17*19

print num