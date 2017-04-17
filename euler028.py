# Project Euler Problem #28

diagSum = 1
diagonal = 1
increment = 1

for i in range(1,501):
	increment = i
	for j in range(1,5):
		diagonal += 2*increment
		diagSum += diagonal

print diagSum

# The answer is 669171001