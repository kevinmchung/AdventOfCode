data = open("Day8.txt", "r").read().split(" ")
data = list(map(int, data))

class Node:
	def __init__(self, children, metadata):
		self.metadata = metadata
		self.children = children

	def add_child(self, child):
		self.children.append(child)

	def value(self):
		if len(self.children) > 0:
			out = 0
			for m in self.metadata:
				if m <= len(self.children) and m != 0:
					out += self.children[m - 1].value()
			return out
		else:
			return sum(self.metadata)

	def __str__(self):
		return "{} - {}".format(len(self.children), str(self.metadata))

def get_node(inp):
	num_children = inp.pop(0)
	num_meta = inp.pop(0)
	children = []
	metadata = []
	if num_children > 0:
		for i in range(num_children):
			children.append(get_node(inp))
	for i in range(num_meta):
		metadata.append(inp.pop(0))
	return Node(children, metadata)

root = get_node(data)

total = 0
q = [root]
while len(q) > 0:
	cur = q.pop(0)
	total += sum(cur.metadata)
	for c in cur.children:
		q.append(c)
print(total)

print(root.value())