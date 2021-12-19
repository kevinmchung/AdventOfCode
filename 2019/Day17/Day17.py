class Program:
	def __init__(self, prog=None, relative_base=0, i=0):
		if prog is None:
			self.prog = default_prog.copy()
		else:
			self.prog = prog.copy()
		self.relative_base = relative_base
		self.i = i
		self.output = []
		self.inp_index = 0

	def extend_memory(self, index):
		if index >= len(self.prog):
			self.prog.extend([0 for k in range(index - len(self.prog) + 1)])

	def set_index(self, index, value):
		self.extend_memory(index)
		self.prog[index] = value

	def run(self, inp=None):
		while self.prog[self.i] != 99:

			instruction = "{:>05d}".format(self.prog[self.i])
			opcode = int(instruction[3:])

			if opcode < 3:
				modes = list(map(int, instruction[:3]))[::-1]
			elif opcode < 5 or opcode == 9:
				modes = [int(instruction[2])]
			elif opcode < 7:
				modes = list(map(int, instruction[1:3]))[::-1]
			else:
				modes = list(map(int, instruction[:3]))[::-1]

			parameters = []

			for j in range(len(modes)):
				cur_index = self.prog[self.i + j + 1]
				if not ((9 > opcode > 6 or opcode < 4) and j == len(modes) - 1) and modes[j] == 0:
					self.extend_memory(cur_index)
					parameters.append(self.prog[cur_index])
				elif modes[j] == 1:
					parameters.append(cur_index)
				elif modes[j] == 2:
					if (9 > opcode > 6 or opcode < 4) and j == len(modes) - 1:
						parameters.append(cur_index + self.relative_base)
					else:
						self.extend_memory(cur_index + self.relative_base)
						parameters.append(self.prog[cur_index + self.relative_base])
				else:
					parameters.append(cur_index)

			add = True
			if opcode == 1:
				self.set_index(parameters[2], parameters[0] + parameters[1])
			elif opcode == 2:
				self.set_index(parameters[2], parameters[0] * parameters[1])
			elif opcode == 3:
				self.set_index(parameters[0], ord(inp[self.inp_index]))
				self.inp_index += 1
			elif opcode == 4:
				self.output.append(parameters[0])
			elif opcode == 5:
				if parameters[0] != 0:
					self.i = parameters[1]
					add = False
			elif opcode == 6:
				if parameters[0] == 0:
					self.i = parameters[1]
					add = False
			elif opcode == 7:
				self.set_index(parameters[2], int(parameters[0] < parameters[1]))
			elif opcode == 8:
				self.set_index(parameters[2], int(parameters[0] == parameters[1]))
			elif opcode == 9:
				self.relative_base += parameters[0]
			else:
				print("Something went wrong.")
				exit()

			if add:
				self.i += len(modes) + 1

		return None

	def get_output(self):
		return self.output

	def __copy__(self):
		return type(self)(self.prog, self.relative_base, self.i)

def robot_coords(grid):
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == "^":
				return r, c

def get_long_program(grid):
	cur_pos = list(robot_coords(grid))
	cur_dir = 0
	output = []
	while True:
		turned = False
		for i in range(4):
			if i != cur_dir and i != (cur_dir + 2) % 4 and \
					0 <= cur_pos[0] + directions[i][0] < len(grid) and \
					0 <= cur_pos[1] + directions[i][1] < len(grid[0]) and \
					grid[cur_pos[0] + directions[i][0]][cur_pos[1] + directions[i][1]] == "#":
				turn = (i - cur_dir) % 4
				cur_dir = i
				turned = True
				if turn == 3:
					output.append("L")
				else:
					output.append("R")
				break
		if not turned:
			break
		d = 1
		dr, dc = directions[cur_dir]
		while 0 <= cur_pos[0] + dr * d < len(grid) and \
				0 <= cur_pos[1] + dc * d < len(grid[0]) and \
				grid[cur_pos[0] + dr * d][cur_pos[1] + dc * d] == "#":
			d += 1
		d -= 1
		output.append(str(d))
		cur_pos = [cur_pos[0] + dr * d, cur_pos[1] + dc * d]

	return output

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
default_prog = list(map(int, open("Day17.txt", "r").read().split(",")))

# prog = Program()
#
# prog.run()
# output = prog.get_output()
#
# grid = []
# row = []
# for c in output:
# 	if c == 10 and len(row) > 0:
# 		grid.append(row)
# 		row = []
# 	else:
# 		row.append(chr(c))

# for row in grid:
# 	print("".join(row))

# intersections = 0
# for r in range(len(grid)):
# 	for c in range(len(grid[0])):
# 		if grid[r][c] == "#":
# 			intersection = True
# 			for dr, dc in directions:
# 				if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == ".":
# 					intersection = False
# 			if intersection:
# 				intersections += r * c
#
# print(intersections)

# print(",".join(get_long_program(grid)))

main = "C,C,A,B,A,B,A,B,A,C"
A = "L,12,R,6,L,8,L,12"
B = "R,12,L,10,L,10"
C = "R,6,L,12,R,6"

inp = "\n".join([main, A, B, C, "n"]) + "\n"

default_prog[0] = 2
prog2 = Program()
prog2.run(inp)
print(prog2.get_output()[-1])