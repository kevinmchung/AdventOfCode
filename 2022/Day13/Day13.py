# Part 1: 1031
# Part 2: 958

import re
from collections import defaultdict

lines = open("Day13.txt", "r").read().split("\n\n")

ans = 0

def compare(l, r):
    # print(l, r)
    if type(l) == int and type(r) == int:
        if l < r:
            return 1
        elif l == r:
            return 0
        else:
            return -1
    if type(l) == int:
        l = [l]
    if type(r) == int:
        r = [r]
    i = 0
    while i < len(l) and i < len(r):
        c = compare(l[i], r[i])
        if c == 1:
            return 1
        if c == -1:
            return -1
        i += 1
    if i == len(l) == len(r):
        return 0
    if i == len(l):
        return 1
    else:
        return -1

lists = [[[2]], [[6]]]

i = 0
while i < len(lines):
    line = lines[i]
    l, r = line.split("\n")
    l = eval(l)
    r = eval(r)
    lists.append(l)
    lists.append(r)
    if compare(l, r) == 1:
        ans += i + 1
    print(i + 1, compare(l, r))
    i += 1

print(ans)

for i in range(len(lists)):
    for j in range(0, len(lists) - i - 1):
        # print(lists[j], lists[j + 1])
        if compare(lists[j], lists[j + 1]) != 1:
            lists[j], lists[j + 1] = lists[j + 1], lists[j]

print((lists.index([[2]]) + 1) * (lists.index([[6]]) + 1))