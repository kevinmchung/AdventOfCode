class Robot:
	def __init__(self):
		self.prog = default_prog.copy()
		self.relative_base = 0
		self.i = 0

	def set_index(self, index, value):
		if index >= len(self.prog):
			self.prog.extend([0 for k in range(index - len(self.prog) + 1)])
		self.prog[index] = value

	def get_output(self, inp=None):
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
					parameters.append(self.prog[cur_index])
				elif modes[j] == 1:
					parameters.append(cur_index)
				elif modes[j] == 2:
					if (9 > opcode > 6 or opcode < 4) and j == len(modes) - 1:
						parameters.append(cur_index + self.relative_base)
					else:
						parameters.append(self.prog[cur_index + self.relative_base])
				else:
					parameters.append(cur_index)

			add = True
			if opcode == 1:
				self.set_index(parameters[2], parameters[0] + parameters[1])
			elif opcode == 2:
				self.set_index(parameters[2], parameters[0] * parameters[1])
			elif opcode == 3:
				self.set_index(parameters[0], inp)
			elif opcode == 4:
				self.i += len(modes) + 1
				return parameters[0]
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

grid = [[0 for i in range(101)] for j in range(101)]
painted = [[False for i in range(101)] for j in range(101)]
pos = [50, 50]

# Emergency hull
grid[pos[0]][pos[1]] = 1

direction = 0
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

default_prog = list(map(int, open("Day11.txt", "r").read().split(",")))
robot = Robot()

while True:
	new_color = robot.get_output(grid[pos[0]][pos[1]])
	if new_color is None:
		break
	if new_color != grid[pos[0]][pos[1]]:
		grid[pos[0]][pos[1]] = new_color
		painted[pos[0]][pos[1]] = True
	new_dir = robot.get_output(grid[pos[0]][pos[1]])
	if new_dir == 0:
		direction = (direction - 1) % 4
	else:
		direction = (direction + 1) % 4
	pos[0] += directions[direction][0]
	pos[1] += directions[direction][1]

# total = 0
# for r in range(101):
# 	for c in range(101):
# 		if painted[r][c]:
# 			total += 1
#
# print(total)

print("\n".join("".join(map(str, row)) for row in grid))