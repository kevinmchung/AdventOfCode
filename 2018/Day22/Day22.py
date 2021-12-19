import numpy as np
import networkx as nx

depth = 8787
target = (10, 725)
erosion = np.zeros((target[1] + 100, target[0] + 100), dtype=int) - 1

def get_erosion(x, y):
	if erosion[y][x] != -1:
		return erosion[y][x]
	if (x == 0 and y == 0) or (x == target[0] and y == target[1]):
		geo_idx = 0
	elif y == 0:
		geo_idx = x * 16807
	elif x == 0:
		geo_idx = y * 48271
	else:
		geo_idx = get_erosion(x - 1, y) * get_erosion(x, y - 1)
	erosion[y][x] = (geo_idx + depth) % 20183
	return erosion[y][x]

for x in range(target[0] + 1):
	for y in range(target[1] + 1):
		get_erosion(x, y)

grid = erosion % 3
print(np.sum(grid[:target[1] + 1, :target[0] + 1]))

tools = (0, 1, 2) # neither, torch, climbing gear

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

# for y in range(16):
# 	for x in range(16):
# 		print(".=|"[get_erosion(x, y) % 3], end="")
# 	print()

graph = nx.Graph()

for y in range(erosion.shape[0]):
	for x in range(erosion.shape[1]):
		risk = get_erosion(x, y) % 3
		valid_tools = [tool for tool in tools if tool != risk]
		graph.add_edge((x, y, valid_tools[0]), (x, y, valid_tools[1]), weight=7)
		for dx, dy in dirs:
			new_x, new_y = x + dx, y + dy
			if 0 <= new_x < erosion.shape[1] and 0 <= new_y < erosion.shape[0]:
				new_risk = get_erosion(new_x, new_y) % 3
				new_valid_tools = [tool for tool in tools if tool != new_risk]
				for tool in set(valid_tools).intersection(new_valid_tools):
					graph.add_edge((x, y, tool), (new_x, new_y, tool), weight=1)

# print(nx.dijkstra_path(graph, (0, 0, 1), (target[0], target[1], 1)))
print(nx.dijkstra_path_length(graph, (0, 0, 1), (target[0], target[1], 1)))


# print(path[::-1])
