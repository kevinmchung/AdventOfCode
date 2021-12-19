data = open("Day2.txt", "r").read().split("\n")

l2 = 0
l3 = 0
for line in data:
	for c in line:
		if line.count(c) == 2:
			l2 += 1
			break
	for c in line:
		if line.count(c) == 3:
			l3 += 1
			break

print(l2 * l3)

for i in range(len(data)):
	for j in range(i + 1, len(data)):
		common = ""
		for k in range(len(data[i])):
			if data[i][k] == data[j][k]:
				common += data[i][k]
		if len(common) == len(data[i]) - 1:
			print(common)
			exit()