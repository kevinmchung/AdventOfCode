import re

class Group:
	def __init__(self, team, num_units, hp, att, att_type, initiative, immune=(), weak=()):
		self.team = team
		self.num_units = num_units
		self.hp = hp
		self.att = att
		self.att_type = att_type
		self.initiative = initiative
		self.immune = immune
		self.weak = weak

	def calc_damage(self, enemy_att, enemy_att_type):
		if enemy_att_type in self.immune:
			return 0
		if enemy_att_type in self.weak:
			return enemy_att * 2
		return enemy_att

	def eff_damage(self):
		return self.num_units * self.att

	def deal_damage(self, enemy_att, enemy_att_type):
		num_died = self.calc_damage(enemy_att, enemy_att_type) // self.hp
		self.num_units -= num_died
		return num_died

def process_line(line, team):
	num_units, hp, att, initiative = map(int, re.findall("\d+", line))
	att_type = re.search("with an attack that does \d+ ([a-z]*) damage", line).groups()[0]
	immune = re.search("immune to ([a-z, ]*)[;\)]", line)
	weak = re.search("weak to ([a-z, ]*)[;\)]", line)
	if immune is None:
		immune = ()
	else:
		immune = tuple(immune.groups()[0].split(", "))

	if weak is None:
		weak = ()
	else:
		weak = tuple(weak.groups()[0].split(", "))

	return Group(team, num_units, hp, att, att_type, initiative, immune, weak)


data = open("Day24.txt", "r").read().split("\n\n")
immune_system = data[0].split("\n")[1:]
infection = data[1].split("\n")[1:]
original_groups = []

for line in immune_system:
	original_groups.append(process_line(line, "immune"))

for line in infection:
	original_groups.append(process_line(line, "infection"))

def battle(original_groups, boost):
	groups = []
	for g in original_groups:
		new_att = g.att + (boost if g.team == "immune" else 0)
		groups.append(Group(g.team, g.num_units, g.hp, new_att, g.att_type, g.initiative, g.immune, g.weak))
	while len(set(g.team for g in groups if g.num_units > 0)) > 1:
		targets = {}
		groups = sorted(groups, key=lambda g: (g.eff_damage(), g.initiative), reverse=True)
		# for g in groups:
		# 	print(g.team, g.num_units, g.att_type, g.immune, g.weak)
		# print()
		for choosing in groups:
			choices = [g for g in groups if g.num_units > 0 and g not in targets.values() and g.team != choosing.team and
					   g.calc_damage(choosing.eff_damage(), choosing.att_type) > 0]
			if len(choices) > 0:
				targets[choosing] = max(choices, key=lambda g: (g.calc_damage(choosing.eff_damage(), choosing.att_type), g.eff_damage(), g.initiative))

		attackers = list(sorted(targets.keys(), key=lambda g: g.initiative, reverse=True))
		any_died = False
		for attacker in attackers:
			if attacker.num_units > 0:
				if targets[attacker].deal_damage(attacker.eff_damage(), attacker.att_type) > 0:
					any_died = True

		if not any_died:
			return None

	if list(set(g.team for g in groups if g.num_units > 0))[0] == "immune":
		total = 0
		for g in groups:
			# print(g.team, g.num_units)
			if g.num_units > 0:
				total += g.num_units
		return total
	else:
		return None

boost = 39
while True:
	print(boost)
	outcome = battle(original_groups, boost)
	if outcome is not None:
		print(outcome)
		break
	boost += 1