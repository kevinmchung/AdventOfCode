# Part 1: 1167
# Part 2: 712

from collections import defaultdict
import re

lines = open("Day6.txt", "r").read().split("\n")
s = lines[0]

ans = 0
arr = []

for i in range(0, len(s), 1):
    print(s[i:i+14])
    if len(set(s[i:i+14])) == 14:
        print(i+14)
        break

print(ans)