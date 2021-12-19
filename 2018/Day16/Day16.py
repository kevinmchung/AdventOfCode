from collections import defaultdict

data = open("Day16.txt", "r").read().split("\n\n\n\n")
pt1 = data[0].split("\n\n")
pt2 = data[1].split("\n")

opcodes = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtri", "gtir", "gtrr", "eqir", "eqri", "eqrr"]
ops = {"add":"+", "mul":"*", "ban":"&", "bor":"|", "gt":">", "eq":"=="}

def evaluate(regs, opcode, inps):
	new_regs = [n for n in regs]
	res = -1
	if opcode[:3] in ops:
		if opcode[3] == "r":
			res = eval("{}{}{}".format(regs[inps[0]], ops[opcode[:3]], regs[inps[1]]))
		else:
			res = eval("{}{}{}".format(regs[inps[0]], ops[opcode[:3]], inps[1]))
	elif opcode[:3] == "set":
		if opcode[3] == "r":
			res = regs[inps[0]]
		else:
			res = inps[0]
	elif opcode[:2] in ops:
		if opcode[2] == "r":
			v1 = regs[inps[0]]
		else:
			v1 = inps[0]

		if opcode[3] == "r":
			v2 = regs[inps[1]]
		else:
			v2 = inps[1]

		res = int(eval("{}{}{}".format(v1, ops[opcode[:2]], v2)))

	new_regs[inps[2]] = res
	return new_regs

possible = defaultdict(set)

total = 0
for entry in pt1:
	entry = entry.split("\n")
	inps = list(map(int, entry[1].split(" ")))
	before = eval(entry[0][entry[0].find(" ") + 1:])
	after = eval(entry[2][entry[2].find(" ") + 1:])

	num_ops = 0
	for opcode in opcodes:
		if evaluate(before, opcode, inps[1:]) == after:
			possible[inps[0]].add(opcode)
			num_ops += 1

	if num_ops >= 3:
		total += 1

print(total)

op_key = [None] * 16

while None in op_key:
	for key in possible:
		not_used = []
		for op in possible[key]:
			if op not in op_key:
				not_used.append(op)

		if len(not_used) == 1:
			op_key[key] = not_used[0]

cur = [0, 0, 0, 0]
for line in pt2:
	line = list(map(int, line.split(" ")))
	cur = evaluate(cur, op_key[line[0]], line[1:])

print(cur)