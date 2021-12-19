def fill(a):
	b = a[::-1].replace("0", "#")
	b = b.replace("1", "0")
	b = b.replace("#", "1")
	return a + "0" + b

def checksum(seq):
	out = ""
	for i in range(0, len(seq), 2):
		out += "1" if seq[i] == seq[i + 1] else "0"
	return out

inp = "01111010110010011"
target_len = 35651584
while len(inp) < target_len:
	inp = fill(inp)

inp = inp[:target_len]
while len(inp) % 2 == 0:
	inp = checksum(inp)

print(inp)