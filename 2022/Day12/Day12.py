# Part 1: 369
# Part 2: 320

import re
from collections import defaultdict

lines = open("Day12.txt", "r").read().split("\n")

a = []
sr, sc = -1, -1
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == "S":
            sr, sc = r, c
        if lines[r][c] == "a":
            a.append((r, c))

pos = (sr, sc)
q = [pos]
visited = set()
cost = {pos: 0}

alpha = "SabcdefghijklmnopqrstuvwxyzE"

while q:
    # print(q)
    r, c = q.pop(0)
    # print(lines[r][c])
    if lines[r][c] == "E":
        print(cost[(r, c)])
        break
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= r + dr < len(lines) and 0 <= c + dc < len(lines[0]):
            # print(lines[nr][nc], lines[r][c])
            if (nr, nc) not in visited and alpha.index(lines[nr][nc]) - alpha.index(lines[r][c]) <= 1:
                q.append((nr, nc))
                visited.add((nr, nc))
                cost[(nr, nc)] = cost[(r, c)] + 1

least = 1000
for sr, sc in a:
    pos = (sr, sc)
    q = [pos]
    visited = set()
    cost = {pos: 0}

    while q:
        # print(q)
        r, c = q.pop(0)
        # print(lines[r][c])
        if lines[r][c] == "E":
            # print(cost[(r, c)])
            if cost[(r, c)] < least:
                least = cost[(r, c)]
            break
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= r + dr < len(lines) and 0 <= c + dc < len(lines[0]):
                # print(lines[nr][nc], lines[r][c])
                if (nr, nc) not in visited and alpha.index(lines[nr][nc]) - alpha.index(lines[r][c]) <= 1:
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    cost[(nr, nc)] = cost[(r, c)] + 1

print(least)