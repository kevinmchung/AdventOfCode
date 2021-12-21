from collections import defaultdict

p = [5, 0]
s = [0, 0]

d = 1
i = 0
t = 0
while s[0] < 1000 and s[1] < 1000:
	m = d + d + 1 + d + 2
	p[t] = (p[t] + m) % 10
	s[t] += p[t] + 1
	d += 3
	i += 3
	t = (t + 1) % 2

print(min(s) * i)

p = [5, 0]
s = [0, 0]

poss = defaultdict(int)
for a in range(1, 4):
	for b in range(1, 4):
		for c in range(1, 4):
			poss[a + b + c] += 1

unis = {}
def a(p, s, t):
	if s[0] >= 21:
		return [1, 0]
	if s[1] >= 21:
		return [0, 1]
	if (*p, *s, t) in unis:
		return unis[(*p, *s, t)]
	else:
		o = [0, 0]
		for k in poss:
			np = [p[0], p[1]]
			np[t] = (np[t] + k) % 10
			ns = [s[0], s[1]]
			ns[t] += np[t] + 1
			nexta = a(np, ns, (t + 1) % 2)
			o[0] += poss[k] * nexta[0]
			o[1] += poss[k] * nexta[1]
		unis[(*p, *s, t)] = o
		return o


print(max(a(p, s, 0)))
# print(unis)