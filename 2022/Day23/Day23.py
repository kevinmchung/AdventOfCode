# Part 1: 448
# Part 2: 339

import re
from collections import defaultdict
import numpy as np

lines = open("Day23.txt", "r").read().split("\n")

elves = set()

ans = 0
i = 0
while i < len(lines):
    line = lines[i]
    for c in range(len(line)):
        if line[c] == "#":
            elves.add((c, i))
    i += 1

d = 0
round = 1
while True:
    moves = {}
    seen = set()
    stop = set()
    
    # for y in range(-5, 15):
    #     for x in range(-5, 15):
    #         if (x, y) in elves:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
    # print()

    for pos in elves:
        x, y = pos
        valid = False
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if not (dx == 0 and dy == 0):
                    if (x + dx, y + dy) in elves:
                        valid = True
        
        if not valid:
            stop.add((x, y))
            continue

        crit = [all((x + dx, y - 1) not in elves for dx in [-1, 0, 1]),
                all((x + dx, y + 1) not in elves for dx in [-1, 0, 1]),
                all((x - 1, y + dy) not in elves for dy in [-1, 0, 1]),
                all((x + 1, y + dy) not in elves for dy in [-1, 0, 1])]
        pos_move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        c = d
        cycle = False
        while not crit[c]:
            c = (c + 1) % 4
            if c == d:
                cycle = True
                break
        if cycle:
            stop.add((x, y))
            continue
        
        nx, ny = x + pos_move[c][0], y + pos_move[c][1]
        if (nx, ny) in seen:
            stop.add((nx, ny))
        else:
            moves[pos] = (nx, ny)
            seen.add((nx, ny))
    
    new_elves = set()
    for key in elves:
        x, y = key
        if key in moves:
            nx, ny = moves[key]
            if (nx, ny) not in stop:
                new_elves.add((nx, ny))
            else:
                new_elves.add(key)
        else:
            new_elves.add(key)
    if elves == new_elves:
        print(round)
        break
    elves = new_elves
    d = (d + 1) % 4
    round += 1
    

dims = [1000, 0, 1000, 0]
for key in elves:
    x, y = key
    dims[0] = min(dims[0], x)
    dims[1] = max(dims[1], x)
    dims[2] = min(dims[2], y)
    dims[3] = max(dims[3], y)

print((dims[3] - dims[2] + 1) * (dims[1] - dims[0] + 1) - len(elves))

print(ans)