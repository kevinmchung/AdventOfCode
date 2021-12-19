data = open("Day3.txt", "r").read().split("\n")

total = 0

# for line in data:
# 	line = sorted(list(map(int, (x for x in line.split(" ") if x))))
# 	if line[0] + line[1] > line[2]:
# 		total += 1

cur = [[], [], []]
for line in data:
	line = list(map(int, (x for x in line.split(" ") if x)))
	for i in range(3):
		cur[i].append(line[i])
		if len(cur[i]) == 3:
			triangle = sorted(cur[i])
			if triangle[0] + triangle[1] > triangle[2]:
				total += 1
			cur[i] = []

print(total)
