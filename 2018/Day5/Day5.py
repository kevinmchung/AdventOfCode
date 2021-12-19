import re

alpha = "abcdefghijklmnopqrstuvwxyz"

def react(poly):
	while True:
		s = re.search(r"([a-z])(?!\1)(?i:\1)|([A-Z])(?!\2)(?i:\2)", poly)
		if s:
			poly = re.sub(r"([a-z])(?!\1)(?i:\1)|([A-Z])(?!\2)(?i:\2)", "", poly)
		else:
			break

	return poly

inp = open("Day5.txt", "r").read()

print(len(react(inp)))

shortest = len(inp)

for c in alpha:
	print(c)
	reduced = re.sub("{}|{}".format(c, c.upper()), "", inp)
	r = react(reduced)
	if len(r) < shortest:
		shortest = len(r)

print(shortest)