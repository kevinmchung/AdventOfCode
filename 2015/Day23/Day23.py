from collections import defaultdict

code = [line.strip().split(" ") for line in open("Day23.txt", "r").readlines()]
for i in range(len(code)):
	if len(code[i]) == 3:
		code[i][1] = code[i][1][:-1]
		code[i][2] = int(code[i][2])
	if code[i][0] == "jmp":
		code[i][1] = int(code[i][1])

regs = defaultdict(int)
regs["a"] = 1

i = 0
while i < len(code):
	cur = code[i]
	if cur[0] == "hlf":
		regs[cur[1]] /= 2
		i += 1
	elif cur[0] == "tpl":
		regs[cur[1]] *= 3
		i += 1
	elif cur[0] == "inc":
		regs[cur[1]] += 1
		i += 1
	elif cur[0] == "jmp":
		i += cur[1]
	elif cur[0] == "jie":
		if regs[cur[1]] % 2 == 0:
			i += cur[2]
		else:
			i += 1
	elif cur[0] == "jio":
		if regs[cur[1]] == 1:
			i += cur[2]
		else:
			i += 1

print(regs)
