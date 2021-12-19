from collections import defaultdict

lines = [line.strip() for line in open("Day14.txt", "r")]
# lines = list(map(int, lines))

poly = lines[0]

ts = {}

for i in range(2, len(lines)):
	line = lines[i]
	line = line.split(" -> ")
	ts[line[0]] = line[1]

pairs = defaultdict(int)
for i in range(len(poly) - 1):
	pairs[poly[i:i+2]] += 1

for _ in range(40):
	newpairs = defaultdict(int)
	for k in ts:
		newpairs[k[0] + ts[k]] += pairs[k]
		newpairs[ts[k] + k[1]] += pairs[k]
	pairs = newpairs

counts = defaultdict(int)
for p in pairs:
	counts[p[0]] += pairs[p]
	counts[p[1]] += pairs[p]

counts[poly[0]] += 1
counts[poly[-1]] += 1
print(max(counts.values()) // 2 - min(counts.values()) // 2)