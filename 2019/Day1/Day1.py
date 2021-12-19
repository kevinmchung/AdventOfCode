modules = open("Day1.txt", "r").readlines()

total = 0
for module in modules:
	mass = int(module)
	while True:
		mass = mass // 3 - 2
		if mass <= 0:
			break
		total += mass

print(total)