from statistics import mode

infile = open("Day7.txt")
tower = {}
weights = {}
totalWeights = {}

def removeCommas(string):
    if "," in string:
        return string[:len(string) - 1]
    else:
        return string

def getInfo(line):
    lineList = line.rstrip().split(" ")
    try:
        lineList.remove("->")
    except ValueError:
        pass
    name = lineList[0]
    weight = int(lineList[1][1:len(lineList[1]) - 1])
    subs = list(map(removeCommas, lineList[2:]))
    return name, weight, subs

def unbalancedProgram(bottom):
    if len(tower[bottom]) == 0:
        totalWeights[bottom] = weights[bottom]
        return weights[bottom]
    subWeights = [unbalancedProgram(i) for i in tower[bottom]]
    containsStr = not all([type(i) is not str for i in subWeights])
    if containsStr:
        for i in subWeights:
            if type(i) is str:
                return i
    elif len(set(subWeights)) == 1:
        totalWeights[bottom] = weights[bottom] + sum(subWeights)
        return weights[bottom] + subWeights[0] * len(subWeights)
    else:
        totalWeights[bottom] = weights[bottom] + sum(subWeights)
        return bottom

lines = infile.readlines()
bottom = getInfo(lines[0])[0]
i = 0
while i < len(lines):
    name, weight, subs = getInfo(lines[i])
    tower[name] = subs
    weights[name] = weight
    if bottom in subs:
        bottom = name
        i = 0
    i += 1
unbalanced = unbalancedProgram(bottom)
commonWeight = mode([totalWeights[i] for i in tower[unbalanced]])
for i in tower[unbalanced]:
    if totalWeights[i] != commonWeight:
        print(commonWeight - sum([totalWeights[i] for i in tower[i]]))