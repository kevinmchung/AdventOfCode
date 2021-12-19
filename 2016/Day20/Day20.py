data = open("Day20.txt", "r").read().split("\n")

ranges = sorted(list(map(lambda l: tuple(map(int, l.split("-"))), data)), key=lambda l: l[0])
combined = [[0, 0]]
for r in ranges:
	if r[0] <= combined[-1][1] + 1:
		if r[1] > combined[-1][1]:
			combined[-1][1] = r[1]
	else:
		combined.append(list(r))
print(combined)
total = 0
for i in range(len(combined) - 1):
	total += combined[i + 1][0] - combined[i][1] - 1
print(total)