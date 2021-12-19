import numpy as np

adj = ((1, 0), (-1, 0), (0, 1), (0, -1))

def next_step(grid):
	new_grid = [row for row in grid]
	for r in range(5):
		for c in range(5):
			bugs = 0
			for dr, dc in adj:
				nr, nc = r + dr, c + dc
				if 0 <= nr < 5 and 0 <= nc < 5:
					if grid[nr][nc] == "#":
						bugs += 1
			if grid[r][c] == "#" and bugs != 1:
				new_grid[r] = new_grid[r][:c] + "." + new_grid[r][c + 1:]
			if grid[r][c] == "." and (bugs == 1 or bugs == 2):
				new_grid[r] = new_grid[r][:c] + "#" + new_grid[r][c + 1:]
	return tuple(new_grid)

def next_step2(np_grid, zero):
	new_grid = np.concatenate((np.zeros((1, 5, 5), dtype=int), np.copy(np_grid), np.zeros((1, 5, 5), dtype=int)))
	zero += 1
	for d in range(new_grid.shape[0]):
		for r in range(5):
			for c in range(5):
				if not (r == 2 and c == 2):
					bugs = 0
					for dr, dc in adj:
						nr, nc = r + dr, c + dc
						if 0 <= nr < 5 and 0 <= nc < 5:
							if nr == 2 and nc == 2 and d > 1:
								if r == 1 and c == 2:
									bugs += np.sum(np_grid[d - 2, 0, :])
								elif r == 3 and c == 2:
									bugs += np.sum(np_grid[d - 2, 4, :])
								elif r == 2 and c == 1:
									bugs += np.sum(np_grid[d - 2, :, 0])
								elif r == 2 and c == 3:
									bugs += np.sum(np_grid[d - 2, :, 4])
							elif 0 <= d - 1 < np_grid.shape[0]:
								bugs += np_grid[d - 1, nr, nc]
						elif d < new_grid.shape[0] - 2:
							if nr < 0:
								bugs += np_grid[d, 1, 2]
							elif nr >= 5:
								bugs += np_grid[d, 3, 2]
							elif nc < 0:
								bugs += np_grid[d, 2, 1]
							elif nc >= 5:
								bugs += np_grid[d, 2, 3]

					if 0 <= d - 1 < np_grid.shape[0]:
						val = np_grid[d - 1, r, c]
					else:
						val = 0

					if val == 1 and bugs != 1:
						new_grid[d, r, c] = 0
					if val == 0 and (bugs == 1 or bugs == 2):
						new_grid[d, r, c] = 1

	return new_grid, zero


grid = tuple(open("Day24.txt", "r").read().split("\n"))

np_grid = np.zeros((1, 5, 5), dtype=int)
for r in range(len(grid)):
	for c in range(len(grid[0])):
		if grid[r][c] == "#":
			np_grid[0][r][c] = 1

seen = {grid}
while True:
	grid = next_step(grid)
	if grid in seen:
		break
	seen.add(grid)

# print(grid)
out = ""
for r in range(len(grid)):
	for c in range(len(grid[0])):
		out += str(int(grid[r][c] == "#"))

out = out[::-1]
print(int(out, 2))

zero = 0
for i in range(200):
	np_grid, zero = next_step2(np_grid, zero)
print(np.sum(np_grid))