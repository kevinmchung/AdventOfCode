import numpy as np

lines = open("Day12.txt", "r").readlines()

def simulate(moons, velocities, steps):
	for i in range(steps):
		for j in range(len(moons)):
			for k in range(len(moons)):
				for l in range(3):
					if moons[k][l] < moons[j][l]:
						velocities[j][l] -= 1
					elif moons[k][l] > moons[j][l]:
						velocities[j][l] += 1
		for m in range(len(moons)):
			for n in range(3):
				moons[m][n] += velocities[m][n]
	return moons, velocities

def cycle(moons, velocities, i):
	steps = 1
	coords = [moon[i] for moon in moons]
	initial_coords = coords.copy()
	vels = [velocity[i] for velocity in velocities]
	while True:
		for i in range(len(coords)):
			for j in range(len(coords)):
				if coords[j] < coords[i]:
					vels[i] -= 1
				elif coords[j] > coords[i]:
					vels[i] += 1
		for i in range(len(coords)):
			coords[i] += vels[i]
		steps += 1
		if coords == initial_coords:
			return steps

moons = []
velocities = []
for line in lines:
	line = line.strip()[1:-1]
	coords = line.split(", ")
	moon = [int(coord[2:]) for coord in coords]
	moons.append(moon)
	velocities.append([0, 0, 0])

cycles = []
for i in range(3):
	cycles.append(cycle(moons, velocities, i))

print(np.lcm.reduce(cycles))

# total = 0
# for i in range(len(moons)):
# 	kinetic = 0
# 	potential = 0
# 	for j in range(3):
# 		kinetic += abs(velocities[i][j])
# 		potential += abs(moons[i][j])
# 	total += kinetic * potential
#
# print(total)