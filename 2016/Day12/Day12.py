from collections import defaultdict

data = open("Day12.txt", "r").read().split("\n")

vals = defaultdict(int)
vals["c"] = 1

instructions = []
for line in data:
	instructions.append(line.split(" "))

def evaluate(i):
	if i.isnumeric():
		return int(i)
	else:
		return vals[i]

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
			i += int(cur[2])
		else:
			i += 1

print(vals)