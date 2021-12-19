from collections import defaultdict

lines = [line.strip() for line in open("Day5.txt", "r")]
# lines = list(map(int, lines))

counts = defaultdict(int)
ls = []
for i in range(len(lines)):
	line = lines[i]
	line = line.split(" -> ")
	l1 = list(map(int, line[0].split(",")))
	l2 = list(map(int, line[1].split(",")))
	if l1[0] == l2[0]:
		for j in range(min(l1[1], l2[1]), max(l1[1], l2[1]) + 1):
			counts[(l1[0], j)] += 1
	elif l1[1] == l2[1]:
		for j in range(min(l1[0], l2[0]), max(l1[0], l2[0]) + 1):
			counts[(j, l1[1])] += 1
	else:
		mag = abs(l2[0] - l1[0])
		dx = (l2[0] - l1[0]) // mag
		dy = (l2[1] - l1[1]) // mag
		for j in range(mag + 1):
			counts[(l1[0] + dx * j, l1[1] + dy * j)] += 1

ans = 0
for key in counts:
	if counts[key] >= 2:
		ans += 1

print(ans)