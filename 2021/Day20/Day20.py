import sys
from collections import defaultdict

lines = [line.strip() for line in open("Day20.txt")]
s = lines[0]

size = [[0, len(lines)], [0, len(lines[2])]]
grid = defaultdict(lambda: ".")
for i in range(2, len(lines)):
	line = lines[i]
	for c in range(len(lines[i])):
		grid[(i - 2, c)] = line[c]

for i in range(50):
	newgrid = defaultdict(lambda: (s[-1], s[0])[i % 2])
	for k in grid:
		newgrid[k] = grid[k]
	size[0][0] -= 2
	size[0][1] += 2
	size[1][0] -= 2
	size[1][1] += 2
	for r in range(*size[0]):
		for c in range(*size[1]):
			bs = ""
			for dr in [-1, 0, 1]:
				for dc in [-1, 0, 1]:
					bs += grid[(r + dr, c + dc)]
			bs = bs.replace(".", "0")
			bs = bs.replace("#", "1")
			newgrid[(r, c)] = s[int(bs, 2)]
	grid = newgrid

n = 0
for k in grid:
	n += (grid[k] == "#")
print(n)