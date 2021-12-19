infile = open("Day13.txt", "r")

def move(firewall, index, steps):
    pos = steps % (firewall[index] * 2 - 2)
    if pos < firewall[index]:
        return pos
    else:
        return firewall[index] * 2 - pos - 1

firewall = {}
for line in infile.readlines():
    info = line.split(": ")
    firewall[int(info[0])] = int(info[1])
delay = 0
while True:
    passed = True
    for i in firewall:
        if move(firewall, i, i + delay) == 0:
            passed = False
            break
    if passed:
        print(delay)
        break
    delay += 1