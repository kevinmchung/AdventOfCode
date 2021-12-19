import math

def get_dr_dc(r1, c1, r2, c2):
	dr = r2 - r1
	dc = c2 - c1
	if dr == 0:
		dc /= abs(dc)
	elif dc == 0:
		dr /= abs(dr)
	else:
		dc /= abs(dr)
		dr /= abs(dr)
	return dr, dc

def num_visible_asteroids(row, col, grid):
	num_visible = 0
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if (r != row or c != col) and grid[r][c] == "#":
				dr, dc = get_dr_dc(row, col, r, c)
				blocked = False
				cur_r = row + dr
				cur_c = col + dc
				while round(cur_r, 8) != r or round(cur_c, 8) != c:
					if round(cur_r, 8) % 1 == 0 and round(cur_c, 8) % 1 == 0 and grid[round(cur_r)][round(cur_c)] == "#":
						blocked = True
						break
					cur_r += dr
					cur_c += dc
				if not blocked:
					num_visible += 1
	return num_visible


grid = [list(line.strip()) for line in open("Day10.txt", "r").readlines()]

max_coords = None
max_visible = 0
for r in range(len(grid)):
	for c in range(len(grid[0])):
		if grid[r][c] == "#":
			visible = num_visible_asteroids(r, c, grid)
			if visible > max_visible:
				max_visible = visible
				max_coords = (r, c)

print(max_coords, max_visible)

station = max_coords

angles = []
asteroid_angles = {}
for r in range(len(grid)):
	for c in range(len(grid[0])):
		if (r != station[0] or c != station[1]) and grid[r][c] == "#":
			dr, dc = get_dr_dc(station[0], station[1], r, c)
			if (dr, dc) in asteroid_angles:
				asteroid_angles[(dr, dc)].append((r, c))
			else:
				angles.append((dr, dc))
				asteroid_angles[(dr, dc)] = [(r, c)]

angles = sorted(angles, key=lambda angle : math.atan2(angle[1], -angle[0]) % (2 * math.pi))
for angle in asteroid_angles:
	asteroid_angles[angle] = sorted(asteroid_angles[angle], key=lambda point : (point[0] - station[0]) ** 2 + (point[1] - station[1]) ** 2)

asteroid = 1
revolution = 0
i = 0
while asteroid < 200:
	if len(asteroid_angles[angles[i]]) > revolution:
		asteroid += 1
	if i == len(angles) - 1:
		i = 0
		revolution += 1
	else:
		i += 1

print(asteroid_angles[angles[i]][revolution])
