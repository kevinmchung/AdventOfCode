grid = open("Day13.txt", "r").read().split("\n")

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
inter_turns = (-1, 0, 1)

turns = {"/":(1, 0, 3, 2), "\\":(3, 2, 1, 0)}
start_carts = ("^", ">", "v", "<")

class Cart:
	def __init__(self, pos, d):
		self.pos = pos
		self.d = d
		self.next_turn = 0

	def move(self, grid):
		c = grid[self.pos[0]][self.pos[1]]
		if c in turns:
			self.d = turns[c][self.d]
		elif c == "+":
			self.d = (self.d + inter_turns[self.next_turn]) % 4
			self.next_turn = (self.next_turn + 1) % 3
		self.pos[0] += dirs[self.d][0]
		self.pos[1] += dirs[self.d][1]

carts = []
for r in range(len(grid)):
	for c in range(len(grid[r])):
		if grid[r][c] in start_carts:
			cart = Cart([r, c], start_carts.index(grid[r][c]))
			carts.append(cart)
			grid[r] = grid[r][:c] + ("|", "-")[cart.d % 2] + grid[r][c + 1:]

while len(carts) > 1:
	dead = set()
	carts = sorted(carts, key=lambda c: c.pos)
	for i in range(len(carts)):
		if carts[i] in dead:
			continue
		for j in range(len(carts)):
			if i != j and carts[i].pos == carts[j].pos and not carts[j] in dead:
				dead.add(carts[i])
				dead.add(carts[j])
				break
		if carts[i] in dead:
			continue
		carts[i].move(grid)

	carts = [c for c in carts if c not in dead]

print(carts[0].pos)
