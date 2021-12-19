import math

wires = open("Day3.txt", "r").readlines()

# grid = [[[0, 0] for i in range(10000)] for j in range(10000)]
# port = [5000, 5000]

grid = [[[0, 0]]]
port = [0, 0]

for j in range(2):
	cur = port[:]
	steps = 0
	for step in wires[j].strip().split(","):
		print(step)
		n = int(step[1:])
		steps += n
		if step[0] == "U":
			if cur[0] < n:
				pad = n - cur[0]
				for i in range(pad):
					grid.insert(0, [[0, 0] for j in range(len(grid[0]))])
				cur[0] += pad
				port[0] += pad
			cur[0] -= n
			for i in range(n):
				grid[cur[0] + i][cur[1]][j] = steps - i
		elif step[0] == "D":
			if len(grid) - cur[0] - 1 < n:
				pad = n - len(grid) + cur[0] + 1
				for i in range(pad):
					grid.append([[0, 0] for j in range(len(grid[0]))])
			cur[0] += n
			for i in range(n):
				grid[cur[0] - i][cur[1]][j] = steps - i
		elif step[0] == "L":
			if cur[1] < n:
				pad = n - cur[1]
				for i in range(pad):
					for r in range(len(grid)):
						grid[r].insert(0, [0, 0])
				cur[1] += pad
				port[1] += pad
			cur[1] -= n
			for i in range(n):
				grid[cur[0]][cur[1] + i][j] = steps - i
		elif step[0] == "R":
			if len(grid[0]) - cur[1] - 1 < n:
				pad = n - len(grid[0]) + cur[1] + 1
				for i in range(pad):
					for r in range(len(grid)):
						grid[r].append([0, 0])
			cur[1] += n
			for i in range(n):
				grid[cur[0]][cur[1] - i][j] = steps - i

min_dist = math.inf
for r in range(len(grid)):
	for c in range(len(grid[0])):
		if grid[r][c][0] > 0 and grid[r][c][1] > 0:
			dist = sum(grid[r][c])
			if dist < min_dist:
				min_dist = dist

print(min_dist)
print(port)
print("\n".join(" ".join(map(str, row)) for row in grid))
