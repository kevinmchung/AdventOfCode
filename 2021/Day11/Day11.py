grid = [list(map(int, line.strip())) for line in open("Day11.txt", "r")]

ans = 0
i = 0
while True:
	i += 1
	visited = set()
	fq = []
	for r in range(10):
		for c in range(10):
			grid[r][c] += 1
			if grid[r][c] > 9:
				fq.append((r, c))
				visited.add((r, c))
	while len(fq):
		r, c = fq.pop(0)
		for dr in range(-1, 2):
			for dc in range(-1, 2):
				if not (dr == 0 and dc == 0) and 0 <= r + dr < 10 and 0 <= c + dc < 10:
					grid[r + dr][c + dc] += 1
					if grid[r + dr][c + dc] > 9 and (r + dr, c + dc) not in visited:
						fq.append((r + dr, c + dc))
						visited.add((r + dr, c + dc))
	if len(visited) == 100:
		print(i)
		break
	ans += len(visited)
	for r, c in visited:
		grid[r][c] = 0

print(ans)