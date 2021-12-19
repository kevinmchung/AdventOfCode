from collections import defaultdict

regex = open("Day20.txt", "r").read()[1:-1]
dirs = {"N":(0, 1), "E":(1, 0), "S":(0, -1), "W":(-1, 0)}
opp = {"N":"S", "S":"N", "E":"W", "W":"E"}
doors = defaultdict(lambda: {d:False for d in dirs})

def get_grid(regex, positions):
	i = 0
	while i < len(regex):
		if regex[i] == "(":
			stack = ["("]
			j = i + 1
			splits = [i]
			while len(stack) > 0:
				if regex[j] == "(":
					stack.append("(")
				elif regex[j] == ")":
					stack.pop(-1)
				elif regex[j] == "|" and len(stack) == 1:
					splits.append(j)
				j += 1
			splits.append(j - 1)

			new_positions = []
			for k in range(len(splits) - 1):
				temp_positions = [[n for n in p] for p in positions]
				new_positions += get_grid(regex[splits[k] + 1:splits[k + 1]], temp_positions)
			positions = list(map(list, set(map(tuple, new_positions))))
			i = j

		else:
			d = regex[i]
			for j in range(len(positions)):
				doors[tuple(positions[j])][d] = True
				doors[(positions[j][0] + dirs[d][0], positions[j][1] + dirs[d][1])][opp[d]] = True
				positions[j][0] += dirs[d][0]
				positions[j][1] += dirs[d][1]
			i += 1
	return positions

start = (0, 0)
get_grid(regex, [list(start)])

total = 0
q = [(0, start)]
visited = {start}
highest = 0
while len(q) > 0:
	n, cur = q.pop(0)
	if n > highest:
		highest = n
	if n >= 1000:
		total += 1
	for d in dirs:
		new_pos = (cur[0] + dirs[d][0], cur[1] + dirs[d][1])
		if doors[cur][d] and new_pos not in visited:
			q.append((n + 1, new_pos))
			visited.add(new_pos)

print(highest)
print(total)
