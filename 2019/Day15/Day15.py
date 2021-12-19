from copy import copy

class Robot:
	def __init__(self, prog=None, relative_base=0, i=0):
		if prog is None:
			self.prog = default_prog.copy()
		else:
			self.prog = prog.copy()
		self.relative_base = relative_base
		self.i = i

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

	def __copy__(self):
		return type(self)(self.prog, self.relative_base, self.i)

def shortest_path():
	queue = [(Robot(), (0, 0), 0)]
	visited = {(0, 0)}
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	while len(queue) > 0:
		bot, pos, depth = queue.pop(0)
		for i in range(4):
			dx, dy = directions[i]
			new_pos = (pos[0] + dx, pos[1] + dy)
			if new_pos not in visited:
				new_bot = copy(bot)
				out = new_bot.get_output(i + 1)
				if out == 0:
					# Hit a wall
					pass
				elif out == 1:
					queue.append((new_bot, new_pos, depth + 1))
				elif out == 2:
					return new_bot, new_pos, depth + 1
				else:
					print("Something went wrong.")
					exit()
				visited.add(new_pos)
	return None


def minutes_to_fill(bot_on_oxygen, oxygen_pos):
	queue = [(bot_on_oxygen, oxygen_pos, 0)]
	visited = {oxygen_pos}
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	largest_depth = 0
	while len(queue) > 0:
		bot, pos, depth = queue.pop(0)
		largest_depth = depth
		for i in range(4):
			dx, dy = directions[i]
			new_pos = (pos[0] + dx, pos[1] + dy)
			if new_pos not in visited:
				new_bot = copy(bot)
				out = new_bot.get_output(i + 1)
				if out == 0:
					pass
				elif out == 1:
					queue.append((new_bot, new_pos, depth + 1))
				else:
					print("Something went wrong.")
					exit()
				visited.add(new_pos)
	return largest_depth

lines = [line.strip() for line in open("Day15.txt", "r").readlines()]

default_prog = list(map(int, lines[0].split(",")))

bot_on_oxygen, oxygen_pos, depth = shortest_path()

print(minutes_to_fill(bot_on_oxygen, oxygen_pos))