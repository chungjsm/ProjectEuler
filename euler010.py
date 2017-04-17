# Project Euler Problem #10
# Find the sum of all the primes below two million.

import sympy

primeSum = 0


for num in range(1,2000000):
	if sympy.isprime(num):
		primeSum += num

print primeSum