import math

inp = 1364
target = (31, 39)
# inp = 10
# target = (7, 4)

def wall(x, y):
	n = x*x + 3*x + 2*x*y + y + y*y
	n += inp
	num_ones = bin(n).count("1")
	return num_ones % 2 == 1

def dist(p1, p2):
	return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))

visited = set()
q = [((1, 1),)]
while len(q) > 0:
	# q = sorted(q, key=lambda s: dist(s[-1], target))
	cur = q.pop(0)
	last_pos = cur[-1]
	visited.add(last_pos)
	# if last_pos == target:
	# 	print(cur)
	# 	print(len(cur) - 1)
	# 	break
	if len(cur) - 1 < 50:
		for d in dirs:
			new_pos = (last_pos[0] + d[0], last_pos[1] + d[1])
			if 0 <= new_pos[0] and 0 <= new_pos[1] and new_pos not in cur and not wall(new_pos[0], new_pos[1]):
				q.append(cur + (new_pos,))
print(len(visited))
