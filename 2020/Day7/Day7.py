# Part 1: 190
# Part 2: 212

data = open("Day7.txt", "r").read()
data = data.split("\n")
# data = list(map(int, data))

tree = {}
reverse_tree = {}
total = 0

for line in data:
	line = line.strip()
	if not "no other bags" in line:
		line_list = line.split(" ")
		key = line_list[0] + " " + line_list[1]
		vals = line[line.find("contain ") + len("contain "):].split(", ")
		tree[key] = []
		for item in vals:
			item = item.split(" ")
			bag = item[1] + " " + item[2]
			tree[key].append((bag, int(item[0])))
			if bag in reverse_tree:
				reverse_tree[bag].append(key)
			else:
				reverse_tree[bag] = [key]

def num_bags(cur):
	if cur[0] in tree:
		total = 0
		for bag in tree[cur[0]]:
			total += num_bags(bag)
		return total * cur[1] + cur[1]
	else:
		return cur[1]

print(num_bags(("shiny gold", 1)))

q = [("shiny gold", 0)]
visited = {("shiny gold", 0)}
while len(q) > 0:
	cur = q.pop(0)
	visited.add(cur)
	if cur[0] in reverse_tree:
		for bag in reverse_tree[cur[0]]:
			q.append(bag)

print(len(visited))
