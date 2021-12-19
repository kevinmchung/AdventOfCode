# Part 1: 32
# Part 2: 116

def find_sum(l, n):
	for i in range(len(l)):
		for j in range(i + 1, len(l)):
			if l[i] + l[j] == n:
				return True
	return False

data = open("Day9.txt", "r").read()
data = data.split("\n")
data = list(map(int, data))

total = 0

i = 25
while i < len(data):
	prev = data[i - 25:i]
	if not find_sum(prev, data[i]):
		print(data[i])
	i += 1

n = 20874512
i = 0
while i < len(data):
	j = i
	cur_total = 0
	while cur_total < n:
		cur_total += data[j]
		j += 1
	print(j)
	if cur_total == n:
		print(min(data[i:j + 1]) + max(data[i:j + 1]))
		break
	i += 1
print(i)