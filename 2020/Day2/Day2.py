# RANKS
# Part 1: 65
# Part 2: 66

data = open("Day2.txt", "r").readlines()
# data = list(map(int, data))

total = 0
for p in data:
	p = p.split(" ")
	# if int(p[0].split("-")[0]) <= p[2].count(p[1][0]) <= int(p[0].split("-")[1]):
	# 	total += 1
	if (p[2][int(p[0].split("-")[0]) - 1] == p[1][0]) ^ (p[2][int(p[0].split("-")[1]) - 1] == p[1][0]):
		total += 1

print(total)