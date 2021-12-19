data = open("Day21.txt", "r").read().split("\n")

def p1(cur):
	debug = [cur]
	for line in data:
		p = line.split(" ")
		if p[0] == "swap":
			if p[1] == "position":
				positions = [int(p[2]), int(p[5])]
				l, h = sorted(positions)
				cur = cur[:l] + cur[h] + cur[l + 1:h] + cur[l] + cur[h + 1:]
			else:
				cur = cur.replace(p[2], "#")
				cur = cur.replace(p[5], p[2])
				cur = cur.replace("#", p[5])
		elif p[0] == "rotate":
			if p[1] == "left":
				start = int(p[2]) % len(cur)
			elif p[1] == "right":
				start = -int(p[2]) % len(cur)
			else:
				idx = cur.index(p[6])
				start = -(1 + idx + (idx >= 4)) % len(cur)
			cur = cur[start:] + cur[:start]
		elif p[0] == "reverse":
			l, h = int(p[2]), int(p[4])
			cur = cur[:l] + cur[l:h + 1][::-1] + cur[h + 1:]
		elif p[0] == "move":
			o, n = int(p[2]), int(p[5])
			c = cur[o]
			cur = cur[:o] + cur[o + 1:]
			cur = cur[:n] + c + cur[n:]
		debug.append(cur)
	print(debug)
	return cur

def p2(cur):
	debug = [cur]
	for line in data[::-1]:
		p = line.split(" ")
		if p[0] == "swap":
			if p[1] == "position":
				positions = [int(p[2]), int(p[5])]
				l, h = sorted(positions)
				cur = cur[:l] + cur[h] + cur[l + 1:h] + cur[l] + cur[h + 1:]
			else:
				cur = cur.replace(p[2], "#")
				cur = cur.replace(p[5], p[2])
				cur = cur.replace("#", p[5])
		elif p[0] == "rotate":
			if p[1] == "right":
				start = int(p[2]) % len(cur)
			elif p[1] == "left":
				start = -int(p[2]) % len(cur)
			else:
				idx = cur.index(p[6])
				old_idx = idx - 1
				if old_idx % 2 == 1:
					old_idx = (old_idx - 1) % len(cur)
					old_idx += len(cur)
				old_idx //= 2
				start = (1 + old_idx + (old_idx >= 4)) % len(cur)
			cur = cur[start:] + cur[:start]
		elif p[0] == "reverse":
			l, h = int(p[2]), int(p[4])
			cur = cur[:l] + cur[l:h + 1][::-1] + cur[h + 1:]
		elif p[0] == "move":
			n, o = int(p[2]), int(p[5])
			c = cur[o]
			cur = cur[:o] + cur[o + 1:]
			cur = cur[:n] + c + cur[n:]
		print(line)
		print(cur)
		debug.append(cur)
	print(debug[::-1])
	return cur

# print(p1("abcdefgh"))
# print(p2("bdfhgeca"))
print(p2("fbgdceah"))
# print(p1("ebagcdhf"))
