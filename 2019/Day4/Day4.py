low = 367479
high = 893698

def check_num(n):
	num = str(n)
	double = False
	i = 0
	while i < len(num):
		cur = num[i]
		count = 0
		while i < len(num) and num[i] == cur:
			if i + 1 < len(num) and int(num[i]) > int(num[i + 1]):
				return False
			count += 1
			i += 1
		if count == 2:
			double = True
	return double

print(check_num(111122))

total = 0

for n in range(low, high + 1):
	if check_num(n):
		total += 1

print(total)
