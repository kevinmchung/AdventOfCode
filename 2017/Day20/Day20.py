infile = open("Day20.txt", "r")

def getInfo(line):
    l = line.split(", ")
    for i in range(len(l)):
        l[i] = list(map(int, l[i][l[i].index("<") + 1:l[i].index(">")].split(",")))
    return l

def distance(pos):
    return sum(map(abs, pos))

def removeParticle(n):
    global numParticles
    velocities.pop(n)
    accelerations.pop(n)
    dist.pop(n)
    numParticles -= 1
    return positions.pop(n)

lines = infile.readlines()
positions = []
velocities = []
accelerations = []
dist = []
numParticles = 0
for line in lines:
    p, v, a = getInfo(line)
    positions.append(p)
    velocities.append(v)
    accelerations.append(a)
    dist.append(distance(p))
    numParticles += 1
for i in range(1000):
    for j in range(numParticles):
        for k in range(3):
            velocities[j][k] += accelerations[j][k]
            positions[j][k] += velocities[j][k]
            dist[j] = distance(positions[j])
    l = 0
    while l < numParticles:
        if positions.count(positions[l]) > 1:
            p = removeParticle(l)
            l -= 1
            while p in positions:
                removeParticle(positions.index(p))
        l += 1

print(numParticles)