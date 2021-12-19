# Part 1: 577
# Part 2: 114

data = open("Day14.txt", "r").read().split("\n")
# data = list(map(int, data))

def all_possible(b):
	if "X" not in b:
		return [b]
	for i in range(len(b)):
		if b[i] == "X":
			return all_possible(b[:i] + "0" + b[i + 1:]) + all_possible(b[:i] + "1" + b[i + 1:])

mask = data[0].split(" = ")[1]

mem = {}

data = data[1:]

# for line in data:
# 	line = line.split(" = ")
# 	if line[0] == "mask":
# 		mask = line[1]
# 	else:
# 		idx = line[0][line[0].find("[") + 1:line[0].find("]")]
# 		b = bin(int(line[1]))[2:]
# 		i = 1
# 		while i <= len(mask):
# 			if i > len(b):
# 				b = "0" + b
# 			if mask[-i] != "X":
# 				b = b[:-i] + mask[-i] + (b[-i + 1:] if i != 1 else "")
# 			i += 1
# 		print(mask)
# 		print(b)
# 		print("----")
# 		mem[idx] = int(b, 2)

for line in data:
	line = line.split(" = ")
	if line[0] == "mask":
		mask = line[1]
	else:
		idx = int(line[0][line[0].find("[") + 1:line[0].find("]")])
		b = bin(int(idx))[2:]
		i = 1
		while i <= len(mask):
			if i > len(b):
				b = "0" + b
			if mask[-i] != "0":
				b = b[:-i] + mask[-i] + (b[-i + 1:] if i != 1 else "")
			i += 1
		for add in all_possible(b):
			mem[add] = int(line[1])

print(sum(mem.values()))