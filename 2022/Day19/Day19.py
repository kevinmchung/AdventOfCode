import re
from math import ceil
import numpy as np
from collections import defaultdict

lines = open("/Users/kevin/Documents/code/PycharmProjects/AdventOfCode/2022/Day19/Day19.txt", "r").read().split("\n")

costs = []

i = 0
while i < len(lines):
    line = lines[i]
    _, o1, o2, o3, c3, o4, b4 = map(int, re.findall(r"(\d+)", line))
    costs.append(((o1, 0, 0, 0), (o2, 0, 0, 0), (o3, c3, 0, 0), (o4, 0, b4, 0)))
    i += 1

# costs = (((4, 0, 0, 0), (2, 0, 0, 0), (3, 14, 0, 0), (2, 0, 7, 0)),
#          ((2, 0, 0, 0), (3, 0, 0, 0), (3, 8, 0, 0), (3, 0, 12, 0)),
#         )

# 3, 3, 3/9, 3/7

# costs = [costs[28]]

costs = costs[:3]

answers = [6, 0, 0, 0, 2, 12, 2, 0, 1, 0, 0, 1, 9, 0, 1, 4, 6, 0, 10, 0, 0, 2, 6, 2, 11, 2, 2, 3, 7, 3]

ans = 0
ans2 = 1
mins = 32

# for i in range(len(costs)):
#     starts = []

#     r = 1
#     robs = 1
#     rocks = 0
#     cost = costs[i][0][0]
#     for m in range(mins):
#         if robs == r:
#             starts.append((m, robs, rocks))
#             r += 1
#         if not any(r <= costs[i][j][0] for j in range(4)):
#             break
#         add_rob = False
#         if cost <= rocks:
#             rocks -= cost
#             add_rob = True
#         rocks += robs
#         if add_rob:
#             robs += 1

#     highest = 0
#     for tstart, bstart, rstart in starts:
#         cost = np.array(costs[i])
#         robs = np.array([bstart, 0, 0, 0])
#         rocks = np.array([rstart, 0, 0, 0])
#         for m in range(tstart, mins):
#             move = "_"
#             new_robs = np.array([0, 0, 0, 0])
#             print((cost[3][0] - rocks[0] + cost[2][0]) / robs[0], (cost[3][2] - rocks[2]) / robs[2])
#             print((cost[2][0] - rocks[0] + cost[1][0]) / robs[0], (cost[2][1] - rocks[1]) / robs[1])
#             print(((mins - m) * robs + rocks) / cost[2])
#             print(((mins - m) * (robs + np.array([0, 1, 0, 0])) + rocks - cost[1]) / cost[2])
#             if np.all(cost[3] <= rocks):
#                 if cost[3][0] <= rocks[0]:
#                     new_robs[3] += 1
#                     rocks -= cost[3]
#                     move = "G"
#             elif cost[2][1] <= rocks[1]:
#                 if robs[2] == 0 or ceil((cost[3][0] - rocks[0] + cost[2][0]) / robs[0]) <= ceil((cost[3][2] - rocks[2]) / robs[2]):
#                     new_robs[2] += 1
#                     rocks -= cost[2]
#                     move = "Ob"
#             elif cost[1][0] <= rocks[0]:
#                 if robs[1] == 0 or ceil((cost[2][0] - rocks[0] + cost[1][0]) / robs[0]) <= ceil((cost[2][1] - rocks[1]) / robs[1]):
#                     new_robs[1] += 1
#                     rocks -= cost[1]
#                     move = "C"
#             rocks += robs
#             robs += new_robs
#             print(m + 1, rocks, robs, move)
#             if rocks[3] > highest:
#                 highest = rocks[3]
#         print("--")
#     ans += highest * (i + 1)
#     if highest != answers[i]:
#         print(i + 1, highest)

cache = {}
highest = defaultdict(int)
def max_geodes(m, robs, rocks, cost, goal):
    global mins, cache, highest
    if m == mins:
        return rocks[3]
    
    if rocks[3] < highest[m] - 1:
        return 0
    if rocks[3] > highest[m]:
        highest[m] = rocks[3]

    max_ore = max(cost[i][0] for i in range(4))
    if (goal == 0 and robs[0] >= max_ore) or (goal == 1 and robs[1] >= cost[2][1]) or \
        (goal == 2 and (robs[2] >= cost[3][2] or robs[1] == 0)) or (goal == 3 and robs[2] == 0):
        return 0

    state = (m, robs, rocks, goal)
    if state in cache:
        return cache[state]

    maxval = 0
    while m < mins:
        if goal == 0 and cost[0][0] <= rocks[0]:
            temp = 0
            for g in range(4):
                newrocks = [rocks[i] + robs[i] for i in range(4)]
                newrocks[0] -= cost[0][0]
                newrobs = list(robs)
                newrobs[0] += 1
                temp = max(temp, max_geodes(m + 1, tuple(newrobs), tuple(newrocks), cost, g))
            maxval = max(maxval, temp)
            cache[state] = maxval
            return maxval
        elif goal == 1 and cost[1][0] <= rocks[0]:
            temp = 0
            for g in range(4):
                newrocks = [rocks[i] + robs[i] for i in range(4)]
                newrocks[0] -= cost[1][0]
                newrobs = list(robs)
                newrobs[1] += 1
                temp = max(temp, max_geodes(m + 1, tuple(newrobs), tuple(newrocks), cost, g))
            maxval = max(maxval, temp)
            cache[state] = maxval
            return maxval
        elif goal == 2 and cost[2][0] <= rocks[0] and cost[2][1] <= rocks[1]:
            temp = 0
            for g in range(4):
                newrocks = [rocks[i] + robs[i] for i in range(4)]
                newrocks[0] -= cost[2][0]
                newrocks[1] -= cost[2][1]
                newrobs = list(robs)
                newrobs[2] += 1
                temp = max(temp, max_geodes(m + 1, tuple(newrobs), tuple(newrocks), cost, g))
            maxval = max(maxval, temp)
            cache[state] = maxval
            return maxval
        elif goal == 3 and cost[3][0] <= rocks[0] and cost[3][2] <= rocks[2]:
            temp = 0
            for g in range(4):
                newrocks = [rocks[i] + robs[i] for i in range(4)]
                newrocks[0] -= cost[3][0]
                newrocks[2] -= cost[3][2]
                newrobs = list(robs)
                newrobs[3] += 1
                temp = max(temp, max_geodes(m + 1, tuple(newrobs), tuple(newrocks), cost, g))
            maxval = max(maxval, temp)
            cache[state] = maxval
            return maxval
        m += 1
        rocks = tuple(rocks[i] + robs[i] for i in range(4))
        maxval = max(maxval, rocks[3])

    cache[state] = maxval
    return maxval
                
for i in range(len(costs)):
    cache = {}
    highest = defaultdict(int)
    m = 0
    for g in range(4):
        m = max(m, max_geodes(0, (1, 0, 0, 0), (0, 0, 0, 0), costs[i], g))
    print(m)
    ans += m * (i + 1)
    ans2 *= m

print(ans)
print(ans2)
                