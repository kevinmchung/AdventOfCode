d = (-1, 0, 1)

def next_step(grid):
	new_grid = []
	for r in range(len(grid)):
		new_row = ""
		for c in range(len(grid[0])):
			counts = {".":0, "|":0, "#":0}
			for dr in d:
				for dc in d:
					if not (dr == 0 and dc == 0) and 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
						counts[grid[r + dr][c + dc]] += 1
			if grid[r][c] == ".":
				if counts["|"] >= 3:
					new_row += "|"
				else:
					new_row += "."
			elif grid[r][c] == "|":
				if counts["#"] >= 3:
					new_row += "#"
				else:
					new_row += "|"
			elif grid[r][c] == "#":
				if counts["|"] >= 1 and counts["#"] >= 1:
					new_row += "#"
				else:
					new_row += "."
		new_grid.append(new_row)
	return tuple(new_grid)

grid = tuple(open("Day18.txt", "r").read().split("\n"))

n = 1000000000
seen = []
for i in range(n):
	grid = next_step(grid)
	if grid in seen:
		j = seen.index(grid)
		n -= 1 # convert to index
		n = (n - i) % (i - j)
		grid = seen[j + n]
		break
	else:
		seen.append(grid)

trees = 0
lumberyards = 0
for r in grid:
	for c in r:
		if c == "|":
			trees += 1
		elif c == "#":
			lumberyards += 1

print(trees * lumberyards)