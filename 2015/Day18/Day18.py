import numpy as np

def next_step(grid):
	for corner in corners:
		grid[corner[0], corner[1]] = 1
	new_grid = np.copy(grid)
	for r in range(grid.shape[0]):
		for c in range(grid.shape[1]):
			lr = 0 if r == 0 else r - 1
			hr = grid.shape[0] - 1 if r == grid.shape[0] - 1 else r + 1
			lc = 0 if c == 0 else c - 1
			hc = grid.shape[1] - 1 if c == grid.shape[1] - 1 else c + 1
			lights_on = np.sum(grid[lr:hr + 1, lc:hc + 1])
			if grid[r][c] == 1:
				if not (lights_on - 1 == 2 or lights_on - 1 == 3):
					new_grid[r][c] = 0
			else:
				if lights_on == 3:
					new_grid[r][c] = 1
	return new_grid

data = open("Day18.txt").readlines()

grid = []
for line in data:
	line = line.strip()
	row = []
	for c in line:
		if c == "#":
			row.append(1)
		elif c == ".":
			row.append(0)
	grid.append(row)

grid = np.array(grid)
corners = ((0, 0), (0, grid.shape[1] - 1), (grid.shape[0] - 1, grid.shape[1] - 1), (grid.shape[0] - 1, 0))
for i in range(100):
	grid = next_step(grid)

for corner in corners:
	grid[corner[0], corner[1]] = 1
print(np.sum(grid))
