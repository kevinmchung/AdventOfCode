tree = {}
reverse = {}

orbits = open("Day6.txt", "r").readlines()
for orbit in orbits:
	node1, node2 = orbit.strip().split(")")
	if node1 in tree:
		tree[node1].append(node2)
	else:
		tree[node1] = [node2]
	reverse[node2] = node1

# total = 0
# for node in reverse:
# 	cur = node
# 	cur_depth = 0
# 	while cur in reverse:
# 		cur = reverse[cur]
# 		cur_depth += 1
# 	total += cur_depth
# print(total)

cur1, cur2 = "YOU", "SAN"
visited1, visited2 = ["YOU"], ["SAN"]
while cur1 in reverse or cur2 in reverse:
	if cur1 in reverse:
		cur1 = reverse[cur1]
		visited1.append(cur1)
		if cur1 in visited2:
			break
	if cur2 in reverse:
		cur2 = reverse[cur2]
		visited2.append(cur2)
		if cur2 in visited1:
			break

if cur1 in visited2:
	ans = visited1.index(cur1) + visited2.index(cur1) - 2
else:
	ans = visited1.index(cur2) + visited2.index(cur2) - 2
print(ans)