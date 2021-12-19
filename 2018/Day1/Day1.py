data = open("Day1.txt", "r").read().split("\n")

print(sum(map(int, data)))

visited = set()
cur = 0
i = 0
while cur not in visited:
	visited.add(cur)
	cur += int(data[i])
	i = (i + 1) % len(data)

print(cur)