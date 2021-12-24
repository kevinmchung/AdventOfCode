from collections import defaultdict
prog = [line.strip().split(" ") for line in open("Day24.txt")]

xadd = [10, 15, 14, 15, -8, 10, -16, -4, 11, -3, 12, -7, -15, -7]
yadd = [2, 16, 9, 0, 1, 12, 6, 6, 3, 5, 9, 3, 2, 3]
zdiv = [1, 1, 1, 1, 26, 1, 26, 26, 1, 26, 1, 26, 26, 26]

a = 0
while len(str(a)) <= 7:
	n = list(map(int, str(a).zfill(7)))
	# print(a)
	if 0 in n:
		a += 1
		continue
	ni = 0
	inp = [0 for _ in range(14)]
	for i in range(14):
		if zdiv[i] == 1:
			inp[i] = n[ni]
			ni += 1

	x, z = 0, 0
	for i in range(14):
		x = (z % 26) + xadd[i]
		z //= zdiv[i]
		if zdiv[i] == 26 and 1 <= x <= 9:
			inp[i] = x
		else:
			z *= 26
			z += inp[i] + yadd[i]
	if z == 0:
		print("".join(map(str, inp)))
		break
	a += 1