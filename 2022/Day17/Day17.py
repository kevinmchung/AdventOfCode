import re
import pickle
from collections import defaultdict

def h(rocks):
    if rocks:
        return max(rocks, key=lambda r: r[1])[1]
    else:
        return -1

lines = open("Day17.txt", "r").read().split("\n")
dirs = lines[0]
di = 0
shapes = [['####'], ['.#.', '###', '.#.'], ['..#', '..#', '###'], ['#', '#', '#', '#'], ['##', '##']]
rocks = set()

seen = {}

vals = {}

cycle = 0

inter = lambda x, y, shape: any(shape[dy][dx] == "#" and (x + dx, y - dy) in rocks for dx in range(len(shape[0])) for dy in range(len(shape)))
i = 0
rem_val = 0
while True:
    height = h(rocks)
    vals[i] = height + 1
    column_heights = [height for _ in range(7)]
    for r in rocks:
        if height - r[1] < column_heights[r[0]]:
            column_heights[r[0]] = height - r[1]
    state = (i % 5, di, tuple(column_heights))
    # print(state)
    if state in seen:
        cycle = i - seen[state]
        break
    seen[state] = i
    r = i % 5
    shape = shapes[r]
    x = 2
    y = len(shape) + height + 3
    
    while True:
        if dirs[di] == "<" and x > 0 and not inter(x - 1, y, shape):
            x -= 1
        elif dirs[di] == ">" and x + len(shape[0]) < 7 and not inter(x + 1, y, shape):
            x += 1
        di = (di + 1) % len(dirs)
        if y - len(shape) + 1 > 0 and not inter(x, y - 1, shape):
            y -= 1
        else:
            for dx in range(len(shape[0])):
                for dy in range(len(shape)):
                    if shape[dy][dx] == "#":
                        rocks.add((x + dx, y - dy))
            break
    # for y in range(10, -1, -1):
    #     for x in range(7):
    #         if (x, y) in rocks:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
    # print("------")
    i += 1
    if i % 5 == 0 and di == 0:
        break

print(i, cycle)

start = i - cycle

n = 1000000000000 - start
m = n // cycle
rem = n % cycle

print(vals[start] + m * (vals[i] - vals[start]) + vals[rem + start] - vals[start])