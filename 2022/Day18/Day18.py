# Part 1: 115
# Part 2: 1612

import re
from collections import defaultdict

lines = open("Day18.txt", "r").read().split("\n")

cubes = set()
i = 0
l = [1000, 1000, 1000]
h = [0, 0, 0]
while i < len(lines):
    line = tuple(map(int, lines[i].split(",")))
    cubes.add(line)
    for j in range(3):
        if l[j] > line[j]:
            l[j] = line[j]
        if h[j] < line[j]:
            h[j] = line[j]
    i += 1

ans = 0
for x, y, z in cubes:
    for dx in (-1, 1):
        if (x + dx, y, z) not in cubes:
            ans += 1
    for dy in (-1, 1):
        if (x, y + dy, z) not in cubes:
            ans += 1
    for dz in (-1, 1):
        if (x, y, z + dz) not in cubes:
            ans += 1
print(ans)

trap = {}
def trapped(point):
    if point in trap:
        return trap[point]
    visited = set()
    q = [point]
    visited.add(point)
    while q:
        x, y, z = q.pop(0)
        for dx, dy, dz in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            np = (x + dx, y + dy, z + dz)
            if any(np[i] < l[i] or np[i] > h[i] for i in range(3)):
                for p in visited:
                    trap[p] = False
                return False
            if np not in visited and np not in cubes:
                visited.add(np)
                q.append(np)
    for p in visited:
        trap[p] = True
    return True

ans = 0
for x, y, z in cubes:
    for dx in (-1, 1):
        if (x + dx, y, z) not in cubes and not trapped((x + dx, y, z)):
            ans += 1
    for dy in (-1, 1):
        if (x, y + dy, z) not in cubes and not trapped((x, y + dy, z)):
            ans += 1
    for dz in (-1, 1):
        if (x, y, z + dz) not in cubes and not trapped((x, y, z + dz)):
            ans += 1

print(ans)