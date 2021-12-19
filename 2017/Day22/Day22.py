infile = open("Day22.txt", "r")

right = {(-1, 0):(0, 1), (0, 1):(1, 0), (1, 0):(0, -1), (0, -1):(-1, 0)}
left = {(-1, 0):(0, -1), (0, -1):(1, 0), (1, 0):(0, 1), (0, 1):(-1, 0)}
reverse = {(-1, 0):(1, 0), (1, 0):(-1, 0), (0, 1):(0, -1), (0, -1):(0, 1)}

lines = infile.readlines()
grid = [list(line.rstrip()) for line in lines]
r, c = len(grid) // 2, len(grid) // 2
direction = (-1, 0)
count = 0
for i in range(10000000):
    if r < 0:
        grid = [['.' for j in range(len(grid[0]))]] + grid
        r += 1
    elif r >= len(grid):
        grid += [['.' for j in range(len(grid[0]))]]
    elif c < 0:
        for j in range(len(grid)):
            grid[j] = ['.'] + grid[j]
        c += 1
    elif c >= len(grid[0]):
        for j in range(len(grid)):
            grid[j] += ['.']
    if grid[r][c] == "#":
        direction = right[direction]
        grid[r][c] = "F"
    elif grid[r][c] == "W":
        grid[r][c] = "#"
        count += 1
    elif grid[r][c] == ".":
        direction = left[direction]
        grid[r][c] = "W"
    elif grid[r][c] == "F":
        direction = reverse[direction]
        grid[r][c] = "."
    r += direction[0]
    c += direction[1]
print(count)