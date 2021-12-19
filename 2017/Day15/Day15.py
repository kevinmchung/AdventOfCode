genA = 873
genB = 583
numPairs = 5000000
count = 0
factorA = 16807
factorB = 48271
div = 2147483647

def updateA():
    global genA
    genA = (genA * factorA) % div

def updateB():
    global genB
    genB = (genB * factorB) % div

for i in range(numPairs):
    updateA()
    updateB()
    while genA % 4 != 0:
        updateA()
    while genB % 8 != 0:
        updateB()
    binA = bin(genA)[-16:]
    binA = "0" * (16 - len(binA)) + binA
    binB = bin(genB)[-16:]
    binB = "0" * (16 - len(binB)) + binB
    if binA == binB:
        count += 1
print(count)