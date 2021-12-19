class Amp:
	def __init__(self):
		self.prog = default_prog.copy()
		self.relative_base = 0
		self.i = 0

	def get_output(self):
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
				if cur_index >= len(self.prog):
					self.prog.extend([0 for k in range(cur_index - len(self.prog) + 1)])
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
				self.prog[parameters[2]] = parameters[0] + parameters[1]
			elif opcode == 2:
				self.prog[parameters[2]] = parameters[0] * parameters[1]
			elif opcode == 3:
				self.prog[parameters[0]] = int(input("Enter number: "))
			elif opcode == 4:
				print(parameters[0])
			elif opcode == 5:
				if parameters[0] != 0:
					self.i = parameters[1]
					add = False
			elif opcode == 6:
				if parameters[0] == 0:
					self.i = parameters[1]
					add = False
			elif opcode == 7:
				self.prog[parameters[2]] = int(parameters[0] < parameters[1])
			elif opcode == 8:
				self.prog[parameters[2]] = int(parameters[0] == parameters[1])
			elif opcode == 9:
				self.relative_base += parameters[0]
			else:
				print("Something went wrong.")
				exit()

			if add:
				self.i += len(modes) + 1

		return None

default_prog = list(map(int, open("Day9.txt", "r").read().split(",")))

amp = Amp()
amp.get_output()
