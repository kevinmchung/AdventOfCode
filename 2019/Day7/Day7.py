import itertools

class Amp:
	def __init__(self, phase):
		self.phase = phase
		self.prog = default_prog.copy()
		self.in_index = 0
		self.i = 0

	def get_output(self, inp=None):
		while self.prog[self.i] != 99:

			instruction = "{:>05d}".format(self.prog[self.i])
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
					parameters.append(self.prog[self.prog[self.i + j + 1]])
				else:
					parameters.append(self.prog[self.i + j + 1])

			ret = False
			add = True
			toret = None
			if opcode == 1:
				self.prog[parameters[2]] = parameters[0] + parameters[1]
			elif opcode == 2:
				self.prog[parameters[2]] = parameters[0] * parameters[1]
			elif opcode == 3:
				if self.in_index == 0:
					self.prog[parameters[0]] = self.phase
				else:
					self.prog[parameters[0]] = inp
				self.in_index += 1
			elif opcode == 4:
				ret = True
				toret = parameters[0]
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
			else:
				print("Something went wrong.")
				exit()

			if add:
				self.i += len(modes) + 1
			if ret:
				return toret

		return None


default_prog = list(map(int, open("Day7.txt", "r").readline().split(",")))

# 1202 program alarm
# prog[1] = 12
# prog[2] = 2

amp_config = "98765"

max_val = 0


for amp in itertools.permutations(amp_config):
	amps = [Amp(int(i)) for i in amp]
	cur_val = 0
	i = 0
	last_val = 0
	while cur_val is not None:
		last_val = cur_val
		cur_val = amps[i].get_output(cur_val)
		i = (i + 1) % 5
	if last_val > max_val:
		max_val = last_val

print(max_val)


