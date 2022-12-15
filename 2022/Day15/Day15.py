# Part 1: 1745
# Part 2: 1007

import re
from collections import defaultdict

lines = open("Day15.txt", "r").read().split("\n")

ans = 0

sensors = []
beacons = set()
dists = []

def m(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

i = 0
while i < len(lines):
    line = lines[i]
    g = re.findall(r"(-?\d+)", line)
    sx, sy, bx, by = map(int, g)
    sensors.append((sx, sy))
    beacons.add((bx, by))
    dists.append(m((sx, sy), (bx, by)))
    i += 1

ranges = []

y = 2000000

for i, (sx, sy) in enumerate(sensors):
    d = dists[i] - abs(sy - y)
    if d >= 0:
        ranges.append((sx - d, sx + d))

i = 0
while i < len(ranges):
    overlap = False
    j = i + 1
    while j < len(ranges):
        r1, r2 = ranges[i], ranges[j]
        if r1[0] <= r2[1] and r2[0] <= r1[1]:
            ranges[i] = (min(r1[0], r2[0]), max(r1[1], r2[1]))
            ranges.pop(j)
            overlap = True
        else:
            j += 1
    if not overlap:
        i += 1
    

for r in ranges:
    ans += r[1] - r[0] + 1
    for b in beacons:
        if r[0] <= b[0] <= r[1] and b[1] == y:
            ans -= 1
print(ans)

print(2557297*4000000+3267339)

b = 4000000

y = 0
while y < b + 1:
    ranges = []

    for i, (sx, sy) in enumerate(sensors):
        d = dists[i] - abs(sy - y)
        if d >= 0:
            l = sx - d
            h = sx + d
            if l < 0:
                l = 0
            if h > b:
                h = b
            ranges.append((l, h))

    if any(r == (0, b) for r in ranges):
        y += 1
        continue

    i = 0
    while i < len(ranges):
        overlap = False
        j = i + 1
        while j < len(ranges):
            r1, r2 = ranges[i], ranges[j]
            if r1[0] <= r2[1] and r2[0] <= r1[1]:
                ranges[i] = (min(r1[0], r2[0]), max(r1[1], r2[1]))
                ranges.pop(j)
                overlap = True
            else:
                j += 1
        if not overlap:
            i += 1

    if len(ranges) > 1:
        print(ranges, y)
    
    y += 1
