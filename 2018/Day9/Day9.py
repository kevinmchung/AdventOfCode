from collections import defaultdict

num_players = 479
last_marble = 7103500

class Marble:
	def __init__(self, value):
		self.value = value
		self.prv = None
		self.nxt = None

	def delete(self):
		self.prv.nxt = self.nxt
		self.nxt.prv = self.prv

cur_marble = Marble(0)
cur_marble.nxt = cur_marble
cur_marble.prv = cur_marble
turn = 1
scores = defaultdict(int)
while turn <= last_marble:
	# print(turn)
	if turn % 23 == 0:
		scores[turn % num_players] += turn
		cur = cur_marble
		for i in range(7):
			cur = cur.prv
		scores[turn % num_players] += cur.value
		cur.delete()
		cur_marble = cur.nxt
	else:
		new_marble = Marble(turn)
		new_marble.prv = cur_marble.nxt
		new_marble.nxt = cur_marble.nxt.nxt
		cur_marble.nxt.nxt.prv = new_marble
		cur_marble.nxt.nxt = new_marble
		cur_marble = new_marble
	turn += 1

print(max(scores.values()))