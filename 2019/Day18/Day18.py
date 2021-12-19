dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

def reachable_keys(pos, grid, keys):
	reachable = []
	q = [(pos, 0)]
	visited = {pos}
	while len(q) > 0:
		(r, c), n = q.pop(0)
		if grid[r][c].isalpha() and grid[r][c].islower() and grid[r][c] not in keys:
			reachable.append((grid[r][c], (r, c), n))
			continue
		for d in dirs:
			new_r, new_c = r + d[0], c + d[1]
			if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and (new_r, new_c) not in visited:
				if not ((grid[r][c].isalpha() and grid[r][c].isupper() and grid[r][c].lower() not in keys) or grid[r][c] == "#"):
					q.append(((new_r, new_c), n + 1))
					visited.add((new_r, new_c))
	return reachable

def pt1(start, all_keys, grid):
	q = [(0, start, ())]
	visited = {(start, ()): 0}
	while len(q) > 0:
		q = sorted(q)
		n, (r, c), keys = q.pop(0)
		if sorted(keys) == all_keys:
			return n
		reachable = reachable_keys((r, c), grid, keys)
		# print(reachable)
		for l, (new_r, new_c), dist in reachable:
			new_keys = keys + (l,)
			sorted_keys = tuple(sorted(new_keys))
			if ((new_r, new_c), sorted_keys) not in visited or visited[((new_r, new_c), sorted_keys)] > n + dist:
				q.append((n + dist, (new_r, new_c), new_keys))
				visited[((new_r, new_c), sorted_keys)] = n + dist

def pt2(starts, all_keys, grid):
	q = [(0, starts, ())]
	visited = {(starts, ()): 0}
	while len(q) > 0:
		q = sorted(q)
		n, positions, keys = q.pop(0)
		print(n, positions, keys)
		if sorted(keys) == all_keys:
			return n
		reachable = []
		for pos in positions:
			reachable.append(reachable_keys(pos, grid, keys))
		# print(reachable)
		for i in range(4):
			for l, (new_r, new_c), dist in reachable[i]:
				new_keys = keys + (l,)
				sorted_keys = tuple(sorted(new_keys))
				new_positions = list(positions)
				new_positions[i] = (new_r, new_c)
				new_positions = tuple(new_positions)
				if (new_positions, sorted_keys) not in visited or visited[(new_positions, sorted_keys)] > n + dist:
					q.append((n + dist, new_positions, new_keys))
					visited[(new_positions, sorted_keys)] = n + dist

grid = open("Day18.txt", "r").read().split("\n")

starts = []
all_keys = []
for r in range(len(grid)):
	for c in range(len(grid[0])):
		if grid[r][c] == "@":
			starts.append((r, c))
		elif grid[r][c].isalpha() and grid[r][c].islower():
			all_keys.append(grid[r][c])

all_keys = sorted(tuple(all_keys))
starts = tuple(starts)

# print(pt1(start, all_keys, grid))
print(pt2(starts, all_keys, grid))
