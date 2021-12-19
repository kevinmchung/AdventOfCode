infile = open("Day25.txt", "r")

lines = infile.readlines()
state = [i[:-1] for i in lines.pop(0).rstrip().split(" ")][-1]
diagnostic = [int(i) for i in lines.pop(0).rstrip().split(" ") if i.isnumeric()][0]
curLine = 0
rules = {}
while curLine < len(lines):
    if "In state" in lines[curLine]:
        s = [i[:-1] for i in lines[curLine].rstrip().split(" ")][-1]
        rules[s] = {}
        curLine += 1
        for i in range(2):
            change = []
            curLine += 1
            for j in range(3):
                n = [i[:-1] for i in lines[curLine].rstrip().split(" ")][-1]
                if n == "right":
                    change.append(1)
                elif n == "left":
                    change.append(-1)
                elif n.isnumeric():
                    change.append(int(n))
                else:
                    change.append(n)
                curLine += 1
            rules[s][i] = change
    curLine += 1
tape = {0:0}
cur = 0
for i in range(diagnostic):
    if cur not in tape:
        tape[cur] = 0
    change = rules[state][tape[cur]]
    tape[cur] = change[0]
    cur += change[1]
    state = change[2]
print(sum(tape.values()))