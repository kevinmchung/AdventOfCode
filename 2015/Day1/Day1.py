inp = open("Day1.txt", "r").readline()

# PART 1
# print(inp.count("(") - inp.count(")"))

# PART 2
floor = 0
for i in range(len(inp)):
	if inp[i] == "(":
		floor += 1
	else:
		floor -= 1
	if floor < 0:
		print(i + 1)
		break