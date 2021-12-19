inputStr = "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"

def maxIndex(l):
    out = 0
    highest = l[0]
    for i in range(len(l)):
        if l[i] > highest:
            out = i
            highest = l[i]
    return out

banks = list(map(int, inputStr.split('\t')))
visited = {}
curCycle = 0
while tuple(banks) not in visited:
    visited[tuple(banks)] = curCycle
    m = maxIndex(banks)
    blocks = banks[m]
    banks[m] = 0
    for i in range(blocks):
        m = (m + 1) % len(banks)
        banks[m] += 1
    curCycle += 1
print(curCycle - visited[tuple(banks)])