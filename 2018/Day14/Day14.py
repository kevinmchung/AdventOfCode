inp = "598701"
recipes = "37"
i, j = 0, 1

while inp not in recipes[-7:]:
	recipes += str(int(recipes[i]) + int(recipes[j]))
	i = (i + int(recipes[i]) + 1) % len(recipes)
	j = (j + int(recipes[j]) + 1) % len(recipes)

print(recipes[int(inp):int(inp) + 10])
print(recipes.index(inp))