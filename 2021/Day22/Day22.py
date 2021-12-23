from collections import defaultdict

def area(bounds):
	toret = 1
	for i in range(3):
		toret *= bounds[i][1] - bounds[i][0] + 1
	return toret

def overlap(bounds, other):
	o = []
	for i in range(3):
		if bounds[i][0] > other[i][1] or bounds[i][1] < other[i][0]:
			return None
		t = sorted([*bounds[i], *other[i]])
		tl, th = t[1], t[2]
		if bounds[i][0] <= tl <= th <= bounds[i][1] and other[i][0] <= tl <= th <= other[i][1]:
			o.append((tl, th))
		else:
			return None
	return o

class Cube:
	def __init__(self, bounds):
		self.bounds = bounds
		self.rem = []

	def remove(self, bounds):
		ol = overlap(self.bounds, bounds)
		if ol is None:
			return
		for r in self.rem:
			r.remove(ol)
		self.rem.append(Cube(ol))

	def count(self):
		return area(self.bounds) - sum(r.count() for r in self.rem)


cubes = []
lines = [line.strip() for line in open("Day22.txt")]
for i in range(len(lines)):
	line = lines[i]
	line = line.split(" ")
	c = line[1].split(",")
	v = ("off", "on").index(line[0])
	xl, xh = map(int, c[0][2:].split(".."))
	yl, yh = map(int, c[1][2:].split(".."))
	zl, zh = map(int, c[2][2:].split(".."))
	b = ((xl, xh), (yl, yh), (zl, zh))
	nc = Cube(b)
	for oc in cubes:
		oc.remove(b)
	if v:
		cubes.append(nc)

print(sum(c.count() for c in cubes))