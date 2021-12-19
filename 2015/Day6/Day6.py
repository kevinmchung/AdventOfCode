import numpy as np

data = open("Day6.txt", "r").readlines()

# PART 1

# grid = np.zeros((1000, 1000), dtype=bool)

# for line in data:
# 	instructions = line.split(" ")
# 	if instructions[0] == "toggle":
# 		p1 = list(map(int, instructions[1].split(",")))
# 		p2 = list(map(int, instructions[3].split(",")))
# 		grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] = np.logical_not(grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1])
# 	else:
# 		p1 = list(map(int, instructions[2].split(",")))
# 		p2 = list(map(int, instructions[4].split(",")))
# 		if instructions[1] == "on":
# 			grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] = True
# 		else:
# 			grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] = False

grid = np.zeros((1000, 1000))

for line in data:
	instructions = line.split(" ")
	if instructions[0] == "toggle":
		p1 = list(map(int, instructions[1].split(",")))
		p2 = list(map(int, instructions[3].split(",")))
		grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] += 2
	else:
		p1 = list(map(int, instructions[2].split(",")))
		p2 = list(map(int, instructions[4].split(",")))
		if instructions[1] == "on":
			grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] += 1
		else:
			grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] -= 1
			grid[grid < 0] = 0

print(np.sum(grid))

