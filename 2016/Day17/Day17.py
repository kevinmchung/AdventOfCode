import hashlib

inp = "mmsxrhfx"

order = "UDLR"
dirs = {"U":(0, -1),
		"D":(0, 1),
		"L":(-1, 0),
		"R":(1, 0)}

q = [((0, 0), "")]
while len(q) > 0:
	pos, seq = q.pop(0)
	if pos == (3, 3):
		print(len(seq))
	else:
		h = hashlib.md5((inp + seq).encode("utf-8")).hexdigest()
		for i in range(4):
			if h[i] in "bcdef":
				d = order[i]
				new_pos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
				if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
					q.append((new_pos, seq + d))
