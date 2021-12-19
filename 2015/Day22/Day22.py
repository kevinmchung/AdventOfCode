from copy import copy

# effect: (dmg, hp)
# timer_effect: (dmg, armor, mana)

class Attack:
	def __init__(self, cost, effect, timer_length=0, timer_effect=None):
		self.cost = cost
		self.effect = effect
		self.timer_length = timer_length
		self.timer_effect = timer_effect

	def __eq__(self, other):
		return self.cost == other.cost

class Battle:
	def __init__(self, hp=50, mana=500, boss_hp=51, boss_dmg=9, spent=0):
		self.hp = hp
		self.armor = 0
		self.mana = mana
		self.spent = spent
		self.boss_hp = boss_hp
		self.boss_dmg = boss_dmg
		self.attacks = []
		self.live_attacks = []

	def run_live_attacks(self):
		i = 0
		while i < len(self.live_attacks):
			self.live_attacks[i][0] += 1
			att = self.live_attacks[i][1]
			self.boss_hp -= att.timer_effect[0]
			self.armor += att.timer_effect[1]
			self.mana += att.timer_effect[2]
			if self.live_attacks[i][0] == att.timer_length:
				self.live_attacks.pop(i)
			else:
				i += 1

	def use_attack(self, attack, debug=False):
		if debug: print("PLAYER TURN")
		self.hp -= 1
		if self.hp <= 0:
			return "lost"

		self.attacks.append(attack.cost)

		self.spent += attack.cost
		self.mana -= attack.cost

		self.run_live_attacks()

		self.boss_hp -= attack.effect[0]
		self.hp += attack.effect[1]

		if attack.timer_effect is not None:
			self.live_attacks.append([0, attack])

		if debug: print(attack.cost, self.hp, self.boss_hp, self.mana)


		if self.boss_hp <= 0:
			return "won"

		self.armor = 0
		# BOSS TURN
		if debug: print("BOSS TURN")
		self.run_live_attacks()
		if self.boss_hp <= 0:
			return "won"

		boss_attack = self.boss_dmg - self.armor
		if boss_attack < 1:
			boss_attack = 1

		self.hp -= boss_attack
		if self.hp <= 0:
			return "lost"

		if debug: print(self.hp, self.boss_hp, self.mana)

		return "continue"

	def __copy__(self):
		new_b = Battle(self.hp, self.mana, self.boss_hp, self.boss_dmg, self.spent)
		new_b.live_attacks = [[live[0], live[1]] for live in self.live_attacks]
		new_b.attacks = self.attacks[:]
		return new_b

	def __hash__(self):
		return hash((self.hp, self.mana, self.spent, self.boss_hp, self.boss_dmg, map(tuple, sorted(self.live_attacks))))

attacks = [Attack(53, (4, 0)),
		   Attack(73, (2, 2)),
		   Attack(113, (0, 0), 6, (0, 7, 0)),
		   Attack(173, (0, 0), 6, (3, 0, 0)),
		   Attack(229, (0, 0), 5, (0, 0, 101))]

# b = Battle()
# print(b.use_attack(attacks[3]))
# print(b.use_attack(attacks[0]))

q = [Battle()]
visited = {q[0]}
while len(q) > 0:
	cur = q.pop(0)
	for att in attacks:
		if att.cost <= cur.mana and all(att != live[1] or (att == live[1] and live[0] == att.timer_length - 1) for live in cur.live_attacks):
			new_b = copy(cur)
			res = new_b.use_attack(att)
			if res == "won":
				print(new_b.spent)
				test_b = Battle()
				for attack in new_b.attacks:
					for a in attacks:
						if a.cost == attack:
							test_b.use_attack(a, debug=True)
							# print(attack, test_b.boss_hp, test_b.hp)
							break
				exit()
			if res == "continue":
				if new_b not in visited:
					q.append(new_b)
	q = sorted(q, key=lambda b:b.spent)