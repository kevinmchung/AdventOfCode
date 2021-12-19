# RANKS
# Part 1: 62
# Part 2: 151

data = open("Day5.txt", "r").readlines()
# data = list(map(int, data))

seats = list(range(1024))

total = 0

for line in data:
	line = line.strip()
	row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
	col = int(line[7:].replace("L", "0").replace("R", "1"), 2)
	if row * 8 + col == 155:
		print(line)
	# if row * 8 + col > total:
	# 	total = row * 8 + col
	seats.remove(row * 8 + col)

print(seats)