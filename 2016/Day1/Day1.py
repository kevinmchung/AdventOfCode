data = open("Day1.txt", "r").read().split(", ")

visited = {(0, 0)}
cur = [0, 0]
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
d = 0

def add_location(loc):
	if loc in visited:
		print(sum(loc))
		exit()
	else:
		visited.add(loc)

for ins in data:
	if ins[0] == "R":
		d = (d + 1) % 4
	elif ins[0] == "L":
		d = (d - 1) % 4
	n = int(ins[1:])
	for i in range(n):
		cur[0] += dirs[d][0]
		cur[1] += dirs[d][1]
		add_location(tuple(cur))

print(sum(cur))