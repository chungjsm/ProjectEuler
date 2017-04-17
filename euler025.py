# Project Euler Problem #25

x = 1
y = 1
z= 0
counter = 2
strNum = str(y)

while len(strNum) < 1000:
	z = x
	x = y
	y = z + x
	counter += 1
	strNum = str(y)

print counter