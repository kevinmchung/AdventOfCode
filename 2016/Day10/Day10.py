import re
from collections import defaultdict

data = open("Day10.txt", "r").read().split("\n")
vals = defaultdict(list)
rules = {}

for line in data:
	rule = re.match("bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)", line)
	val = re.match("value (\d+) goes to bot (\d+)", line)
	if rule:
		d = rule.groups()
		rules[int(d[0])] = ((d[1][0], int(d[2])), (d[3][0], int(d[4])))
	elif val:
		v, bot_id = map(int, val.groups())
		vals[bot_id].append(v)

outputs = {}
while True:
	bot = None
	for b in vals:
		if len(vals[b]) == 2:
			bot = b
			break
	if bot is None:
		break

	if 61 in vals[bot] and 17 in vals[bot]:
		print(bot)
	rule = rules[bot]

	if rule[0][0] == "b":
		vals[rule[0][1]].append(min(vals[bot]))
	else:
		outputs[rule[0][1]] = min(vals[bot])

	if rule[1][0] == "b":
		vals[rule[1][1]].append(max(vals[bot]))
	else:
		outputs[rule[1][1]] = max(vals[bot])

	vals[bot] = []

print(outputs[0] * outputs[1] * outputs[2])