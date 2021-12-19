lines = [list(map(int, line.strip())) for line in open("Day15.txt", "r")]

def get_grid_val(r, c, lines):
	val = lines[r % len(lines)][c % len(lines)] + r // len(lines) + c // len(lines)
	while val > 9:
		val -= 9
	return val

q = [(0, 0, 0)]
visited = {(0, 0)}
while len(q):
	q = sorted(q, key=lambda f:f[2])
	r, c, n = q.pop(0)
	if r >= len(lines) * 5 - 1 and c >= len(lines) * 5 - 1:
		print(n)
		break
	else:
		for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
			if 0 <= rr < len(lines) * 5 and 0 <= cc < len(lines) * 5 and (rr, cc) not in visited:
				q.append((rr, cc, n + get_grid_val(rr, cc, lines)))
				visited.add((rr, cc))