from collections import defaultdict

def find(index, l):

	while l[index][1] != index:
		index, l[index][1] = l[index][1], l[l[index][1]][1]

	return index


def union(index1, index2, l):

	root1 = find(index1, l)
	root2 = find(index2, l)

	if root1 == root2:
		return

	if l[root1][2] < l[root2][2]:
		root1, root2 = root2, root1

	l[root2][1] = root1
	if l[root1][2] == l[root2][2]:
		l[root1][2] += 1

def manhattan(s1, s2):
	return abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) + abs(s1[2] - s2[2]) + abs(s1[3] - s2[3])

data = open("Day25.txt", "r").read().split("\n")

stars = []
for i in range(len(data)):
	stars.append([tuple(map(int, data[i].split(","))), i, 0])

for i in range(len(stars)):
	for j in range(len(stars)):
		if manhattan(stars[i][0], stars[j][0]) <= 3:
			union(i, j, stars)

groups = defaultdict(list)

for star in stars:
	groups[find(star[1], stars)].append(star[0])

print(len(groups.keys()))

# print(groups)