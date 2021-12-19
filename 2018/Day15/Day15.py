from copy import copy
from collections import defaultdict

class Unit:
	def __init__(self, team, pos, att=3, hp=200):
		self.team = team
		self.pos = pos
		self.att = att
		self.hp = hp
		self.alive = True

	def __str__(self):
		return "{}({})".format(self.team, self.hp)

	def __copy__(self):
		return Unit(self.team, self.pos, self.att, self.hp)

grid = open("Day15.txt", "r").read().split("\n")

units = []
walls = set()

for r in range(len(grid)):
	for c in range(len(grid[0])):
		if grid[r][c] == "#":
			walls.add((r, c))
		elif grid[r][c] != ".":
			units.append(Unit(grid[r][c], (r, c)))

other = {"G":"E", "E":"G"}
dirs = ((-1, 0), (0, 1), (0, -1), (1, 0))

def solve(units, elf_death=False):
	turn = 0
	while True:

		units = sorted(units, key=lambda u: u.pos)

		for unit in units:
			if unit.alive:
				spots = defaultdict(list)
				for u in units:
					if u.alive and u.team == other[unit.team]:
						for d in dirs:
							if (u.pos[0] + d[0], u.pos[1] + d[1]) not in walls:
								spots[(u.pos[0] + d[0], u.pos[1] + d[1])].append(u)

				if unit.pos not in spots:
					q = [(unit.pos,)]
					visited = set()
					move = None
					occupied = {u.pos for u in units if u.alive}
					while len(q) > 0:
						cur = q.pop(0)
						if cur[-1] in spots:
							move = cur[1]
							break
						for d in dirs:
							new_pos = (cur[-1][0] + d[0], cur[-1][1] + d[1])
							if new_pos not in walls and new_pos not in visited and new_pos not in occupied:
								visited.add(new_pos)
								q.append(cur + (new_pos,))
					if move:
						unit.pos = move

				if unit.pos in spots:
					to_att = min(spots[unit.pos], key=lambda u: (u.hp, u.pos))
					if to_att.hp > 0:
						to_att.hp -= unit.att
						if to_att.hp <= 0:
							if elf_death and to_att.team == "E":
								return -1
							to_att.alive = False

					alive = [u for u in units if u.alive]
					if len(set(u.team for u in alive)) == 1:
						if unit == alive[-1]:
							turn += 1
						print(turn, sum(u.hp for u in units if u.alive))
						return turn * sum(u.hp for u in units if u.alive)

		turn += 1

		positions = {}
		for unit in units:
			if unit.alive:
				positions[unit.pos] = unit

		print(turn)
		for r in range(len(grid)):
			healths = []
			for c in range(len(grid[0])):
				if (r, c) in walls:
					print("#", end="")
				elif (r, c) in positions:
					print(positions[(r, c)].team, end="")
					healths.append(positions[(r, c)])
				else:
					print(".", end="")
			print("  " + ", ".join(map(str, healths)))
		print()

new_units = [copy(unit) for unit in units]
print(solve(new_units))

a = 3
out = -1
while out == -1:
	new_units = [copy(unit) for unit in units]
	a += 1
	for unit in new_units:
		if unit.team == "E":
			unit.att = a
	out = solve(new_units, elf_death=True)
print(a, out)

# 78 2843
# Part 1 221754
# 28 1499
# 34
# Part 2 41972
