target = [2981, 3075]
cur = [1, 1]
cur_code = 20151125

while cur != target:
	# print(cur)
	cur_code = (cur_code * 252533) % 33554393
	if cur[0] == 1:
		cur = [cur[1] + 1, 1]
	else:
		cur[0] -= 1
		cur[1] += 1

print(cur_code)