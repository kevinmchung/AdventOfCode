default_prog = list(map(int, open("Day2.txt", "r").readline().split(",")))

# 1202 program alarm
# prog[1] = 12
# prog[2] = 2

for j in range(100):
	for k in range(100):

		prog = default_prog.copy()

		prog[1] = j
		prog[2] = k

		i = 0
		while prog[i] != 99:
			if prog[i] == 1:
				prog[prog[i + 3]] = prog[prog[i + 1]] + prog[prog[i + 2]]
			elif prog[i] == 2:
				prog[prog[i + 3]] = prog[prog[i + 1]] * prog[prog[i + 2]]
			else:
				break
			i += 4

		if prog[0] == 19690720:
			print(j, k)
			exit()