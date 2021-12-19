inp = open("Day3.txt", "r").readline()

# PART 1
# visited = set()
# pos = [0, 0]
#
# for c in inp:
# 	visited.add(tuple(pos))
# 	if c == "<":
# 		pos[0] -= 1
# 	elif c == "^":
# 		pos[1] += 1
# 	elif c == ">":
# 		pos[0] += 1
# 	elif c == "v":
# 		pos[1] -= 1
#
# print(len(visited))

visited = set()
toggle = 0
pos = [[0, 0], [0, 0]]

for c in inp:
	visited.add(tuple(pos[toggle]))
	if c == "<":
		pos[toggle][0] -= 1
	elif c == "^":
		pos[toggle][1] += 1
	elif c == ">":
		pos[toggle][0] += 1
	elif c == "v":
		pos[toggle][1] -= 1
	toggle = (toggle + 1) % 2

print(len(visited))