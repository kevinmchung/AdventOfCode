import itertools

floors = (("thg", "thm", "plg", "stg", "elg", "elm", "dig", "dim"), ("plm", "stm"), ("prg", "prm", "rug", "rum"), ())
# floors = (("hym", "lim"), ("hyg",), ("lig",), ())

floors = tuple(map(lambda f:tuple(sorted(f)), floors))

def check_floor(floor):
	generators = [item for item in floor if item[2] == "g"]
	if len(generators) > 0:
		for item in floor:
			if item[2] == "m" and not (item[:2] + "g") in generators:
				return False
	return True

dirs = (-1, 1)
def get_legal_moves(elev, floors):
	cur_floor = floors[elev]
	c1 = list(itertools.combinations(cur_floor, 1))
	c2 = list(itertools.combinations(cur_floor, 2))
	to_test = []
	if 0 <= elev - 1 < 4:
		if len(c1) > 0:
			for c in c1:
				to_test.append((-1, c))
		else:
			for c in c2:
				to_test.append((-1, c))
	if 0 <= elev + 1 < 4:
		if len(c2) > 0:
			for c in c2:
				to_test.append((1, c))
		else:
			for c in c1:
				to_test.append((1, c))

	moves = []
	for m in to_test:
		d, items = m
		if len(items) == 2:
			items = sorted(items, key=lambda i: i[2])
			if items[1][2] == "m" and items[0][2] == "g":
				if items[0][:2] != items[1][:2]:
					continue
		old_floor = [i for i in cur_floor]
		new_floor = [i for i in floors[elev + d]]
		for item in items:
			old_floor.remove(item)
			new_floor.append(item)
		if check_floor(old_floor) and check_floor(new_floor):
			moves.append(m)
	return moves


def generalize(floors):
	seen = {}
	idx = 0
	out = [[], [], [], []]
	for f in range(4):
		for item in floors[f]:
			if item[:2] not in seen:
				seen[item[:2]] = idx
				idx += 1
			out[f].append(item[2] + str(seen[item[:2]]))
	return tuple(map(lambda f: tuple(sorted(f)), out))


q = [(0, 0, floors)]
visited = {(0, generalize(floors))}
while len(q) > 0:
	q = sorted(q)
	n, elev, cur = q.pop(0)
	print(n, elev, cur)
	if all(len(cur[i]) == 0 for i in range(3)):
		print(n)
		break
	moves = get_legal_moves(elev, cur)
	for move in moves:
		d, items = move
		new_floors = [[i for i in floor] for floor in cur]
		for item in items:
			new_floors[elev].remove(item)
			new_floors[elev + d].append(item)
		new_floors = tuple(map(lambda f: tuple(sorted(f)), new_floors))
		c = (elev + d, generalize(new_floors))
		if c not in visited:
			q.append((n + 1, elev + d, new_floors))
			visited.add(c)


