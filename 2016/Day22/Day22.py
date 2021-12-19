import re

data = open("Day22.txt", "r").read().split("\n")[2:]
nodes = {}

for line in data:
	x, y, space, used = map(int, re.match(r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(?:\d+)T\s+(?:\d+)%", line).groups())
	nodes[(x, y)] = (space, used)

total = 0
for p1 in nodes:
	for p2 in nodes:
		if p1 != p2 and 0 < nodes[p1][1] <= (nodes[p2][0] - nodes[p2][1]):
			total += 1

max_x = max(k[0] for k in nodes)
max_y = max(k[1] for k in nodes)
dims = (max_x + 1, max_y + 1)

print(total)

space = []
used = []
for y in range(dims[1]):
	space_row = []
	used_row = []
	for x in range(dims[0]):
		space_row.append(nodes[(x, y)][0])
		used_row.append(nodes[(x, y)][1])
	space.append(space_row)
	used.append(used_row)

space = tuple(map(tuple, space))
used = tuple(map(tuple, used))

zero = None
for x in range(dims[0]):
	for y in range(dims[1]):
		if used[y][x] == 0:
			zero = (x, y)
			break

target = (0, 0)
target_data = (max_x, 0)

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

for y in range(dims[1]):
	for x in range(dims[0]):
		print(" {}/{} ".format(used[y][x], space[y][x]), end="")
	print()


