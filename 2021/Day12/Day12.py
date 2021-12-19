from collections import defaultdict

lines = [line.strip() for line in open("Day12.txt", "r")]
# lines = list(map(int, lines))
cs = [line.split("-") for line in lines]

graph = defaultdict(list)
for a, b in cs:
	graph[a].append(b)
	graph[b].append(a)

q = [("start",)]
ans = 0
while len(q):
	cur = q.pop(0)
	if cur[-1] == "end":
		ans += 1
	else:
		for c in graph[cur[-1]]:
			v = any(cur.count(n) == 2 for n in cur if n.islower())
			if c.islower() and c not in ["start"]:
				if v:
					if c not in cur:
						q.append(cur + (c,))
				else:
					q.append(cur + (c,))
			elif c.isupper():
				q.append(cur + (c,))

print(ans)