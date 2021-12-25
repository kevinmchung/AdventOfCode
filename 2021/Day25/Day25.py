from collections import defaultdict

grid = [list(line.strip()) for line in open("Day25.txt")]

i = 0
while True:
	moved = 0
	egrid = [[s for s in r] for r in grid]
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == ">":
				rightc = (c + 1) % len(grid[r])
				if grid[r][rightc] == ".":
					egrid[r][c] = "."
					egrid[r][rightc] = ">"
					moved += 1
	sgrid = [[s for s in r] for r in egrid]
	for r in range(len(egrid)):
		for c in range(len(egrid[r])):
			if egrid[r][c] == "v":
				downr = (r + 1) % len(egrid)
				if egrid[downr][c] == ".":
					sgrid[r][c] = "."
					sgrid[downr][c] = "v"
					moved += 1
	grid = sgrid
	i += 1
	if moved == 0:
		print(i)
		break
