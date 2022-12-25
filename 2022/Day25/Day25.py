# Part 1: 292
# Part 2: 244

import re
from collections import defaultdict
import numpy as np

lines = open('Day25.txt', 'r').read().split('\n')

ans = 0
i = 0
v = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
while i < len(lines):
    line = lines[i]
    c = 0
    j = 0
    while j < len(line):
        c += pow(5, j) * v[line[len(line) - j - 1]]
        j += 1
    ans += c
    i += 1

# ans = 906
print(ans)
ans2 = ''
j = 0
cs = '012=-'
while ans:
    d = cs[ans % 5]
    print(d)
    ans2 = d + ans2
    ans = (ans - v[d]) // 5
    j += 1

print(ans2)
