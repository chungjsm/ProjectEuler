# Project Euler Problem #6

def squareOfSum(n):
	total = 0
	for i in range(1, n+1):
		total += i
	total = total**2
	return total

def sumOfSquare(n):
	total = 0
	for i in range(1, n+1):
		total += i**2
	return total

print squareOfSum(100) - sumOfSquare(100)