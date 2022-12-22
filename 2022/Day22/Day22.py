# Part 1: 80
# Part 2: 192

import re
from collections import defaultdict
import numpy as np

lines = open("/Users/kevin/Documents/code/PycharmProjects/AdventOfCode/2022/Day22/Day22.txt", "r").read().split("\n")

ans = 0

ins = lines[-1]
lines = lines[:-2]

width = max(len(line) for line in lines)
grid = np.zeros((len(lines), width))

for idx, line in enumerate(lines):
    for i in range(width):
        if i >= len(line):
            grid[idx, i:] = -1
        elif line[i] == "#":
            grid[idx, i] = 1
        elif line[i] == " ":
            grid[idx, i] = -1

#  12
#  3
# 54
# 6


f1 = grid[0:50, 50:100]
f2 = grid[0:50, 100:150]
f3 = grid[50:100, 50:100]
f4 = grid[100:150, 50:100]
f5 = grid[100:150, 0:50]
f6 = grid[150:200, 0:50]

faces = [f1, f2, f3, f4, f5, f6]
offset = [(0, 50), (0, 100), (50, 50), (100, 50), (100, 0), (150, 0)]

# RDLU

r = [(1, 0), (3, 2), (1, 3), (1, 2), (3, 0), (3, 3)]
d = [(2, 1), (2, 2), (3, 1), (5, 2), (5, 1), (1, 1)]
l = [(4, 0), (0, 2), (4, 1), (4, 2), (0, 0), (0, 1)]
u = [(5, 0), (5, 3), (0, 3), (2, 3), (2, 0), (4, 3)]
change = [r, d, l, u]

assert(len(u + d + l + r) == len(set(u + d + l + r)))

cr, cc = 0, 0
# for c in range(width):
#     if grid[0, c] == 0:
#         cr, cc = 0, c
#         break

def change_faces(f, di, r, c):
    global faces, dirs
    if f == 0:
        if di == 0:
            return change[di][f][0], change[di][f][1], r, 0
        if di == 1:
            return change[di][f][0], change[di][f][1], 0, c
        if di == 2:
            return change[di][f][0], change[di][f][1], 49 - r, 0
        if di == 3:
            return change[di][f][0], change[di][f][1], c, 0
    if f == 1:
        if di == 0: # right
            return change[di][f][0], change[di][f][1], 49 - r, 49
        if di == 1: # down
            return change[di][f][0], change[di][f][1], c, 49
        if di == 2: # left
            return change[di][f][0], change[di][f][1], r, 49
        if di == 3: # up
            return change[di][f][0], change[di][f][1], 49, c
    if f == 2:
        if di == 0: # right
            return change[di][f][0], change[di][f][1], 49, r
        if di == 1: # down
            return change[di][f][0], change[di][f][1], 0, c
        if di == 2: # left
            return change[di][f][0], change[di][f][1], 0, r
        if di == 3: # up
            return change[di][f][0], change[di][f][1], 49, c
    if f == 3:
        if di == 0: # right
            return change[di][f][0], change[di][f][1], 49 - r, 49
        if di == 1: # down
            return change[di][f][0], change[di][f][1], c, 49
        if di == 2: # left
            return change[di][f][0], change[di][f][1], r, 49
        if di == 3: # up
            return change[di][f][0], change[di][f][1], 49, c
    if f == 4:
        if di == 0: # right
            return change[di][f][0], change[di][f][1], r, 0
        if di == 1: # down
            return change[di][f][0], change[di][f][1], 0, c
        if di == 2: # left
            return change[di][f][0], change[di][f][1], 49 - r, 0
        if di == 3: # up
            return change[di][f][0], change[di][f][1], c, 0
    if f == 5:
        if di == 0: # right
            return change[di][f][0], change[di][f][1], 49, r
        if di == 1: # down
            return change[di][f][0], change[di][f][1], 0, c
        if di == 2: # left
            return change[di][f][0], change[di][f][1], 0, r
        if di == 3: # up
            return change[di][f][0], change[di][f][1], 49, c


f = 0
di = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

i = 0
seen = set()
while i < len(ins):
    if ins[i].isnumeric():
        n = ""
        while i < len(ins) and ins[i].isnumeric():
            n += ins[i]
            i += 1
        n = int(n)
        for j in range(n):
            nr, nc = cr + dirs[di][0], cc + dirs[di][1]
            nf, ndi = f, di
            if not (0 <= nr < 50 and 0 <= nc < 50):
                nf, ndi, nr, nc = change_faces(f, di, cr, cc)
            if faces[nf][nr, nc] == 1:
                break
            cr, cc = nr, nc
            f, di = nf, ndi


            # nr, nc = (cr + dirs[di][0]) % grid.shape[0], (cc + dirs[di][1]) % grid.shape[1]
            # while grid[nr, nc] == -1:
            #     nr, nc = (nr + dirs[di][0]) % grid.shape[0], (nc + dirs[di][1]) % grid.shape[1]
            # # print(nr, nc)
            # if grid[nr, nc] == 1:
            #     break
            # cr, cc = nr, nc
    else:
        if ins[i] == "R":
            di = (di + 1) % 4
        else:
            di = (di - 1) % 4
        i += 1

print(1000 * (cr + offset[f][0] + 1) + 4 * (cc + offset[f][1] + 1) + di)