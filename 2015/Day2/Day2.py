data = open("Day2.txt", "r").readlines()

total = 0
for line in data:
	dims = list(map(int, line.split("x")))

	# PART 1
	# sides = [dims[0] * dims[1], dims[1] * dims[2], dims[2] * dims[0]]
	# total += 2 * sum(sides) + min(sides)

	total += 2 * sum(dims) - 2 * max(dims) + dims[0] * dims[1] * dims[2]

print(total)