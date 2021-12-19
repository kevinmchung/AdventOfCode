infile = open("Day9.txt", "r")
inputStr = infile.readline()
groupStarts = 0
score = 0
garbage = False
i = 0
ans = 0
while i < len(inputStr):
    if inputStr[i] == "!":
        i += 1
    elif garbage:
        if inputStr[i] == ">":
            garbage = False
        else:
            ans += 1
    else:
        if inputStr[i] == "<":
            garbage = True
        elif inputStr[i] == "{":
            groupStarts += 1
        elif inputStr[i] == "}" and groupStarts > 0:
            score += groupStarts
            groupStarts -= 1
    i += 1
print(ans)