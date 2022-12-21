# Part 1: 355
# Part 2: 371

import re
import numpy as np
from collections import defaultdict

lines = open("Day21.txt", "r").read().split("\n")

keys = []
ops = {}

ans = 0
i = 0
while i < len(lines):
    line = lines[i].split(": ")
    keys.append(line[0])
    if line[1].isnumeric():
        line[1] = int(line[1])
    ops[line[0]] = line[1]
    i += 1

ops['humn'] = 4234213782421

# i = 0
# while not all(type(ops[o]) == int for o in ops):
#     exp = ops[keys[i]]
#     if type(ops[keys[i]]) != int:
#         cs = "+-/*"
#         for c in cs:
#             if c in ops[keys[i]]:
#                 o1, o2 = exp.split(" " + c + " ")
#                 if type(ops[o1]) == int and type(ops[o2]) == int:
#                     ops[keys[i]] = int(eval(f"{ops[o1]}{c}{ops[o2]}"))
#                 break
#     i = (i + 1) % len(keys)
    # print(ops)


ops["humn"] = "inp"
while not all(type(ops[o]) == int or ops[o] == "inp" for o in ops):
    change = False
    for i in range(len(keys)):
        exp = ops[keys[i]]
        if type(ops[keys[i]]) != int:
            cs = "+-/*"
            for c in cs:
                if c in ops[keys[i]]:
                    o1, o2 = exp.split(" " + c + " ")
                    if type(ops[o1]) == int and type(ops[o2]) == int:
                        ops[keys[i]] = int(eval(f"{ops[o1]}{c}{ops[o2]}"))
                        change = True
                    break
    if not change:
        break

cur = 'root'
val = 0
if type(ops[ops[cur][:4]]) == int:
    val = ops[ops[cur][:4]]
    cur = ops[cur][-4:]
else:
    val = ops[ops[cur][-4:]]
    cur = ops[cur][:4]

while cur != 'humn':
    cs = '+-/*'
    for c in cs:
        if c in ops[cur]:
            o1, o2 = ops[cur].split(" " + c + " ")
            if type(ops[o1]) == int:
                if c == '+':
                    val -= ops[o1]
                elif c == '-':
                    val = ops[o1] - val
                elif c == '*':
                    val //= ops[o1]
                else:
                    val = ops[o1] // val
                cur = o2
                break
            else:
                if c == '+':
                    val -= ops[o2]
                elif c == '-':
                    val += ops[o2]
                elif c == '*':
                    val //= ops[o2]
                else:
                    val *= ops[o2]
                cur = o1
                break

print(val)

# print(ops)