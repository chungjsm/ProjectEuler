# Project Euler Problem #21

def amicableNum(n):
	amicableSum = 0
	for i in range(1,n):
		if sumDivisors(sumDivisors(i)) == i and sumDivisors(i) != i:
			print i
			amicableSum += i
	return amicableSum

def sumDivisors(n):
	sumDiv = 0
	for i in range(1,n):
		if n % i == 0:
			sumDiv += i
	return sumDiv

print "The sum is " + str(amicableNum(10000))