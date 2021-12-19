data = open("Day24.txt", "r").read().split("\n")
distances = [[0 for i in range(8)] for j in range(8)]

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

for i in range(8):
	pos = None
	for r in range(len(data)):
		for c in range(len(data[0])):
			if data[r][c] == str(i):
				pos = (r, c)
				break
		if pos is not None:
			break
	q = [(0, pos)]
	visited = {pos}
	found = set()
	while len(q) > 0:
		n, cur = q.pop(0)
		if data[cur[0]][cur[1]].isnumeric():
			v = int(data[cur[0]][cur[1]])
			distances[i][v] = n
			distances[v][i] = n
			found.add(v)
		if set(range(8)) == found:
			break
		for d in dirs:
			new_pos = (cur[0] + d[0], cur[1] + d[1])
			if 0 <= new_pos[0] < len(data) and 0 <= new_pos[1] < len(data[0]) and data[new_pos[0]][new_pos[1]] != "#" and new_pos not in visited:
				q.append((n + 1, new_pos))
				visited.add(new_pos)

q = [(0, (0,))]
while len(q) > 0:
	q = sorted(q)
	n, cur = q.pop(0)
	if len(cur) == 9:
		print(n)
		break
	elif set(cur) == set(range(8)):
		q.append((n + distances[cur[-1]][0], cur + (0,)))
	else:
		for i in range(8):
			if i not in cur:
				last = cur[-1]
				q.append((n + distances[last][i], cur + (i,)))