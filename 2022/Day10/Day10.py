# Part 1: 1265
# Part 2: 355

import re
from collections import defaultdict

lines = open("Day10.txt", "r").read().split("\n")

ans = 0
x = 1

check = [20, 60, 100, 140, 180, 220]

grid = ["." for j in range(240)]

c = 1
i = 0
while c <= 240:
    line = lines[i].split(" ")
    if c in check:
        ans += c * x
    if abs(((c - 1) % 40) - x) <= 1:
        grid[c] = "#"
    if line[0] == "addx":
        c += 1
        if c in check:
            ans += c * x
        if abs(((c - 1) % 40) - x) <= 1:
            grid[c] = "#"
    c += 1
    if line[0] == "addx":
        x += int(line[1])
    i += 1

print(ans)
for i in range(6):
    print("".join(grid[i * 40:(i+1) * 40]))
