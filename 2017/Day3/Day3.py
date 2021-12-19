num = 312051
dirChange = {(1, 0):(0, 1), (0, 1):(-1, 0), (-1, 0):(0, -1), (0, -1):(1, 0)}
xChange = [-1, 0, 1]
yChange = [-1, 0, 1]
size = int(num ** 0.5)
if size % 2 == 0:
    size += 1
else:
    size += 2
grid = [[0 for i in range(size)] for j in range(size)]
x, y = size // 2, size // 2
grid[x][y] = 1
direction = (1, 0)
while True:
    x += direction[0]
    y += direction[1]
    val = 0
    for i in xChange:
        for j in yChange:
            val += grid[x + i][y + j]
    grid[x][y] = val
    if val > num:
        print(val)
        break
    nextDir = dirChange[direction] # Doesn't necessarily change directions, this is just for checking
    if grid[x + nextDir[0]][y + nextDir[1]] == 0: # Change direction
        direction = dirChange[direction]