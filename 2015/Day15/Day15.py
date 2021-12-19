import numpy as np

data = open("Day15.txt", "r").readlines()
ingredients = []

for line in data:
	line = line.replace(",","").strip().split(" ")
	ingredients.append(np.array(list(map(int, [line[2], line[4], line[6], line[8], line[10]]))))

ingredients = np.array(ingredients)

max_score = 0
for a in range(1, 100):
	for b in range(1, 100):
		for c in range(1, 100):
			d = 100 - a - b - c
			if d > 0:
				nums = np.array([a, b, c, d])
				vals = np.matmul(nums, ingredients)
				vals[vals < 0] = 0
				score = np.prod(vals[:4])
				if score > max_score and vals[4] == 500:
					max_score = score
print(max_score)