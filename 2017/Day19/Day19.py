infile = open("Day19.txt", "r")

DOWN = (1, 0)
UP = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def checkDir(grid, r, c, direction):
    return grid[r + direction[0]][c + direction[1]]

lines = infile.readlines()
maxLen = 0
grid = []
for line in lines:
    if len(line) > maxLen:
        maxLen = len(line)
    grid.append(list(line.rstrip()))
for i in range(len(grid)):
    grid[i] += [' '] * (maxLen - len(grid[i]))
curR, curC = 0, 0
for i in range(maxLen):
    if grid[0][i] == "|":
        curC = i
direction = DOWN
letters = ""
count = 0
while grid[curR][curC] != ' ':
    count += 1
    cur = grid[curR][curC]
    if cur.isalpha():
        letters += cur
    elif cur == "+":
        if direction == DOWN or direction == UP:
            checkLeft = checkDir(grid, curR, curC, LEFT)
            if checkLeft == "-" or checkLeft.isalpha():
                direction = LEFT
            else:
                direction = RIGHT
        else:
            checkUp = checkDir(grid, curR, curC, UP)
            if checkUp == "|" or checkUp.isalpha():
                direction = UP
            else:
                direction = DOWN
    curR += direction[0]
    curC += direction[1]
print(letters)
print(count)