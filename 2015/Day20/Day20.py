import math
from collections import defaultdict

def prime_factorize(n):
	factors = defaultdict(int)
	i = 2
	while i <= math.sqrt(n):
		while n % i == 0:
			n //= i
			factors[i] += 1
		i += 1
	if n > 1:
		factors[n] += 1
	return factors

def sum_divisors(n):
	factors = prime_factorize(n)
	out = 1
	for f in factors:
		s = 0
		for i in range(factors[f] + 1):
			s += f ** i
		out *= s
	return out

def sum_divisors2(n):
	factors = prime_factorize(n)
	out = 1
	for f in factors:
		s = 0
		for i in range(factors[f] + 1):
			s += f ** i
		out *= s
	j = 1
	while j <= n / 50:
		if n % j == 0:
			out -= j
		j += 1
	return out


target = 33100000

n = 776160
while sum_divisors2(n) * 11 < target:
	# print(sum_divisors2(n) * 11)
	n += 1

print(n)