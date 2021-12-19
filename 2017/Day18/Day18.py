infile = open("Day18.txt", "r")

send = [[], []]

def runCommand(c, var, id):
    global ans
    if c[0] == "set":
        if c[2].isalpha():
            var[c[1]] = var[c[2]]
        else:
            var[c[1]] = int(c[2])
    elif c[0] == "add":
        if c[2].isalpha():
            var[c[1]] += var[c[2]]
        else:
            var[c[1]] += int(c[2])
    elif c[0] == "mul":
        if c[2].isalpha():
            var[c[1]] *= var[c[2]]
        else:
            var[c[1]] *= int(c[2])
    elif c[0] == "mod":
        if c[2].isalpha():
            var[c[1]] %= var[c[2]]
        else:
            var[c[1]] %= int(c[2])
    elif c[0] == "snd":
        if id == 1:
            ans += 1
        if c[1].isalpha():
            send[id].append(var[c[1]])
        else:
            send[id].append(int(c[1]))
    elif c[0] == "rcv":
        if len(send[(id + 1) % 2]) > 0:
            v = send[(id + 1) % 2].pop(0)
            var[c[1]] = v
        else:
            return 0
    if c[0] == "jgz" and (c[1].isalpha() and var[c[1]]) > 0 or (not c[1].isalpha() and int(c[1]) > 0):
        if c[2].isalpha():
            return var[c[2]]
        else:
            return int(c[2])
    else:
        return 1

lines = infile.readlines()
commands = []
progVars = [{"p":0}, {"p":1}]
var = []
ans = 0
for line in lines:
    stuff = line.rstrip().split(" ")
    if stuff[1] not in var:
        var.append(stuff[1])
    commands.append(stuff)
for v in var:
    if v != "p":
        progVars[0][v] = 0
        progVars[1][v] = 0
curCommands = [0, 0]
locked = [False, False]
while not all(locked):
    for i in range(2):
        inc = runCommand(commands[curCommands[i]], progVars[i], i)
        if inc == 0:
            locked[i] = True
        else:
            locked[i] = False
            curCommands[i] += inc
print(ans)