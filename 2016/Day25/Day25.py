def valid_pattern(string):
	t = 0
	for i in range(len(string)):
		if string[::-1][i] != str(t):
			return False
		t = (t + 1) % 2
	return True

a = 0
const = 231 * 11
while True:
	b = bin(const + a)[2:]
	if valid_pattern(b):
		print(a)
		break
	a += 1