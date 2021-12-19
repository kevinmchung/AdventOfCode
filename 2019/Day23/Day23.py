from collections import defaultdict

class Program:
	def __init__(self, prog=None, relative_base=0, i=0):
		if prog is None:
			self.prog = default_prog.copy()
		else:
			self.prog = prog.copy()
		self.relative_base = relative_base
		self.i = i
		self.inp = []
		self.output = []
		self.special_params = (4, 5, 6, 9)

	def extend_memory(self, index):
		if index >= len(self.prog):
			self.prog.extend([0 for k in range(index - len(self.prog) + 1)])

	def set_index(self, index, value):
		self.extend_memory(index)
		self.prog[index] = value

	def run(self):
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
				if len(self.inp) == 0:
					return "input"
				self.set_index(parameters[0], self.inp.pop(0))
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

	def write(self, l):
		for n in l:
			self.inp.append(n)

	def read(self, n=1):
		if len(self.output) >= n:
			out = []
			for i in range(n):
				out.append(self.output.pop(0))
			return out
		return None

	def __copy__(self):
		return type(self)(self.prog, self.relative_base, self.i)

def pt1():
	computers = [Program() for i in range(50)]
	for i in range(50):
		computers[i].write([i])
	packets = defaultdict(list)

	ans = None
	while ans is None:
		sent = 0
		for i in range(50):
			if len(packets[i]) == 0:
				computers[i].write([-1])
			else:
				computers[i].write(packets[i].pop(0))
			res = computers[i].run()
			if res == "input":
				new_packet = computers[i].read(3)
				if new_packet is not None:
					if new_packet[0] == 255:
						ans = new_packet[2]
						break
					packets[new_packet[0]].append(new_packet[1:])
			else:
				exit("ERROR")
	# print(packets)

	return ans

def pt2():
	computers = [Program() for i in range(50)]
	for i in range(50):
		computers[i].write([i])
	packets = defaultdict(list)

	seen = set()
	ans = None
	while ans is None:
		sent = 0
		for i in range(50):
			if len(packets[i]) == 0:
				computers[i].write([-1])
			else:
				computers[i].write(packets[i].pop(0))
			res = computers[i].run()
			if res == "input":
				new_packet = computers[i].read(3)
				if new_packet is not None:
					if new_packet[0] == 0:
						y = new_packet[2]
						if y in seen:
							ans = y
							break
						seen.add(y)
					packets[new_packet[0]].append(new_packet[1:])
					sent += 1
			else:
				exit("ERROR")

		if sent == 0:
			packets[0].append(packets[255][-1])
			y = packets[255][-1][1]
			if y in seen:
				ans = y
				break
			seen.add(y)
	# print(packets)

	return ans

default_prog = list(map(int, open("Day23.txt", "r").read().split(",")))

print(pt1())
print(pt2())