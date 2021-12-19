lx, hx, ly, hy = 81, 129, -150, -108

highest = 0
ans = 0
for a in range(130):
	for b in range(-151, 1000):
		vx = a
		vy = b
		cur = 0
		x, y = 0, 0
		while x <= hx and y >= ly:
			x += vx
			y += vy
			if vx != 0:
				vx -= vx / abs(vx)
			vy -= 1
			if y > cur:
				cur = y
			if lx <= x <= hx and ly <= y <= hy:
				ans += 1
				if cur > highest:
					highest = cur
				break

print(highest)
print(ans)