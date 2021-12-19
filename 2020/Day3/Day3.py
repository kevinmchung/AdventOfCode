# RANKS
# Part 1: 3
# Part 2: 18

data = open("Day3.txt", "r").readlines()
# data = list(map(int, data))

total = 0
idx = 0
for i in range(0, len(data), 2):
	line = data[i].strip()
	if line[idx] == "#":
		total += 1
	idx = (idx + 1) % len(line)

print(total)