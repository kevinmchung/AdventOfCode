# RANKS
# Part 1: 389 (site crashed)
# Part 2: 63

data = list(map(int, open("Day1.txt", "r").readlines()))

for i in range(len(data)):
	for j in range(i + 1, len(data)):
		for k in range(j + 1, len(data)):
			if data[i] + data[j] + data[k] == 2020:
				print(data[i]*data[j]*data[k])