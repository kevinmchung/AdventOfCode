data = open("Day8.txt", "r").readlines()

total = 0
for line in data:
	line = line.strip()

	# PART 1
	# total += len(line) - len(eval("str(" + line + ")"))

	# PART 2
	total += line.count("\"") + line.count("\\") + 2

print(total)