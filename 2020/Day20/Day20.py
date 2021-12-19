# Part 1: 658
# Part 2: 610

import numpy as np
from copy import deepcopy

class Grid:
	def __init__(self, size):
		self.size = size
		self.id_grid = [[0 for i in range(size)] for j in range(size)]
		self.grid = [[None for i in range(size)] for j in range(size)]

	def check_if_valid(self, tile):
		cur = ()
		for r in range(self.size):
			for c in range(self.size):
				if self.grid[r][c] is None:
					cur = (r, c)
					break
			if cur:
				break
		if cur[0] > 0:
			above = self.grid[cur[0] - 1][cur[1]]
			if not np.array_equal(above[-1, :], tile[0, :]):
				return False
		if cur[1] > 0:
			left = self.grid[cur[0]][cur[1] - 1]
			if not np.array_equal(left[:, -1], tile[:, 0]):
				return False
		return True

	def add_to_grid(self, n, tile):
		for r in range(self.size):
			for c in range(self.size):
				if self.grid[r][c] is None:
					self.id_grid[r][c] = n
					self.grid[r][c] = tile
					return

	def check_full(self):
		for r in range(self.size):
			for c in range(self.size):
				if self.grid[r][c] is None:
					return False

		return True

	def get_ids(self):
		out = set()
		for r in range(self.size):
			for c in range(self.size):
				if self.id_grid[r][c] != 0:
					out.add(self.id_grid[r][c])
		return out


def get_perms(arr):
	return [arr,
			np.rot90(arr),
			np.rot90(arr, 2),
			np.rot90(arr, 3),
			np.fliplr(arr),
			np.rot90(np.fliplr(arr)),
			np.rot90(np.fliplr(arr), 2),
			np.rot90(np.fliplr(arr), 3),]

grid_size = 12
data = open("Day20.txt", "r").read().split("\n\n")
sea_monster = np.zeros((3, 20))
tiles = {}
for t in data:
	t = t.split("\n")
	if "Tile" in t[0]:
		n = int(t[0][5:9])
		arr = np.zeros((10, 10))
		for r in range(10):
			for c in range(10):
				if t[r + 1][c] == "#":
					arr[r][c] = 1
		tiles[n] = arr
	else:
		for r in range(3):
			for c in range(20):
				if t[r][c] == "#":
					sea_monster[r][c] = 1

corners = []

s = 0
ans = 1
for n in tiles:
	tile = tiles[n]
	s += np.sum(tile)
	matches = 0
	edges = [tile[0, :], tile[-1, :], tile[:, 0], tile[:, -1]]
	# print(tile, edges)
	for edge in edges:
		for k in tiles:
			if n != k:
				tile2 = tiles[k]
				edges2 = [tile2[0, :], tile2[-1, :], tile2[:, 0], tile2[:, -1],
						  np.flip(tile2[0, :]), np.flip(tile2[-1, :]),
						  np.flip(tile2[:, 0]), np.flip(tile2[:, -1])]
				if any(np.array_equal(edge, e) for e in edges2):
					matches += 1
					break
	if matches == 2:
		ans *= n
		corners.append(n)

print(ans)

keys = list(tiles.keys())
q = []

for key in corners:
	perms = get_perms(tiles[key])
	for perm in perms:
		grid = Grid(grid_size)
		grid.add_to_grid(key, perm)
		q.append(grid)

ans = None
while len(q) > 0:
	cur = q.pop(0)
	if cur.check_full():
		ans = cur
		break
	cur_ids = cur.get_ids()
	for key in keys:
		if key not in cur_ids:
			perms = get_perms(tiles[key])
			for perm in perms:
				if cur.check_if_valid(perm):
					new_grid = Grid(grid_size)
					new_grid.id_grid = deepcopy(cur.id_grid)
					new_grid.grid = deepcopy(cur.grid)
					new_grid.add_to_grid(key, perm)
					q.append(new_grid)

image = np.zeros((96, 96))
for r in range(12):
	for c in range(12):
		image[r * 8:(r + 1) * 8, c * 8:(c + 1) * 8] = ans.grid[r][c][1:-1, 1:-1]

# out_file = open("Day20_grid", "w")
# for r in range(120):
# 	out_file.write("".join(map(lambda x: str(int(x)), image[r, :])) + "\n")
# out_file.close()


monster_idx = sea_monster == 1
for perm in get_perms(image):
	new_perm = np.copy(perm)
	for r in range(96):
		for c in range(96):
			if r + 3 <= 96 and c + 20 <= 96:
				if np.all(perm[r:r+3, c:c+20][monster_idx] == 1):
					new_perm[r:r+3, c:c+20][monster_idx] = 0

	print(np.sum(new_perm))