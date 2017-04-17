# Project Euler Problem #4

def isPalindrome(n):
	num = str(n)
	if len(num) > 1:
		if num[0] == num[-1]:
			return isPalindrome(num[1:-1])
		else:
			return False
	else:
		return True

sumOf = 0

for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		if isPalindrome(i*j):
			if i*j > sumOf:
				sumOf = i*j
				print sumOf