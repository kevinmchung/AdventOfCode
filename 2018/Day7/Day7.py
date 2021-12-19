import re
from collections import defaultdict

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

data = open("Day7.txt", "r").read().split("\n")
reqs = defaultdict(set)

for line in data:
	f, b = re.match("Step ([A-Z]) must be finished before step ([A-Z]) can begin.", line).groups()
	reqs[b].add(f)

done = set()
order = ""
while done != set(alpha):
	allowed = []
	for k in alpha:
		if k not in done and reqs[k].issubset(done):
			allowed.append(k)
	cur = min(allowed)
	done.add(cur)
	order += cur

print(order)

workers = [["", 0] for i in range(5)]
done = set()
i = 0
while done != set(alpha):

	for w in range(len(workers)):
		if workers[w][0] != "":
			if workers[w][1] == 60 + alpha.index(workers[w][0]):
				done.add(workers[w][0])
				workers[w] = ["", 0]
			else:
				workers[w][1] += 1

	allowed = []
	for k in alpha:
		if k not in done and all(w[0] != k for w in workers) and reqs[k].issubset(done):
			allowed.append(k)
	allowed = sorted(allowed)

	for w in range(len(workers)):
		if workers[w][0] == "":
			if len(allowed) > 0:
				workers[w][0] = allowed.pop(0)
	i += 1

print(i - 1)