# Part 1: 1029
# Part 2: 1608

import re

data = open("Day19.txt", "r").read().split("\n\n")
# data = list(map(int, data))

def get_strings(rule, rules):
	if type(rules[rule]) == str:
		return [rules[rule]]
	strings = []
	for sub in rules[rule]:
		cur = [""]
		for r in sub:
			sub_regex = get_strings(r, rules)
			new_cur = []
			for c in cur:
				for s in sub_regex:
					new_cur.append(c + s)
			cur = new_cur
		strings += cur
	return strings

def get_regex(rule, rules):
	if type(rules[rule]) == str:
		return rules[rule]
	if rule == 8 or rule == 11:
		subs = [rules[rule][0]]
	else:
		subs = rules[rule]
	out = []
	for sub in subs:
		cur = ""
		for r in sub:
			cur += get_regex(r, rules) + ("+" if rule == 8 else "") + ("{n}" if rule == 11 else "")
		out.append(cur)
	return "(" + "|".join(out) + ")"



rules = {}
raw_rules = data[0].split("\n")
lines = data[1].split("\n")

for raw in raw_rules:
	raw = raw.split(": ")
	raw[0] = int(raw[0])
	if raw[1] == '"a"':
		rules[raw[0]] = "a"
	elif raw[1] == '"b"':
		rules[raw[0]] = "b"
	else:
		rules[raw[0]] = [list(map(int, r.split(" "))) for r in raw[1].split(" | ")]

reg = get_regex(0, rules)

total = 0
for line in lines:
	for i in range(1, 10):
		res = re.match(reg.replace("n", str(i)), line)
		if res is not None:
			span = res.span()
			if span[0] == 0 and span[1] == len(line):
				total += 1

print(total)
