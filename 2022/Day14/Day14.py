import re
from collections import defaultdict

lines = open("Day14.txt", "r").read().split("\n")

grid = defaultdict(lambda: ".")

highest = 0

i = 0
while i < len(lines):
    line = lines[i].split(" -> ")
    for j in range(1, len(line)):
        x1, y1 = map(int, line[j - 1].split(","))
        x2, y2 = map(int, line[j].split(","))
        cx, cy = x1, y1
        dx, dy = x2 - x1, y2 - y1
        if dx != 0:
            dx = dx // abs(dx)
        if dy != 0:
            dy = dy // abs(dy)
        while cx != x2 or cy != y2:
            if cy > highest:
                highest = cy
            grid[(cx, cy)] = "#"

            cx += dx
            cy += dy
        grid[(x2, y2)] = "#"
    i += 1

s = 0
cx, cy = 500, 0
while True:
    if cy > highest:
        print(s)
        break
    if grid[(cx, cy + 1)] == ".":
        cy += 1
    elif grid[(cx - 1, cy + 1)] == ".":
        cx -= 1
        cy += 1
    elif grid[(cx + 1, cy + 1)] == ".":
        cx += 1
        cy += 1
    else:
        grid[(cx, cy)] = "o"
        s += 1
        cx, cy = 500, 0

s = 0
cx, cy = 500, 0
while True:
    # print(cx, cy)
    if grid[(cx, cy)] == "o":
        print(s)
        break
    if cy == highest + 1:
        grid[(cx, cy)] = "o"
        s += 1
        cx, cy = 500, 0
        continue
    if grid[(cx, cy + 1)] == ".":
        cy += 1
    elif grid[(cx - 1, cy + 1)] == ".":
        cx -= 1
        cy += 1
    elif grid[(cx + 1, cy + 1)] == ".":
        cx += 1
        cy += 1
    else:
        grid[(cx, cy)] = "o"
        s += 1
        cx, cy = 500, 0

s = 0
for k in grid:
    if grid[k] == "o":
        s += 1
print(s)

for y in range(12):
    for x in range(480, 515):
        print(grid[(x, y)], end="")
    print()