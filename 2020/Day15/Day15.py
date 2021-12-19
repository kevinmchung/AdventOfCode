# Part 1: 108
# Part 2: 2470

from collections import defaultdict

last_index = defaultdict(lambda: 0)

inp = [1, 0, 18, 10, 19, 6]

i = 1
cur = inp[-1]
while i < 30000000:
	if i <= len(inp) - 1:
		last_index[inp[i - 1]] = i
	else:
		old = cur
		cur = last_index[cur]
		if cur != 0:
			cur = i - cur
		last_index[old] = i
	i += 1

print(cur)