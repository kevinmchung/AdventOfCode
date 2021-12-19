infile = open("Day8.txt", "r")

lines = infile.readlines()
variables = {}
largestVal = 0
for line in lines:
    instructions = line.rstrip().split(" ")
    instructions.remove("if")
    conditionVar = instructions[3]
    if conditionVar not in variables:
        variables[conditionVar] = 0
    check = instructions[4]
    val = int(instructions[5])
    true = False
    if check == "==":
        true = variables[conditionVar] == val
    elif check == "!=":
        true = variables[conditionVar] != val
    elif check == "<":
        true = variables[conditionVar] < val
    elif check == ">":
        true = variables[conditionVar] > val
    elif check == "<=":
        true = variables[conditionVar] <= val
    elif check == ">=":
        true = variables[conditionVar] >= val
    if true:
        var = instructions[0]
        if var not in variables:
            variables[var] = 0
        command = instructions[1]
        changeVal = int(instructions[2])
        if command == "inc":
            variables[var] += changeVal
        else:
            variables[var] -= changeVal
    highest = max(variables.values())
    if highest > largestVal:
        largestVal = highest
print(largestVal)