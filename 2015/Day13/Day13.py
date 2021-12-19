import itertools

data = open("Day13.txt", "r").readlines()

names = ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"]
hap_change = {name1:{name2:0 for name2 in names} for name1 in names}

for line in data:
	line = line.strip(".\n").split(" ")
	change = int(line[3]) * (-1 if line[2] == "lose" else 1)
	name1 = line[0]
	name2 = line[-1]
	hap_change[name1][name2] += change
	hap_change[name2][name1] += change

# PART 1
# perms = itertools.permutations(names)
# max_change = 0
# for perm in perms:
# 	cur_change = 0
# 	for i in range(len(perm)):
# 		cur_change += hap_change[perm[i]][perm[(i + 1) % len(perm)]]
# 	if cur_change > max_change:
# 		max_change = cur_change
#
# print(max_change)

# PART 2
names.append("Me")
perms = itertools.permutations(names)
max_change = 0
for perm in perms:
	cur_change = 0
	for i in range(len(perm)):
		if not (perm[i] == "Me" or perm[(i + 1) % len(perm)] == "Me"):
			cur_change += hap_change[perm[i]][perm[(i + 1) % len(perm)]]
	if cur_change > max_change:
		max_change = cur_change

print(max_change)