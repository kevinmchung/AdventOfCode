# Part 1: 1087
# Part 2: 1070

from collections import defaultdict
from copy import deepcopy

# dirs = ["e", "se", "sw", "w", "nw", "ne"]
# opps = {"e":"w", "w":"e", "se":"nw", "nw":"se", "sw":"ne", "ne":"sw"}
#
# class Tile:
# 	def __init__(self, neighbors):
# 		self.color = 0
# 		self.neighbors = neighbors
#
# 	def set_neighbor(self, d, tile):
# 		opp_d = opps[d]
# 		self.neighbors[dirs.index(d)] = tile
# 		tile.neighbors[dirs.index(opp_d)] = self
#
# 	def get_neighbor(self, d):
# 		return self.neighbors[dirs.index(d)]
#
# 	def change_color(self):
# 		self.color = (self.color + 1) % 2

dirs = {"e":(2, 0),
		"w":(-2, 0),
		"ne":(1, 1),
		"se":(1, -1),
		"nw":(-1, 1),
		"sw":(-1, -1)}

data = open("Day24.txt", "r").read().split("\n")

tiles = defaultdict(lambda: 0)

for line in data:
	cur = [0, 0]
	i = 0
	while i < len(line):
		if line[i] == "e" or line[i] == "w":
			d = line[i]
			i += 1
		else:
			d = line[i:i+2]
			i += 2
		delta = dirs[d]
		cur[0] += delta[0]
		cur[1] += delta[1]
	tiles[tuple(cur)] = (tiles[tuple(cur)] + 1) % 2

print(sum(tiles.values()))

for i in range(100):
	print(i, sum(tiles.values()))
	# expand coords

	new_tiles = deepcopy(tiles)

	for c in list(tiles.keys()):
		for delta in dirs.values():
			new_pos = (c[0] + delta[0], c[1] + delta[1])
			if new_pos not in tiles:
				tiles[new_pos] = 0
	for c in tiles.keys():
		total = 0
		for delta in dirs.values():
			new_pos = (c[0] + delta[0], c[1] + delta[1])
			if new_pos in tiles:
				total += tiles[(c[0] + delta[0], c[1] + delta[1])]
		if tiles[c] == 0 and total == 2:
			new_tiles[c] = 1
		elif tiles[c] == 1 and (total == 0 or total > 2):
			new_tiles[c] = 0
	tiles = new_tiles

print(sum(tiles.values()))
