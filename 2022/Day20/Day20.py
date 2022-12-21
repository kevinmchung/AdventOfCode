# Part 1: 559
# Part 2: 442

import re
from collections import defaultdict
import numpy as np

lines = open("Day20.txt", "r").read().split("\n")

l = []
prv = {}
nxt = {}

key = 811589153

ans = 0
idx = 0
while idx < len(lines):
    line = lines[idx]
    l.append((idx, int(line) * key))
    idx += 1

# print(l)

for i in range(len(lines)):
    prv[l[i]] = l[(i - 1) % len(lines)]
    nxt[l[i]] = l[(i + 1) % len(lines)]

for _ in range(10):
    for i in range(len(l)):
        # print(prv)
        # print(nxt)
        # print()
        node = l[i]
        if node[1] < 0:
            prv[nxt[node]] = prv[node]
            nxt[prv[node]] = nxt[node]
            cur = node
            for _ in range(abs(node[1]) % (len(l) - 1)):
                cur = prv[cur]
            prv[node] = prv[cur]
            nxt[node] = cur
            nxt[prv[cur]] = node
            prv[cur] = node
        elif node[1] > 0:
            prv[nxt[node]] = prv[node]
            nxt[prv[node]] = nxt[node]
            cur = node
            for _ in range(node[1] % (len(l) - 1)):
                cur = nxt[cur]
            prv[node] = cur
            nxt[node] = nxt[cur]
            prv[nxt[cur]] = node
            nxt[cur] = node

    

cur = None
for node in l:
    if node[1] == 0:
        cur = node
        break

for _ in range(3):
    for _ in range(1000):
        cur = nxt[cur]
    ans += cur[1]
    print(cur[1])

print(ans)
