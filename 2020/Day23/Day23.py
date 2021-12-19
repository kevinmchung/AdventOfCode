# Part 1: 455
# Part 2: 56

cups = list(map(int, "598162734"))
n = max(cups) + 1
while len(cups) < 1000000:
	cups.append(n)
	n += 1

# idx = 0
# for i in range(10000000):
# 	cur = cups[idx]
# 	remove = []
# 	for j in range(3):
# 		if idx + 1 < len(cups):
# 			remove.append(cups.pop(idx + 1))
# 		else:
# 			remove.append(cups.pop(0))
#
# 	dest = cur - 1
#
# 	while dest not in cups:
# 		if dest == 0:
# 			dest = max(cups)
# 		else:
# 			dest -= 1
# 	dest_idx = cups.index(dest)
# 	for j in range(3):
# 		cups.insert(dest_idx + 1 + j, remove[j])
#
# 	if cups.index(cur) != idx:
# 		diff = cups.index(cur) - idx
# 		cups = cups[diff:] + cups[:diff]
#
# 	idx = (idx + 1) % len(cups)


# print(cups)

cups = {cups[i]:cups[(i + 1) % len(cups)] for i in range(len(cups))}

cur = 5
for i in range(10000000):
	removed = [cups[cur], cups[cups[cur]], cups[cups[cups[cur]]]]
	cups[cur] = cups[cups[cups[cups[cur]]]]
	dest = cur
	while True:
		dest -= 1
		if dest == 0:
			dest = max(cups.keys())
		if dest not in removed:
			break
	cof_dest = cups[dest]
	cups[dest] = removed[0]
	cups[removed[2]] = cof_dest
	cur = cups[cur]

print(cups[1] * cups[cups[1]])