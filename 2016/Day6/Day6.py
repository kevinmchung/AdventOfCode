from collections import defaultdict

data = open("Day6.txt", "r").read().split("\n")

counts = [defaultdict(int) for i in range(8)]
for line in data:
	for i in range(8):
		counts[i][line[i]] += 1

for i in range(8):
	print(min([k for k in counts[i].keys() if counts[i][k] != 0], key=lambda x: counts[i][x]), end="")