class Elf:
	def __init__(self, n):
		self.n = n
		self.prv = None
		self.nxt = None

	def delete(self):
		self.prv.nxt = self.nxt
		self.nxt.prv = self.prv

inp = 3014387

elves = [Elf(i) for i in range(inp)]
for i in range(inp):
	elves[i].prv = elves[(i - 1) % inp]
	elves[i].nxt = elves[(i + 1) % inp]

cur = elves[0]
mid = elves[inp // 2]
for i in range(inp - 1):
	mid.delete()
	mid = mid.nxt
	if (inp - i) % 2 == 1:
		mid = mid.nxt
	cur = cur.nxt

print(cur.n + 1)