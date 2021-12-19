# Part 1: 58
# Part 2: 263

import numpy as np
data = open("Day11.txt", "r").read().split("\n")
# data = list(map(int, data))

def next_step(grid):
	new_grid = np.copy(grid)
	for r in range(grid.shape[0]):
		for c in range(grid.shape[1]):
			if grid[r][c] != 0:
				lr = 0 if r == 0 else r - 1
				hr = grid.shape[0] - 1 if r == grid.shape[0] - 1 else r + 1
				lc = 0 if c == 0 else c - 1
				hc = grid.shape[1] - 1 if c == grid.shape[1] - 1 else c + 1
				seats_occ = np.count_nonzero(grid[lr:hr + 1, lc:hc + 1] == 2)
				if grid[r][c] == 2:
					if seats_occ - 1 >= 4:
						new_grid[r][c] = 1
				elif grid[r][c] == 1:
					if seats_occ == 0:
						new_grid[r][c] = 2
	return new_grid

def count_visible(grid, r, c):
	d = [-1, 0, 1]
	total = 0
	for dr in d:
		for dc in d:
			if not (dr == 0 and dc == 0):
				i = 1
				while 0 <= r + dr * i < grid.shape[0] and 0 <= c + dc * i < grid.shape[1]:
					if grid[r + dr * i][c + dc * i] == 1:
						break
					if grid[r + dr * i][c + dc * i] == 2:
						total += 1
						break
					i += 1
	return total

def next_step2(grid):
	new_grid = np.copy(grid)
	for r in range(grid.shape[0]):
		for c in range(grid.shape[1]):
			if grid[r][c] != 0:
				seats_occ = count_visible(grid, r, c)
				if grid[r][c] == 2:
					if seats_occ >= 5:
						new_grid[r][c] = 1
				elif grid[r][c] == 1:
					if seats_occ == 0:
						new_grid[r][c] = 2
	return new_grid

grid = np.zeros((len(data), len(data[0])))

for r in range(len(data)):
	for c in range(len(data[0])):
		if data[r][c] == ".":
			grid[r][c] = 0
		elif data[r][c] == "L":
			grid[r][c] = 1
		else:
			grid[r][c] = 2

while True:
	prev_grid = np.copy(grid)
	grid = next_step2(grid)
	if np.array_equal(grid, prev_grid):
		break


print(np.count_nonzero(grid == 2))