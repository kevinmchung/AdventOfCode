import math

weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
armors = [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)]
rings = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

class Player:
	def __init__(self, weapon, armor, ring1, ring2):
		self.hp = 100
		self.weapon = weapon
		self.armor = armor
		self.ring1 = ring1
		self.ring2 = ring2

	def damage(self):
		return self.weapon[1] + self.ring1[1] + self.ring2[1]

	def defense(self):
		return self.armor[1] + self.ring1[2] + self.ring2[2]

	def cost(self):
		return self.weapon[0] + self.armor[0] + self.ring1[0] + self.ring2[0]

	def fight(self, enemy_hp, enemy_dmg, enemy_armor):
		my_attack = self.damage() - enemy_armor
		if my_attack < 1:
			my_attack = 1
		enemy_attack = enemy_dmg - self.defense()
		if enemy_attack < 1:
			enemy_attack = 1
		num_my_attacks = math.ceil(enemy_hp / my_attack)
		num_enemy_attacks = math.ceil(self.hp / enemy_attack)
		return num_my_attacks <= num_enemy_attacks

players = []
for w in weapons:
	for a in armors:
		for r1 in range(len(rings)):
			for r2 in range(r1 + 1, len(rings)):
				players.append(Player(w, a, rings[r1], rings[r2]))

boss = (109, 8, 2)

players = sorted(players, key=lambda p: p.cost(), reverse=True)
for player in players:
	if not player.fight(*boss):
		print(player.cost())
		break
