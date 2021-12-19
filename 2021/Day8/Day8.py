from collections import defaultdict
from copy import deepcopy

lines = [line.strip() for line in open("Day8.txt", "r")]
# lines = list(map(int, lines))

nums = [[0, 1, 2, 4, 5, 6],
		[2, 5],
		[0, 2, 3, 4, 6],
		[0, 2, 3, 5, 6],
		[1, 2, 3, 5],
		[0, 1, 3, 5, 6],
		[0, 1, 3, 4, 5, 6],
		[0, 2, 5],
		[0, 1, 2, 3, 4, 5, 6],
		[0, 1, 2, 3, 5, 6]]
nums = [set(n) for n in nums]

ans = 0
for i in range(len(lines)):
	line = lines[i]
	poss = [set("abcdefg") for i in range(7)]
	inp, out = line.split(" | ")
	inp = inp.split(" ")
	out = out.split(" ")
	inp = sorted(inp, key=lambda f: len(f))
	for n in inp:
		if len(n) == 2:
			for l in [2, 5]:
				poss[l] = set(poss[l]).intersection(list(n))
			for j in range(7):
				if j not in [2, 5]:
					poss[j] = poss[j].difference(poss[2])
		elif len(n) == 3:
			poss[0] = set(list(set(n).difference(poss[2]))[0])
			for j in range(7):
				if j != 0:
					poss[j] = poss[j].difference(poss[0])
		elif len(n) == 4:
			poss[1] = set(n).difference(poss[2])
			poss[3] = set(n).difference(poss[2])
			for j in range(7):
				if j not in [1, 3]:
					poss[j] = poss[j].difference(poss[1])

	for m in range(8):
		b = bin(m)[2:].zfill(3)
		mapping = []
		for j in range(7):
			if len(poss[j]) == 1:
				mapping.append(list(poss[j])[0])
			elif j == 1:
				mapping.append(list(poss[j])[int(b[0])])
			elif j == 2:
				mapping.append(list(poss[j])[int(b[1])])
			elif j == 3:
				mapping.append(list(poss[j])[not int(b[0])])
			elif j == 4:
				mapping.append(list(poss[j])[int(b[2])])
			elif j == 5:
				mapping.append(list(poss[j])[not int(b[1])])
			else:
				mapping.append(list(poss[j])[not int(b[2])])
		valid = True
		for n in inp:
			segs = set()
			for c in n:
				segs.add(mapping.index(c))
			if segs not in nums:
				valid = False
				break
		if valid:
			output = ""
			for n in out:
				segs = set()
				for c in n:
					segs.add(mapping.index(c))
				output += str(nums.index(segs))

			print(int(output))
			ans += int(output)

print(ans)