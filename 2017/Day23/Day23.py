infile = open("Day23.txt", "r")

def getVal(v):
    if v.isalpha():
        return var[v]
    else:
        return int(v)

commands = [line.rstrip().split(" ") for line in infile.readlines()]
curCommand = 0
var = {chr(i):0 for i in range(97, 105)}
count = 0
while 0 <= curCommand < len(commands):
    cur = commands[curCommand]
    if cur[0] == "jnz":
        if getVal(cur[1]) != 0:
            curCommand += getVal(cur[2])
        else:
            curCommand += 1
    else:
        if cur[0] == "set":
            var[cur[1]] = getVal(cur[2])
        elif cur[0] == "sub":
            var[cur[1]] -= getVal(cur[2])
        elif cur[0] == "mul":
            count += 1
            var[cur[1]] *= getVal(cur[2])
        curCommand += 1
print(count)

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

h = 0
for i in range(106700, 123701, 17):
    if not isPrime(i):
        h += 1
print(h)