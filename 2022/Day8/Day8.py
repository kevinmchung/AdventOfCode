# Part 1: 666
# Part 2: 396

import re
from collections import defaultdict

lines = open("Day8.txt", "r").read().split("\n")
lines = [list(map(int, row)) for row in lines]
ans = 0
highest = 0

for r in range(len(lines)):
    for c in range(len(lines[0])):
        h = lines[r][c]
        if all(lines[dr][c] < lines[r][c] for dr in range(r)) or \
            all(lines[dr][c] < lines[r][c] for dr in range(r + 1, len(lines))) or \
            all(lines[r][dc] < lines[r][c] for dc in range(c)) or \
            all(lines[r][dc] < lines[r][c] for dc in range(c + 1, len(lines[0]))):
            ans += 1
        
        s = 1
        for dr in range(r - 1, -1, -1):
            if lines[dr][c] >= lines[r][c] or dr == 0:
                s *= r - dr
                break
        for dr in range(r + 1, len(lines)) :
            if lines[dr][c] >= lines[r][c] or dr == len(lines) - 1:
                s *= dr - r
                break
        for dc in range(c - 1, -1, -1):
            if lines[r][dc] >= lines[r][c] or dc == 0:
                s *= c - dc
                break
        for dc in range(c + 1, len(lines[0])):
            if lines[r][dc] >= lines[r][c] or dc == len(lines[0]) - 1:
                s *= dc - c
                break
        if s > highest:
            highest = s

print(ans)
print(highest)