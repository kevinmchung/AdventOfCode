infile = open("Day16.txt", "r")

commands = infile.readline().split(",")
numLetters = 16
pos = [chr(i + 97) for i in range(numLetters)]
for i in range(1000000000 % 24):
    for command in commands:
        c = command[0]
        command = command[1:]
        if c == "s":
            pos = pos[-int(command):] + pos[:-int(command)]
        else:
            command = command.split("/")
            if c == "x":
                a, b = int(command[0]), int(command[1])
            else:
                a, b = pos.index(command[0]), pos.index(command[1])
            temp = pos[a]
            pos[a] = pos[b]
            pos[b] = temp
print(''.join(pos))