from collections import defaultdict

lines = [line.strip() for line in open("Day13.txt", "r")]

dots = []
folds = []

for i in range(len(lines)):
	line = lines[i]
	if len(line) > 0:
		if "fold" in line:
			folds.append(line[11:].split("="))
		else:
			dots.append(tuple(map(int, line.split(","))))

for fold in folds:
	for i in range(len(dots)):
		if fold[0] == "x":
			if dots[i][0] > int(fold[1]):
				dots[i] = (int(fold[1]) - (dots[i][0] - int(fold[1])), dots[i][1])
		else:
			if dots[i][1] > int(fold[1]):
				dots[i] = (dots[i][0], int(fold[1]) - (dots[i][1] - int(fold[1])))

for y in range(max(dot[1] for dot in dots) + 1):
	for x in range(max(dot[0] for dot in dots) + 1):
		if (x, y) in dots:
			print("#", end="")
		else:
			print(".", end="")
	print()