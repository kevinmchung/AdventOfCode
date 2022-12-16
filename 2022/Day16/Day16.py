# Part 1: 257
# Part 2: 218

import re
from queue import PriorityQueue
from collections import defaultdict

lines = open("Day16.txt", "r").read().split("\n")

leads = {}
rates = {}
cands = ["AA"]

i = 0
while i < len(lines):
    line = lines[i]
    v = re.findall("Valve ([A-Z]+)", line)[0]
    r = int(re.findall("(\d+)", line)[0])
    l = line.split(", ")
    l[0] = l[0][-2:]
    leads[v] = l
    rates[v] = r
    if r > 0:
        cands.append(v)
    i += 1

graph = defaultdict(dict)
for c in cands:
    q = [(0, c)]
    visited = set([c])
    while q:
        cost, cur = q.pop(0)
        if cur != c and rates[cur] > 0:
            graph[c][cur] = cost
        for n in leads[cur]:
            if n not in visited:
                visited.add(n)
                q.append((cost + 1, n))


# q = PriorityQueue()
# q.put((0, "AA", ()))
# highest = 0
# lim = 30

# while not q.empty():
#     mins, cur, open = q.get()
#     # print(mins, cur, open)
#     p = 0
#     for o, t in open:
#         p += (lim - t) * rates[o]
#     if p > highest:
#         highest = p
#     for n in graph[cur]:
#         if not any(o[0] == n for o in open):
#             cost = graph[cur][n]
#             if mins + cost + 1 <= lim:
#                 q.put((mins + cost + 1, n, open + ((n, mins + cost + 1),)))

# print(highest)

pressures = defaultdict(int)
q = PriorityQueue()
q.put((0, "AA", ()))
lim = 26

while not q.empty():
    mins, cur, open = q.get()
    # print(mins, cur, open)
    p = 0
    oset = []
    for o, t in open:
        oset.append(o)
        p += (lim - t) * rates[o]
    oset = tuple(sorted(oset))
    if p > pressures[oset]:
        pressures[oset] = p
    for n in graph[cur]:
        if not any(o[0] == n for o in open): 
            cost = graph[cur][n]
            if mins + cost + 1 <= lim:
                q.put((mins + cost + 1, n, open + ((n, mins + cost + 1),)))
        
# print(pressures)
# print(len(pressures))

highest = 0
for k1 in pressures:
    for k2 in pressures:
        if len(set(k1).intersection(set(k2))) == 0:
            p = pressures[k1] + pressures[k2]
            if p > highest:
                highest = p

print(highest)
