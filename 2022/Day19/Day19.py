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
mins = 24

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

np.seterr(invalid="ignore", divide="ignore")
for i in range(len(costs)):
    cost = np.array(costs[i])

    max_robs = [max(c[j] for c in cost) for j in range(4)]
    max_robs[3] = 100
    
    highest = defaultdict(int)
    start = (0, (1, 0, 0, 0), (0, 0, 0, 0))
    # start = (8, (2, 2, 0, 0), (3, 2, 0, 0))
    q = [start]
    visited = {start}
    while q:
        m, robs, rocks = q.pop(0)

        if rocks[3] < highest[m] * 0.5:
            continue
        if rocks[3] > highest[m]:
            highest[m] = rocks[3]

        built = False
        
        for c in range(4):
            newrocks = np.array(rocks)
            newrobs = np.array([0, 0, 0, 0])

            t = (cost[c] - newrocks) / robs
            valid = True
            for j in range(4):
                if cost[c][j] > 0 and not np.isfinite(t)[j]:
                    valid = False
            
            
            if valid:
                dt = int(np.max(np.ceil(t[np.isfinite(t)]))) + 1
                if m + dt > mins:
                    continue
                newrocks += np.array(robs) * dt
                if robs[c] < max_robs[c]:
                    if c == 0:
                        if np.all(cost[c] <= newrocks) and robs[1] < 1:
                            build = True
                    elif c == 1:
                        if np.all(cost[c] <= newrocks):
                            build = True
                    elif c == 2:
                        if np.all(cost[c] <= newrocks):
                            build = True
                    elif c == 3:
                        if np.all(cost[c] <= newrocks):
                            build = True
                            
            if build:
                built = True
                newrobs[c] += 1
                newrocks -= cost[c]
                state = (m + dt, tuple(robs + newrobs), tuple(newrocks))
                # if state not in visited:
                #     visited.add(state)
                q.append(state)

    print(highest[mins])
    ans += highest[mins] * (i + 1)
    ans2 *= highest[mins]
                    

print(ans)
print(ans2)
                