alpha = "abcdefghijklmnopqrstuvwxyz"

inp = "hxbxxyzz"

while True:
	idx = -1
	while True:
		if inp[idx] == "z":
			inp = inp[:idx] + "a" + (inp[idx + 1:] if idx < -1 else "")
			idx -= 1
		else:
			inp = inp[:idx] + alpha[alpha.index(inp[idx]) + 1] + (inp[idx + 1:] if idx < -1 else "")
			break
	if not ("i" in inp or "o" in inp or "l" in inp) and any(alpha[i:i+3] in inp for i in range(len(alpha) - 2)):
		doubles = 0
		prev_letter = ""
		for i in range(len(inp)):
			if inp[i] == prev_letter:
				doubles += 1
				prev_letter = ""
			else:
				prev_letter = inp[i]
		if doubles >= 2:
			break

print(inp)