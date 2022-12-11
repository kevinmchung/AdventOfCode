# Part 1: 144
# Part 2: 287

import re
from collections import defaultdict

lines = open("Day11.txt", "r").read().split("\n\n")
lines = [l.split("\n") for l in lines]

ans = 0

items = [[78, 53, 89, 51, 52, 59, 58, 85],
         [64],
         [71, 93, 65, 82],
         [67, 73, 95, 75, 56, 74],
         [85, 91, 90],
         [67, 96, 69, 55, 70, 83, 62],
         [53, 86, 98, 70, 64],
         [88, 64]]

ops = ["*3", "+7", "+5", "+8", "+4", "*2", "+6", "**2"]
test = [5, 2, 13, 19, 11, 3, 7, 17]

throw = [[7, 2], [6, 3], [4, 5], [0, 6], [1, 3], [1, 4], [0, 7], [5, 2]]
times = [0 for _ in range(8)]

# items = [[79, 98],
#          [54, 65, 75, 74],
#          [79, 60, 97],
#          [74]]

# ops = ["*19", "+6", "**2", "+3"]
# test = [23, 19, 13, 17]
# throw = [[3, 2], [0, 2], [3, 1], [1, 0]]
# times = [0 for _ in range(4)]

mod = 1
for t in test:
    mod *= t

for _ in range(10000):
    for i in range(8):
        while items[i]:
            item = items[i].pop(0)
            times[i] += 1
            n = eval(f"{item}{ops[i]}") % mod
            items[throw[i][n % test[i] == 0]].append(n)
            # print(i, item, n, items)

print(times)

print(ans)
