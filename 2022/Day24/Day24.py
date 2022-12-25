# Part 1: 153
# Part 2: 277

import re
from collections import defaultdict
import numpy as np

lines = open('Day24.txt', 'r').read().split('\n')

blizzards = set()

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]
bdirs = "^v<>"

ans = 0
i = 1
while i < len(lines) - 1:
    line = lines[i][1:-1]
    for x in range(len(line)):
        if line[x] != '.':
            blizzards.add(((x, i - 1), bdirs.index(line[x])))
    i += 1

def move_blizzards(blizzards):
    global w, h
    new_blizzards = set()
    for bpos, di in blizzards:
        x, y = bpos
        new_blizzards.add((((x + dirs[di][0]) % w, (y + dirs[di][1]) % h), di))
    return new_blizzards

bs = [blizzards]

w = 150
h = 20

# w = 6
# h = 4

start = (0, -1)
goal = (w - 1, h)

def search(start, goal, icost):
    global bs
    q = [(icost, start)]
    visited = {(start, icost % (w * h))}
    while q:
        cost, pos = q.pop(0)
        if pos == goal:
            return cost
        cost += 1
        while cost >= len(bs):
            bs.append(move_blizzards(bs[-1]))
            # print(bs)
        b = set(s[0] for s in bs[cost])
        # print(b)
        # print(cost)
        for dx, dy in dirs:
            nx, ny = pos[0] + dx, pos[1] + dy
            if (0 <= nx < w and 0 <= ny < h) or (nx, ny) == goal or (dx == 0 and dy == 0 and (nx, ny) == start):
                if (nx, ny) not in b and ((nx, ny), cost % (w * h)) not in visited:
                    q.append((cost, (nx, ny)))
                    visited.add(((nx, ny), cost % (w * h)))

# a = search(start, goal, 0)
# print(a)
# b = search(goal, start, a)
# print(b)
c = search(start, goal, 636)
print(c)

# for i in range(10):
#     print(i)
#     b = bs[i]
#     d = {s[0]:s[1] for s in b}
#     for y in range(h):
#         for x in range(w):
#             if (x, y) in d:
#                 print(bdirs[d[(x, y)]], end='')
#             else:
#                 print('.', end='')
#         print()
#     print()

print(ans)