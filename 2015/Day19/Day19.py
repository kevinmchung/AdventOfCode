import re
from collections import defaultdict

data = open("Day19.txt", "r").read().split("\n")
seq = data.pop(-1)

replacements = defaultdict(lambda: [])
for line in data:
	if len(line) > 0:
		line = line.split(" => ")
		replacements[line[0]].append(line[1])

# PART 1
# molecules = set()
# for r in replacements:
# 	i = 0
# 	while True:
# 		i = seq.find(r, i)
# 		if i == -1:
# 			break
# 		for replacement in replacements[r]:
# 			new_seq = seq[:i] + replacement + seq[i + len(r):]
# 			molecules.add(new_seq)
# 		i += len(r)

# PART 2
reverse_replacements = {}
for r in replacements:
	for replacement in replacements[r]:
		reverse_replacements[replacement[::-1]] = r[::-1]

seq = seq[::-1]
count = 0
while seq != 'e':
	seq = re.sub('|'.join(reverse_replacements.keys()), lambda r: reverse_replacements[r.group()], seq, 1)
	print(seq)
	count += 1

print(count)