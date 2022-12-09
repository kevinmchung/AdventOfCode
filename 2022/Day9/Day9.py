# Part 1: 386
# Part 2: 181

import re
from collections import defaultdict

lines = open("Day9.txt", "r").read().split("\n")

ans = 0


visited = set()
hx, hy = 0, 0
tx, ty = 0, 0
visited.add((tx, ty))

dirs = {"R": (1, 0), "D": (0, -1), "L": (-1, 0), "U": (0, 1)}
knots = [[0, 0] for _ in range(10)]
visited2 = set()
visited2.add((0, 0))

for i in range(0, len(lines), 1):
    line = lines[i].split(" ")
    d, n = line
    n = int(n)
    dx, dy = dirs[d]
    for j in range(n):
        hx += dx
        hy += dy
        sx = hx - tx
        sy = hy - ty
        if abs(sx) > 1 or abs(sy) > 1:
            if sx != 0:
                sx = sx // abs(sx)
            if sy != 0:
                sy = sy // abs(sy)
            tx += sx
            ty += sy
        visited.add((tx, ty))

        knots[0][0] += dx
        knots[0][1] += dy
        for k in range(1, 10):
            sx = knots[k-1][0] - knots[k][0]
            sy = knots[k-1][1] - knots[k][1]
            if abs(sx) > 1 or abs(sy) > 1:
                if sx != 0:
                    sx = sx // abs(sx)
                if sy != 0:
                    sy = sy // abs(sy)
                knots[k][0] += sx
                knots[k][1] += sy
        visited2.add(tuple(knots[-1]))
    # print(visited)

print(len(visited))
print(len(visited2))