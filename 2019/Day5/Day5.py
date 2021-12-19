prog = list(map(int, open("Day5.txt", "r").readline().split(",")))

# 1202 program alarm
# prog[1] = 12
# prog[2] = 2

i = 0

while prog[i] != 99:

	instruction = "{:>05d}".format(prog[i])
	opcode = int(instruction[3:])

	if opcode < 3:
		modes = list(map(int, instruction[:3]))[::-1]
	elif opcode < 5:
		modes = [int(instruction[2])]
	elif opcode < 7:
		modes = list(map(int, instruction[1:3]))[::-1]
	else:
		modes = list(map(int, instruction[:3]))[::-1]

	parameters = []

	for j in range(len(modes)):
		if not ((opcode > 6 or opcode < 4) and j == len(modes) - 1) and modes[j] == 0:
			parameters.append(prog[prog[i + j + 1]])
		else:
			parameters.append(prog[i + j + 1])

	add = True
	if opcode == 1:
		prog[parameters[2]] = parameters[0] + parameters[1]
	elif opcode == 2:
		prog[parameters[2]] = parameters[0] * parameters[1]
	elif opcode == 3:
		prog[parameters[0]] = int(input("Input: "))
	elif opcode == 4:
		print(parameters[0])
	elif opcode == 5:
		if parameters[0] != 0:
			i = parameters[1]
			add = False
	elif opcode == 6:
		if parameters[0] == 0:
			i = parameters[1]
			add = False
	elif opcode == 7:
		prog[parameters[2]] = int(parameters[0] < parameters[1])
	elif opcode == 8:
		prog[parameters[2]] = int(parameters[0] == parameters[1])
	else:
		print("Something went wrong.")
		exit()

	if add:
		i += len(modes) + 1