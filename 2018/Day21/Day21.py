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

data = open("Day21.txt", "r").read().split("\n")
ip = int(data[0].split(" ")[1])

instructions = []
for line in data[1:]:
	line = line.split(" ")
	instructions.append((line[0], tuple(map(int, line[1:]))))

r = [0, 0, 0, 0, 0, 0]

# while r[ip] < len(instructions):
# 	if r[ip] == 28:
# 		print(r)
# 	inst = instructions[r[ip]]
# 	r = evaluate(r, inst[0], inst[1])
# 	# print(r)
# 	r[ip] += 1

seen = set()
# PART 2
while True:
	r[4] = r[5] | 65536
	r[5] = 13431073
	while True:
		r[3] = r[4] & 255
		r[5] += r[3]
		r[5] = r[5] & 16777215
		r[5] *= 65899
		r[5] = r[5] & 16777215
		if 256 > r[4]:
			if r[5] not in seen:
				print(r[5])
				seen.add(r[5])
			if r[0] == r[5]:
				exit()
			else:
				break
		else:
			r[4] //= 256
