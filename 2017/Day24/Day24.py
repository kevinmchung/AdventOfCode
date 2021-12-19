class Component:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getOther(self, n):
        if n == self.a:
            return self.b
        return self.a

    def getStrength(self):
        return self.a + self.b

    def __contains__(self, n):
        return self.a == n or self.b == n

    def __hash__(self):
        return hash(str(self.a) + "/" + str(self.b))

def getBridge(components, used, num):
    maxLength = 0
    maxStrength = 0
    for c in components:
        if num in c and not used[c]:
            used[c] = True
            length, strength = getBridge(components, used, c.getOther(num))
            length += 1
            strength += c.getStrength()
            if length > maxLength:
                maxLength = length
                maxStrength = strength
            elif length == maxLength:
                if strength > maxStrength:
                    maxStrength = strength
            used[c] = False
    return maxLength, maxStrength

infile = open("Day24.txt", "r")

lines = infile.readlines()
components = []
for line in lines:
    nums = line.split("/")
    components.append(Component(int(nums[0]), int(nums[1])))
used = {c:False for c in components}
print(getBridge(components, used, 0))