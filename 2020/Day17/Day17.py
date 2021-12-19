# Part 1: 545
# Part 2: 383

from collections import defaultdict
from copy import deepcopy

def next_cycle(grid):
	for i in range(4):
		grid_size[i][0] -= 1
		grid_size[i][1] += 1

	new_grid = defaultdict(lambda: ".")

	d = [-1, 0, 1]

	for x in range(*grid_size[0]):
		for y in range(*grid_size[1]):
			for z in range(*grid_size[2]):
				for w in range(*grid_size[3]):
					active_neighbors = 0
					for dx in d:
						for dy in d:
							for dz in d:
								for dw in d:
									if not(dx == 0 and dy == 0 and dz == 0 and dw == 0):
										if grid[(x + dx, y + dy, z + dz, w + dw)] == "#":
											active_neighbors += 1
					if grid[(x, y, z, w)] == "#":
						if active_neighbors != 2 and active_neighbors != 3:
							new_grid[(x, y, z, w)] = "."
						else:
							new_grid[(x, y, z, w)] = "#"
					else:
						if active_neighbors == 3:
							new_grid[(x, y, z, w)] = "#"
						else:
							new_grid[(x, y, z, w)] = "."

	return new_grid


data = open("Day17.txt", "r").read().split("\n")
# data = list(map(int, data))

grid = defaultdict(lambda: ".")
grid_size = [[0, 8], [0, 8], [0, 1], [0, 1]]

print(data)
for y in range(len(data)):
	for x in range(len(data[y])):
		grid[(x, y, 0, 0)] = data[y][x]

print(grid)
for i in range(6):
	grid = next_cycle(grid)
	print(grid_size)

print(sum(i == "#" for i in grid.values()))
