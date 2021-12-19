from collections import defaultdict

data = open("Day6.txt", "r").read().split("\n")
points = tuple(map(lambda l:tuple(map(int, l.split(", "))), data))

max_x = max(p[0] for p in points)
max_y = max(p[1] for p in points)

grid = defaultdict(lambda: None)
for x in range(max_x):
	for y in range(max_y):
		min_dist = min(abs(x - p[0]) + abs(y - p[1]) for p in points)
		for p in points:
			if abs(x - p[0]) + abs(y - p[1]) == min_dist:
				if grid[(x, y)] is not None:
					grid[(x, y)] = None
					break
				grid[(x, y)] = p

invalid = set.union(set(grid[(0, y)] for y in range(max_y)),
					set(grid[(max_x - 1, y)] for y in range(max_y)),
					set(grid[(x, 0)] for x in range(max_x)),
					set(grid[(x, max_y - 1)] for x in range(max_x)))

most = 0
for p in points:
	if p not in invalid:
		cur_count = 0
		for x in range(max_x):
			for y in range(max_y):
				if grid[(x, y)] == p:
					cur_count += 1
		if cur_count > most:
			most = cur_count

print(most)

total = 0
for x in range(max_x):
	for y in range(max_y):
		if sum(abs(x - p[0]) + abs(y - p[1]) for p in points) < 10000:
			total += 1
print(total)
