import re

data = open("Day10.txt", "r").read().split("\n")
guess = 10580

stars = []
for line in data:
	x, y, vx, vy = map(int, re.match("position=<([- ]\d+), ([- ]\d+)> velocity=<([- ]\d+), ([- ]\d+)>", line).groups())
	stars.append(((x, y), (vx, vy)))


for t in range(guess - 50, guess + 50):
	lights = set()
	for star in stars:
		lights.add((star[0][0] + t * star[1][0], star[0][1] + t * star[1][1]))
	x_min = min(l[0] for l in lights)
	x_max = max(l[0] for l in lights)
	y_min = min(l[1] for l in lights)
	y_max = max(l[1] for l in lights)
	print(t, x_min, x_max, y_min, y_max)
	for y in range(y_min, y_max + 1):
		for x in range(x_min, x_max + 1):
			if (x, y) in lights:
				print("#", end="")
			else:
				print(".", end="")
		print()
	print("---------")
