keystring = "hxtvlmkl"

def toHex(num):
    h = hex(num)[2:]
    return "0" * (2 - len(h)) + h

def hexToBin(hexNum):
    out = bin(int(hexNum, 16))[2:]
    return "0" * (4 - len(out)) + out

def knotHash(string):
    lengths = list(map(ord, string)) + [17, 31, 73, 47, 23]
    sparse = list(range(256))
    skip = 0
    cur = 0
    for n in range(64):
        for length in lengths:
            temp = []
            for i in range(cur, cur + length):
                temp.append(sparse[i % len(sparse)])
            for i in range(length):
                sparse[(cur + i) % len(sparse)] = temp[-i - 1]
            cur = (cur + length + skip) % len(sparse)
            skip += 1
    dense = []
    for i in range(16):
        bit = sparse[i * 16]
        for j in range(i * 16 + 1, (i + 1) * 16):
            bit ^= sparse[j]
        dense.append(bit)
    return "".join(list(map(toHex, dense)))

def fillRegion(grid, r, c):
    if not 0 <= r < 128 or not 0 <= c < 128 or grid[r][c] == "0":
        return
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    grid[r] = grid[r][:c] + "0" + grid[r][c + 1:]
    for i, j in directions:
        fillRegion(grid, r + i, c + j)

def findUsed(grid):
    for r in range(128):
        for c in range(128):
            if grid[r][c] == "1":
                return r, c
    return -1, -1

grid = []
for i in range(128):
    cur = keystring + "-" + str(i)
    h = knotHash(cur)
    grid.append("".join(list(map(hexToBin, h))))
numRegions = 0
while True:
    r, c = findUsed(grid)
    if r == -1:
        break
    numRegions += 1
    fillRegion(grid, r, c)
print(numRegions)