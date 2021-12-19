from copy import deepcopy

def getpaths(s):
	paths = []
	q = [(s, "")]
	while q:
		cur, path = q.pop(0)
		if type(cur) == list:
			for i in [0, 1]:
				q.append((cur[i], path + str(i)))
		else:
			paths.append(path)
	return sorted(paths)

lines = [eval(line.strip()) for line in open("Day18.txt")]
s = lines[0]

for line in lines[1:]:
	s = [s, line]
	while True:
		q = [(s, "")]
		new = deepcopy(s)
		paths = getpaths(s)
		bignums = []
		while q:
			cur, path = q.pop(0)
			if type(cur) == list:
				if len(path) == 4:
					a, b, c, d = map(int, path)
					lp = None
					rp = None
					for p in paths:
						if p[:4] != path:
							if p < path:
								lp = p
							if p > path:
								rp = p
								break
					if lp is not None:
						idxs = "".join(f"[{int(n)}]" for n in lp)
						exec(f"new{idxs} += s[a][b][c][d][0]")
					if rp is not None:
						idxs = "".join(f"[{int(n)}]" for n in rp)
						exec(f"new{idxs} += s[a][b][c][d][1]")
					new[a][b][c][d] = 0
				else:
					for i in [0, 1]:
						q.append((cur[i], path + str(i)))
			else:
				if cur >= 10:
					bignums.append((cur, path))
			if new != s:
				break
		if new == s:
			if len(bignums):
				cur, path = sorted(bignums, key=lambda b:b[1])[0]
				idxs = "".join(f"[{int(n)}]" for n in path)
				exec(f"new{idxs} = [cur // 2, cur - cur // 2]")
			else:
				break
		s = new

def mag(s):
	if type(s) == int:
		return s
	else:
		return mag(s[0]) * 3 + mag(s[1]) * 2

print(s)
print(mag(s))

largest = 0
for x in lines:
	for y in lines:
		if x != y:
			f = [x, y]
			while True:
				q = [(f, "")]
				new = deepcopy(f)
				paths = getpaths(f)
				bignums = []
				while q:
					cur, path = q.pop(0)
					if type(cur) == list:
						if len(path) == 4:
							a, b, c, d = map(int, path)
							lp = None
							rp = None
							for p in paths:
								if p[:4] != path:
									if p < path:
										lp = p
									if p > path:
										rp = p
										break
							if lp is not None:
								idxs = "".join(f"[{int(n)}]" for n in lp)
								exec(f"new{idxs} += f[a][b][c][d][0]")
							if rp is not None:
								idxs = "".join(f"[{int(n)}]" for n in rp)
								exec(f"new{idxs} += f[a][b][c][d][1]")
							new[a][b][c][d] = 0
						else:
							for i in [0, 1]:
								q.append((cur[i], path + str(i)))
					else:
						if cur >= 10:
							bignums.append((cur, path))
					if new != f:
						break
				if new == f:
					if len(bignums):
						cur, path = sorted(bignums, key=lambda b: b[1])[0]
						idxs = "".join(f"[{int(n)}]" for n in path)
						exec(f"new{idxs} = [cur // 2, cur - cur // 2]")
					else:
						break
				f = new
			m = mag(f)
			if m > largest:
				largest = m

print(largest)