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
		self.special_params = (4, 5, 6, 9)

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
			raw_params = []

			for j in range(len(modes)):
				cur_index = self.prog[self.i + j + 1]
				raw_params.append(cur_index)
				if not (opcode not in self.special_params and j == len(modes) - 1) and modes[j] == 0:
					self.extend_memory(cur_index)
					parameters.append(self.prog[cur_index])
				elif modes[j] == 1:
					parameters.append(cur_index)
				elif modes[j] == 2:
					if opcode not in self.special_params and j == len(modes) - 1:
						parameters.append(cur_index + self.relative_base)
					else:
						self.extend_memory(cur_index + self.relative_base)
						parameters.append(self.prog[cur_index + self.relative_base])
				else:
					parameters.append(cur_index)

			# print(self.i, opcode, self.relative_base, modes, raw_params, parameters)

			add = True
			if opcode == 1:
				self.set_index(parameters[2], parameters[0] + parameters[1])
			elif opcode == 2:
				self.set_index(parameters[2], parameters[0] * parameters[1])
			elif opcode == 3:
				self.set_index(parameters[0], inp[self.inp_index])
				self.inp_index += 1
			elif opcode == 4:
				# print(parameters[0])
				# print(self.prog[424:])
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

default_prog = list(map(int, open("Day21.txt", "r").read().split(",")))

walk_code = \
"""NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
"""

run_code = \
"""OR A J
AND B J
AND C J
NOT J J
AND D J
OR E T
OR H T
AND T J
RUN
"""

code = list(map(ord, run_code))
prog = Program()
prog.run(code)

out = prog.get_output()
for c in out:
	try:
		print(chr(c), end="")
	except ValueError:
		print(c)