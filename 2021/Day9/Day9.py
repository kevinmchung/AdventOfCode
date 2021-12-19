lines = [line.strip() for line in open("Day9.txt", "r")]
grid = [list(map(int, list(line))) for line in lines]

ans = 0
lows = []
for r in range(len(grid)):
	for c in range(len(grid[r])):
		val = grid[r][c]
		low = True
		for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
			if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[r]):
				if grid[r + dr][c + dc] <= val:
					low = False
		if low:
			ans += val + 1
			lows.append((r, c))
print(ans)

largest = [0, 0, 0]
for lr, lc in lows:
	visited = {(lr, lc)}
	q = [(lr, lc)]
	while len(q) > 0:
		r, c = q.pop(0)
		for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
			if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[r]):
				if (r + dr, c + dc) not in visited and grid[r + dr][c + dc] != 9 and grid[r + dr][c + dc] > grid[r][c]:
					q.append((r + dr, c + dc))
					visited.add((r + dr, c + dc))
	if len(visited) > min(largest):
		largest[largest.index(min(largest))] = len(visited)


print(largest[0] * largest[1] * largest[2])