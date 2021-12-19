data = open("Day2.txt", "r").read().split("\n")

# nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
grid = ['xx1xx',
		'x234x',
		'56789',
		'xABCx',
		'xxDxx']

seq = ""
cur = [1, 1]
dirs = {"L": (0, -1),
		"U": (-1, 0),
		"D": (1, 0),
		"R": (0, 1)}

for line in data:
	for c in line:
		d = dirs[c]
		cur[0] += d[0]
		cur[1] += d[1]
		if not (0 <= cur[0] < 5) or not (0 <= cur[1] < 5) or grid[cur[0]][cur[1]] == 'x':
			cur[0] -= d[0]
			cur[1] -= d[1]
	seq += str(grid[cur[0]][cur[1]])

print(seq)