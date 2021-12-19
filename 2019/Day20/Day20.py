import re

data = open("Day20.txt", "r").read().split("\n")

outer_tl = (2, 2)
outer = (len(data) - 4, data[2].rfind("#") - 1)
inner_tl = (-1, -1)
inner = [0, 0]
for i in range(2, len(data) - 2):
	row = data[i]
	if " " in row[outer_tl[1]:outer_tl[1] + outer[1]]:
		if inner_tl == (-1, -1):
			span = re.match("[ A-Z]*[#.]+([ A-Z]+)[#.]+[ A-Z]*", row).span(1)
			inner_tl = (i, span[0])
			inner[1] = span[1] - span[0]
		inner[0] += 1
inner = tuple(inner)

portal_entrances = {}

# check vertical
rows_to_check = {0: ("below", -1),
				 inner_tl[0]: ("above", 1),
				 inner_tl[0] + inner[0] - 2: ("below", 1),
				 outer_tl[0] + outer[0]: ("above", -1)}
for c in range(outer_tl[1], outer_tl[1] + outer[1]):
	for r in rows_to_check:
		if c < len(data[r]) and data[r][c].isalpha() and data[r + 1][c].isalpha():
			d, depth = rows_to_check[r]
			if d == "below":
				portal_entrances[(r + 2, c)] = (data[r][c] + data[r + 1][c], depth)
			else:
				portal_entrances[(r - 1, c)] = (data[r][c] + data[r + 1][c], depth)

# check horizontal
cols_to_check = {0: ("right", -1),
				 inner_tl[1]: ("left", 1),
				 inner_tl[1] + inner[1] - 2: ("right", 1),
				 outer_tl[1] + outer[1]: ("left", -1)}
for r in range(outer_tl[0], outer_tl[0] + outer[0]):
	for c in cols_to_check:
		if c < len(data[r]) and data[r][c].isalpha() and data[r][c + 1].isalpha():
			d, depth = cols_to_check[c]
			if d == "right":
				portal_entrances[(r, c + 2)] = (data[r][c] + data[r][c + 1], depth)
			else:
				portal_entrances[(r, c - 1)] = (data[r][c] + data[r][c + 1], depth)

start = None
end = None
portals = {}
keys = list(portal_entrances.keys())
for i in range(len(keys)):
	if portal_entrances[keys[i]][0] == "AA":
		start = keys[i]
	elif portal_entrances[keys[i]][0] == "ZZ":
		end = keys[i]
	else:
		for j in range(i + 1, len(keys)):
			if portal_entrances[keys[i]][0] == portal_entrances[keys[j]][0]:
				portals[keys[i]] = (keys[j], portal_entrances[keys[i]][1])
				portals[keys[j]] = (keys[i], portal_entrances[keys[j]][1])

def in_bounds(r, c):
	if not (outer_tl[0] <= r < outer_tl[0] + outer[0] and outer_tl[1] <= c < outer_tl[1] + outer[1]):
		return False
	if inner_tl[0] <= r < inner_tl[0] + inner[0] and inner_tl[1] <= c < inner_tl[1] + inner[1]:
		return False
	return True

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

q = [(0, start, 0)]
visited = {(start, 0)}
while len(q) > 0:
	n, (r, c), depth = q.pop(0)
	if (r, c) == end and depth == 0:
		print(n)
		break
	for d in dirs:
		new_r, new_c = r + d[0], c + d[1]
		if in_bounds(new_r, new_c) and data[new_r][new_c] == "." and ((new_r, new_c), depth) not in visited:
			q.append((n + 1, (new_r, new_c), depth))
			visited.add(((new_r, new_c), depth))
	if (r, c) in portals:
		(new_r, new_c), depth_change = portals[(r, c)]
		new_depth = depth + depth_change
		if ((new_r, new_c), new_depth) not in visited and new_depth >= 0:
			q.append((n + 1, (new_r, new_c), new_depth))
			visited.add(((new_r, new_c), new_depth))
