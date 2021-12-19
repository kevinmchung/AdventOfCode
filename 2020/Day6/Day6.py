# RANKS
# Part 1: 135
# Part 2: 88

data = open("Day6.txt", "r").readlines()
# data = list(map(int, data))

data = "".join(data).split("\n\n")

total = 0

for i in range(len(data)):
	line = data[i].strip()
	line = line.split("\n")
	letters = set(line[0])
	for answers in line[1:]:
		letters = letters.intersection(set(answers))
	total += len(letters)

print(total)