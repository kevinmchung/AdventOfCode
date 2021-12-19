import re

bots = []
data = open("Day23.txt", "r").read().split("\n")

largest_r = 0
largest_bot = None
for line in data:
	x, y, z, r = map(int, re.findall("-?\d+", line))
	bots.append(((x, y, z), r))
	if r > largest_r:
		largest_r = r
		largest_bot = ((x, y, z), r)

total = 0
for bot in bots:
	if abs(bot[0][0] - largest_bot[0][0]) + abs(bot[0][1] - largest_bot[0][1]) + abs(bot[0][2] - largest_bot[0][2]) <= largest_bot[1]:
		total += 1
print(total)

from z3 import *

o = Optimize()

def zabs(n):
	return If(n >= 0, n, -n)

x, y, z = Int("x"), Int("y"), Int("z")

in_ranges = [Int("in_range_" + str(i)) for i in range(len(bots))]
range_count = Int("sum")

for i in range(len(bots)):
	(nx, ny, nz), r = bots[i]
	o.add(in_ranges[i] == If(zabs(x - nx) + zabs(y - ny) + zabs(z - nz) <= r, 1, 0))

o.add(range_count == sum(in_ranges))
dist_from_zero = Int("dist")

o.add(dist_from_zero == zabs(x) + zabs(y) + zabs(z))

h1 = o.maximize(range_count)
h2 = o.minimize(dist_from_zero)

print(o.lower(h2))
