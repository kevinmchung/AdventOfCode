from collections import defaultdict

data = open("Day23.txt", "r").read().split("\n")

vals = defaultdict(int)
vals["a"] = 7

instructions = []
for line in data:
	instructions.append(line.split(" "))

def evaluate(i):
	try:
		return int(i)
	except ValueError:
		return vals[i]

toggle = {"cpy":"jnz",
		  "jnz":"cpy",
		  "inc":"dec",
		  "dec":"inc",
		  "tgl":"inc"}

i = 0
while i < len(instructions):
	cur = instructions[i]
	if cur[0] == "cpy":
		vals[cur[2]] = evaluate(cur[1])
		i += 1
	elif cur[0] == "inc":
		vals[cur[1]] += 1
		i += 1
	elif cur[0] == "dec":
		vals[cur[1]] -= 1
		i += 1
	elif cur[0] == "jnz":
		if evaluate(cur[1]) != 0:
			i += evaluate(cur[2])
		else:
			i += 1
	elif cur[0] == "tgl":
		idx = i + evaluate(cur[1])
		if idx < len(instructions):
			instructions[idx][0] = toggle[instructions[idx][0]]
		i += 1

print(vals)