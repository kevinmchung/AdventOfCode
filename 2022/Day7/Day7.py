# Part 1: 3382
# Part 2: 2512

import re
from collections import defaultdict

lines = open("/Users/kevin/Documents/code/PycharmProjects/AdventOfCode/2022/Day7/Day7.txt", "r").read().split("\n")

ans = 0
dirs_in = ["/"]
sizes = defaultdict(int)

i = 0
while i < len(lines):
    line = lines[i]
    if line[0] == "$":
        line = line[2:].split(" ")
        if line[0] == "cd":
            if line[1] == "..":
                dirs_in.pop(-1)
            elif line[1] == "/":
                dirs_in = ["/"]
            else:
                dirs_in.append(line[1])
            i += 1
        elif line[0] == "ls":
            i += 1
            while  i < len(lines) and lines[i][0] != "$":
                l = lines[i].split(" ")
                if l[0].isnumeric():
                    s = ""
                    for d in dirs_in:
                        s += d + "/"
                        sizes[s] += int(l[0])
                i += 1

for d in sizes:
    if sizes[d] < 100000:
        ans += sizes[d]

print(ans)

unused = 70000000 - sizes['//']
need = 30000000 - unused

smallest = sizes['//']
for d in sizes:
    if sizes[d] > need and sizes[d] < smallest:
        smallest = sizes[d]
print(smallest)