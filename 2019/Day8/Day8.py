import numpy as np
lines = open("Day8.txt", "r").readline().strip()

layers = 0
width = 25
height = 6
image = []

for i in range(len(lines) // (25 * 6)):
	image.append(lines[i * 25 * 6 : (i + 1) * 25 * 6])

for y in range(height):
	for x in range(width):
		i = 0
		while image[i][y * width + x] == "2":
			i += 1
		print(image[i][y * width + x],end="")
	print()