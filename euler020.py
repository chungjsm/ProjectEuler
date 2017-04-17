# Project Euler Problem #20

def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

strFactorial = str(factorial(100))

sumOfDigits = 0

for i in strFactorial:
	sumOfDigits += int(i)

print sumOfDigits