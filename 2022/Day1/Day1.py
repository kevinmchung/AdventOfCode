# Part 1: 482
# Part 2: 741

lines = [line.strip() for line in open("Day1.txt", "r").readlines()]

elves = []
ans = 0
cur = 0
for i in range(0, len(lines)):
    line = lines[i]
    if len(line) > 0:
        cur += int(line)
    else:
        print(line)
        elves.append(cur)
        if cur > ans:
            ans = cur
        cur = 0


print(ans)
print(sum(sorted(elves)[-3:]))