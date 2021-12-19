import re
from collections import defaultdict

data = open("Day3.txt", "r").read().split("\n")

grid = defaultdict(list)

for line in data:
	n, x, y, w, h = map(int, re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line).groups())
	for i in range(w):
		for j in range(h):
			grid[(x + i, y + j)].append(n)

total = 0
for key in grid:
	if len(grid[key]) >= 2:
		total += 1
print(total)

for line in data:
	n, x, y, w, h = map(int, re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line).groups())
	matches = False
	for i in range(w):
		for j in range(h):
			if len(grid[(x + i, y + j)]) > 1:
				matches = True
	if not matches:
		print(n)
		break
