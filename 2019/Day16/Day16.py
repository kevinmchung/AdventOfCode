def phase(num, iteration):
	pattern = [0, 1, 0, -1]
	pattern_index = 0
	i = 0
	total = 0
	for digit in num:
		i += 1
		if i % (iteration + 1) == 0:
			pattern_index = (pattern_index + 1) % 4
			i = 0
		total += int(digit) * pattern[pattern_index]
	return total

num = open("Day16.txt", "r").read() * 10000
offset = int(num[:7])
num = list(map(int, num[offset:]))

# for phases in range(100):
# 	new_num = ""
# 	for i in range(len(num)):
# 		new_num += str(phase(num, i))[-1]
# 	num = new_num

for phases in range(100):
	for i in reversed(range(1, len(num))):
		num[i - 1] += num[i]
	for i in range(len(num)):
		num[i] = abs(num[i]) % 10

print("".join(map(str, num[:8])))