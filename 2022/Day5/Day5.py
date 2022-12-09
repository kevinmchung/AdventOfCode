# Part 1: 314
# Part 2: 160

import re
_, lines = open("Day5.txt", "r").read().split("\n\n")
lines = lines.split("\n")

stacks = ['DHRZSPWQ', 'FHQWRBV', 'HSVC', 'GFH', 'ZBJGP', 'LFWHJTQ', 'NJVLDWTZ', 'FHGJCZTD', 'HBMVPW']

ans = 0
ans2 = 0
arr = []

for i in range(0, len(lines), 1):
    line = lines[i]
    g = re.search(r"move (\d+) from (\d+) to (\d+)", line)
    print(g.groups())
    n, s1, s2 = map(int, g.groups())
    s1 -= 1
    s2 -= 1
    # stacks[s2] = stacks[s1][:n][::-1] + stacks[s2]
    stacks[s2] = stacks[s1][:n] + stacks[s2]
    stacks[s1] = stacks[s1][n:]
    print(stacks)
    # line = int(line)

print(''.join([c[0] for c in stacks]))
print(ans)
print(ans2)