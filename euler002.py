# Project Euler Problem #2

def fibonacci(n):
	x= 0
	y = 1
	num = 0
	while y <= n:
		z = x
		x = y
		y = z + x
		if y % 2 == 0:
			num += y
	print num

fibonacci(4000000)