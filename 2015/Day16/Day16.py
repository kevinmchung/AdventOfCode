data = open("Day16.txt", "r").readlines()

aunts = []
for line in data:
	line = line.strip()
	line = line[line.find(":") + 2:].split(",")
	cur_aunt = {}
	for entry in line:
		entry = entry.split(": ")
		cur_aunt[entry[0].strip()] = int(entry[1])
	aunts.append(cur_aunt)

match = {"children":3, "cats":7, "samoyeds":2, "pomeranians":3, "akitas":0, "vizslas":0, "goldfish":5, "trees":3, "cars":2, "perfumes":1}

# PART 1
# for i in range(len(aunts)):
# 	valid = True
# 	for key in aunts[i]:
# 		if aunts[i][key] != match[key]:
# 			valid = False
# 			break
# 	if valid:
# 		print(i + 1)

# PART 2
greater = ["cats", "trees"]
less = ["pomeranians", "goldfish"]
for i in range(len(aunts)):
	aunt = aunts[i]
	valid = True
	for key in aunt:
		if key in greater:
			if aunt[key] <= match[key]:
				valid = False
				break
		elif key in less:
			if aunt[key] >= match[key]:
				valid = False
				break
		elif aunt[key] != match[key]:
			valid = False
			break
	if valid:
		print(i + 1)