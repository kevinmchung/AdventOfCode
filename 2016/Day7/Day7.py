import re

def has_abba(string):
	for i in range(len(string) - 3):
		if string[i] != string[i + 1] and string[i:i + 2][::-1] == string[i + 2:i + 4]:			return True
	return False

def find_abas(string):
	out = set()
	for i in range(len(string) - 2):
		if string[i] == string[i + 2] and string[i] != string[i + 1]:
			out.add(string[i:i + 3])
	return out

total = 0
data = open("Day7.txt", "r").read().split("\n")
for line in data:
	inside = re.findall("\[(.*?)\]", line)
	outside = re.split("\[.*?\]", line)
	# if all(not has_abba(s) for s in inside) and any(has_abba(s) for s in outside):
	# 	total += 1

	inside_abas = set.union(*map(find_abas, inside))
	outside_abas = set.union(*map(find_abas, outside))

	has_match = False
	for iaba in inside_abas:
		if any(iaba[0] == oaba[1] and iaba[1] == oaba[0] for oaba in outside_abas):
			has_match = True
			break

	if has_match:
		total += 1

print(total)