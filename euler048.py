# Project Euler Problem #48

sumOfTerms = 0

for i in range(1, 1001):
	sumOfTerms += i**i

strSum = str(sumOfTerms)
substrSum = strSum[-10:len(strSum)]

print substrSum