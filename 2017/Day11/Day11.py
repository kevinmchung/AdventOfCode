infile = open("Day11.txt", "r")

def dist(a, b):
    return sum([abs(a[i] - b[i]) for i in range(3)]) // 2

dirAdd = {"n":(1, 0, -1), "ne":(1, -1, 0), "se":(0, -1, 1), "s":(-1, 0, 1), "sw":(-1, 1, 0), "nw":(0, 1, -1)}
directions = infile.readline().split(",")
start = [0, 0, 0]
cur = [0, 0, 0]
maxDist = 0
for d in directions:
    toAdd = dirAdd[d]
    for i in range(3):
        cur[i] += toAdd[i]
    curDist = dist(start, cur)
    if curDist > maxDist:
        maxDist = curDist
print(maxDist)