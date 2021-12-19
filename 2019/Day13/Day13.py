class Game:
	def __init__(self):
		self.prog = default_prog.copy()
		self.relative_base = 0
		self.i = 0
		self.grid = [[0 for i in range(45)] for j in range(24)]
		self.output = []
		self.score = 0
		self.ball_pos = -1
		self.paddle_pos = -1

	def display_grid(self):
		print("\n".join("".join(map(str, row)) for row in self.grid))
		print("Score: {}".format(self.score))

	def set_index(self, index, value):
		if index >= len(self.prog):
			self.prog.extend([0 for k in range(index - len(self.prog) + 1)])
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
				self.display_grid()
				move = self.ball_pos - self.paddle_pos
				if move != 0:
					move /= abs(move)
				self.set_index(parameters[0], move)
			elif opcode == 4:
				self.output.append(parameters[0])
				if len(self.output) == 3:
					if self.output[0] == -1:
						self.score = self.output[2]
					else:
						if self.output[2] == 4:
							self.ball_pos = self.output[0]
						elif self.output[2] == 3:
							self.paddle_pos = self.output[0]
						self.grid[self.output[1]][self.output[0]] = self.output[2]
					self.output = []
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

default_prog = list(map(int, open("Day13.txt", "r").read().split(",")))

default_prog[0] = 2

game = Game()
game.run()
game.display_grid()


# total = 0
# for y in range(23):
# 	for x in range(45):
# 		if grid[y][x] == 2:
# 			total += 1
# print(total)
