def look_and_say(num):
	new_num = ""
	cur_dig = 0
	cur_count = 0
	for i in range(len(num)):
		if num[i] != cur_dig:
			if cur_dig != 0:
				new_num += str(cur_count) + str(cur_dig)
			cur_dig = num[i]
			cur_count = 1
		else:
			cur_count += 1
	new_num += str(cur_count) + str(cur_dig)
	return new_num

inp = "1321131112"

for i in range(50):
	inp = look_and_say(inp)

print(len(inp))