infile = open("Day5.txt", "r")

def trim(string):
    return string.rstrip()

maze = list(map(int, map(trim, infile.readlines())))
ans = 0
i = 0
while 0 <= i < len(maze):
    jump = maze[i]
    if maze[i] >= 3:
        maze[i] -= 1
    else:
        maze[i] += 1
    ans += 1
    i += jump
print(ans)