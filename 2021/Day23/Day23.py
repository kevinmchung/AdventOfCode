from collections import defaultdict

def path(g, sr, sc, er, ec):
	q = [(sr, sc, 0)]
	visited = {(sr, sc)}
	while q:
		cr, cc, l = q.pop(0)
		if cr == er and cc == ec:
			return l
		for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			nr = cr + dr
			nc = cc + dc
			if g[nr][nc] == "." and (nr, nc) not in visited:
				visited.add((nr, nc))
				q.append((nr, nc, l + 1))

bot = 5
hcols = {"A": 3, "B": 5, "C":7, "D":9}
hallspots = ((1, 1), (1, 2), (1, 4), (1, 6), (1, 8), (1, 10), (1, 11))
get_cost = lambda c:pow(10, "ABCD".index(c))

def moves(g):
	ret = []
	for r in range(len(g)):
		for c in range(len(g[r])):
			if g[r][c].isalpha():
				hcol = hcols[g[r][c]]
				done = False
				if c == hcol:
					done = all(g[i][hcol] == g[r][c] for i in range(r + 1, bot + 1))
				if r == 1:
					good = True
					i = bot
					while good and i >= 2:
						if g[i][hcol] == ".":
							break
						if g[i][hcol] != g[r][c]:
							good = False
						i -= 1
					if good:
						p = path(g, r, c, i, hcol)
						if p is not None:
							ret.append((r, c, i, hcol, p * get_cost(g[r][c])))
				elif g[r - 1][c] == "." and not done:
					for sr, sc in hallspots:
						p = path(g, r, c, sr, sc)
						if p is not None:
							ret.append((r, c, sr, sc, p * get_cost(g[r][c])))

					good = True
					i = bot
					while good and i >= 2:
						if g[i][hcol] == ".":
							break
						if g[i][hcol] != g[r][c]:
							good = False
						i -= 1
					if good:
						p = path(g, r, c, i, hcol)
						if p is not None:
							ret.append((r, c, i, hcol, p * get_cost(g[r][c])))
	return ret

def finished(g):
	tot = 0
	for c in "ABCD":
		for i in range(bot, 1, -1):
			if g[i][hcols[c]] == c:
				tot += 1
			else:
				break
	return tot

grid = [list(line.replace("\n", "")) + [" "] * (14 - len(line)) for line in open("Day23.txt")]
grid = tuple(map(tuple, grid))

q = [(grid, finished(grid), 0)]
visited = {grid: 0}
while q:
	q = sorted(q, key=lambda f:(f[2]))
	cur, f, cost = q.pop(0)
	if f >= 4:
		print(f)
		print("\n".join("".join(row) for row in cur))
		print(cost)
	if f == 16:
		print(cost)
		break
	m = moves(cur)
	for sr, sc, er, ec, dcost in m:
		ngrid = list(map(list, cur))
		ngrid[er][ec] = ngrid[sr][sc]
		ngrid[sr][sc] = "."
		ngrid = tuple(map(tuple, ngrid))
		if ngrid not in visited or (ngrid in visited and cost + dcost < visited[ngrid]):
			q.append((ngrid, finished(ngrid), cost + dcost))
			visited[ngrid] = cost + dcost
