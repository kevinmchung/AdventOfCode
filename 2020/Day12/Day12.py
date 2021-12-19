# Part 1: 57
# Part 2: 213

data = open("Day12.txt", "r").read().split("\n")
# data = list(map(int, data))

pos = [0, 0]

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
d = 1

for line in data:
	com = line[0]
	if com == "N":
		pos[1] += int(line[1:])
	elif com == "S":
		pos[1] -= int(line[1:])
	elif com == "E":
		pos[0] += int(line[1:])
	elif com == "W":
		pos[0] -= int(line[1:])
	elif com == "L":
		deg = int(line[1:])
		d = (d - deg // 90) % 4
	elif com == "R":
		deg = int(line[1:])
		d = (d + deg // 90) % 4
	elif com == "F":
		pos[0] += dirs[d][0] * int(line[1:])
		pos[1] += dirs[d][1] * int(line[1:])

print(abs(pos[0]) + abs(pos[1]))

spos = [0, 0]
wpos = [10, 1]
for line in data:
	com = line[0]
	n = int(line[1:])
	if com == "N":
		wpos[1] += n
	elif com == "S":
		wpos[1] -= n
	elif com == "E":
		wpos[0] += n
	elif com == "W":
		wpos[0] -= n
	elif com == "L" or com == "R":
		if com == "L":
			deg = - n // 90 % 4
		else:
			deg = n // 90
		if deg == 1:
			wpos = [wpos[1], -wpos[0]]
		elif deg == 2:
			wpos = [-wpos[0], -wpos[1]]
		else:
			wpos = [-wpos[1], wpos[0]]
	elif com == "F":
		spos[0] += wpos[0] * n
		spos[1] += wpos[1] * n


print(abs(spos[0]) + abs(spos[1]))