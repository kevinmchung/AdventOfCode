import re
import numpy as np

grid = np.zeros((6, 50))

data = open("Day8.txt", "r").read().split("\n")

for line in data:
	rect = re.match("rect (\d+)x(\d+)", line)
	rot = re.match("rotate (row|column) [xy]=(\d+) by (\d+)", line)
	p = re.split("[ =]", line)
	if rect:
		bounds = rect.groups()
		grid[:int(bounds[1]), :int(bounds[0])] = 1
	elif rot:
		d = rot.groups()
		idx = int(d[1])
		shift = int(d[2])
		if d[0] == "row":
			grid[idx, :] = np.roll(grid[idx, :], shift)
		elif d[0] == "column":
			grid[:, idx] = np.roll(grid[:, idx], shift)

print(np.sum(grid))
for r in range(grid.shape[0]):
	for c in range(grid.shape[1]):
		if grid[r][c]:
			print("#", end="")
		else:
			print(".", end="")
	print()

