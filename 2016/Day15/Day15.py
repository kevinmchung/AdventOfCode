import re
data = open("Day15.txt", "r").read().split("\n")

discs = []
for line in data:
	match = re.match(r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).", line)
	discs.append(tuple(map(int, match.groups())))

i = 0
while not all(0 == (d[2] + i + d[0]) % d[1] for d in discs):
	i += 1
print(i)

