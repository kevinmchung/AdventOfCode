data = open("Day9.txt", "r").readlines()

def add_to_graph(graph, loc1, loc2, mag):
	if loc1 not in graph:
		graph[loc1] = {}
	graph[loc1][loc2] = mag

graph = {}

for line in data:
	line = line.strip().split(" = ")
	locs = line[0].split(" to ")
	dist = int(line[1])
	add_to_graph(graph, locs[0], locs[1], dist)
	add_to_graph(graph, locs[1], locs[0], dist)

# PART 1
# q = [[0, loc] for loc in graph]
#
# while len(q) > 0:
# 	q = sorted(q)
# 	cur = q.pop(-1)
# 	unvisited = False
# 	for loc in graph:
# 		if loc not in cur:
# 			new_path = cur + [loc]
# 			new_path[0] += graph[cur[-1]][loc]
# 			q.append(new_path)
# 			unvisited = True
# 	if not unvisited:
# 		print(cur)
# 		break

# PART 2
import itertools

locs = graph.keys()
perms = itertools.permutations(locs)

max_dist = 0
for perm in perms:
	cur_dist = 0
	for i in range(len(perm) - 1):
		cur_dist += graph[perm[i]][perm[i + 1]]
	if cur_dist > max_dist:
		max_dist = cur_dist
print(max_dist)