lines = [line.strip() for line in open("Day2.txt", "r").readlines()]
# lines = list(map(int, lines))

x = 0
y = 0
a = 0
for i in range(len(lines)):
	line = lines[i]
	line = line.split(" ")
	n = int(line[1])
	if line[0][0] == "f":
		x += n
		y += a * n
	elif line[0][0] == "d":
		a += n
	elif line[0][0] == "u":
		a -= n
print(x * y)