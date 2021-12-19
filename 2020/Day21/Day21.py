# Part 1: 92
# Part 2: 37

from collections import defaultdict

data = open("Day21.txt", "r").read().split("\n")
# data = list(map(int, data))

items = []
ings = defaultdict(lambda: 0)
allergens = set()

for line in data:
	line = line.split(" (contains ")
	ingredients = line[0].split(" ")
	allgs = line[1][:-1].split(", ")
	items.append((ingredients, allgs))
	for i in ingredients:
		ings[i] += 1
	for a in allgs:
		allergens.add(a)

contains = defaultdict(lambda: [])
for a in allergens:
	for item in items:
		if a in item[1]:
			contains[a].append(item)

possible = {}
for a in allergens:
	foods = []
	for food in contains[a]:
		foods.append(set(food[0]))
	possible[a] = set.intersection(*foods)
	print(a)
	print(possible[a])


actual = {"dairy":"dhfng",
		  "wheat":"znrzgs",
		  "shellfish":"nqbnmzx",
		  "soy":"ntggc",
		  "fish":"xhkdc",
		  "sesame":"dstct",
		  "eggs":"pgblcd",
		  "peanuts":"ghlzj"}

allergs = []
for a in allergens:
	allergs.append(possible[a])
allergs = set.union(*allergs)

print(sum(ings.values()) - sum(ings[a] for a in allergs))

for k in sorted(actual.keys()):
	print(actual[k], end=",")