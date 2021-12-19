import sys
import re
import math

sys.setrecursionlimit(30000)

def spread(x, y, d, grid):
	if grid[y][x] == ".":
		grid[y][x] = "|"
	if y == len(grid) - 1:
		return
	if grid[y][x] == "#":
		return x
	if grid[y + 1][x] == ".":
		spread(x, y + 1, 0, grid)
	if grid[y + 1][x] == "#" or grid[y + 1][x] == "~":
		if d:
			return spread(x + d, y, d, grid)
		else:
			left = spread(x - 1, y, -1, grid)
			right = spread(x + 1, y, 1, grid)
			if grid[y][left] == "#" and grid[y][right] == "#":
				for x_fill in range(left + 1, right):
					grid[y][x_fill] = "~"
	else:
		return x

data = open("Day17.txt", "r").read().split("\n")

x_min = math.inf
x_max = 0
y_min = math.inf
y_max = 0

d = []
for line in data:
	a, b, c = map(int, re.findall("\d+", line))
	if line[0] == "x":
		d.append((a, a, b, c))
	else:
		d.append((b, c, a, a))

Z = list(zip(*d))
x_min, x_max, y_min, y_max = min(Z[0]), max(Z[1]), min(Z[2]), max(Z[3])

grid = [['.']*(x_max - x_min + 4) for i in range(y_max + 1)]
for x1, x2, y1, y2 in d:
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			grid[y][x - x_min + 2] = "#"
spring = (500 - x_min + 2, 0)
grid[spring[1]][spring[0]] = "+"

spread(spring[0], spring[1], 0, grid)

still = 0
flowing = 0
for y in range(y_min, y_max + 1):
	for x in range(len(grid[0])):
		if grid[y][x] == "~":
			still += 1
		elif grid[y][x] == "|":
			flowing += 1

print(still + flowing, still)


