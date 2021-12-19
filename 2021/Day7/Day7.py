from collections import defaultdict

lines = [line.strip() for line in open("Day7.txt", "r")]
# lines = list(map(int, lines))

crabs = lines[0].split(",")
crabs = list(map(int, crabs))

def tri(n):
	return n * (n + 1) // 2

small = 1000000000000000000000000
for i in range(max(crabs)):
	tot = 0
	for c in crabs:
		tot += tri(abs(c - i))
	if tot < small:
		small = tot
print(small)