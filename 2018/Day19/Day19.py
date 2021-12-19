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

data = open("Day19.txt", "r").read().split("\n")
ip = int(data[0].split(" ")[1])

instructions = []
for line in data[1:]:
	line = line.split(" ")
	instructions.append((line[0], tuple(map(int, line[1:]))))

regs = [1, 0, 0, 0, 0, 0]

# PART 2
total = 0
n = 10551367
for i in range(1, n + 1):
	if n % i == 0:
		total += i
print(total)

while regs[ip] < len(instructions):
	inst = instructions[regs[ip]]
	regs = evaluate(regs, inst[0], inst[1])
	# print(regs)
	regs[ip] += 1


print(regs)

